import os
import io
import json
import re
from typing import Optional, Tuple

import duckdb
import pandas as pd
import streamlit as st

# Optional plotting support
import matplotlib.pyplot as plt

# Optional local LLM support via Ollama
try:
    import requests
except Exception:
    requests = None


st.set_page_config(page_title="AI Data Analyst", page_icon="📊", layout="wide")


# -----------------------------
# Helpers
# -----------------------------
def init_state() -> None:
    defaults = {
        "df": None,
        "table_name": "uploaded_data",
        "chat_history": [],
        "last_sql": "",
        "last_result": None,
        "llm_enabled": True,
        "ollama_model": "llama3",
        "ollama_base_url": "http://localhost:11434",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = []
    for col in df.columns:
        col = str(col).strip().lower()
        col = re.sub(r"[^a-z0-9]+", "_", col)
        col = re.sub(r"_+", "_", col).strip("_")
        cleaned.append(col or "column")
    df = df.copy()
    df.columns = cleaned
    return df


def load_file(uploaded_file) -> pd.DataFrame:
    name = uploaded_file.name.lower()
    if name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif name.endswith(".xlsx") or name.endswith(".xls"):
        df = pd.read_excel(uploaded_file)
    elif name.endswith(".json"):
        df = pd.read_json(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload CSV, Excel, or JSON.")
    return clean_column_names(df)


def register_df_in_duckdb(df: pd.DataFrame, table_name: str) -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(database=":memory:")
    con.register("temp_df", df)
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM temp_df")
    return con


def get_schema_prompt(df: pd.DataFrame, table_name: str) -> str:
    cols = []
    for col, dtype in zip(df.columns, df.dtypes):
        cols.append(f"- {col}: {dtype}")
    preview = df.head(5).to_dict(orient="records")
    return f"""
Table name: {table_name}
Columns:
{chr(10).join(cols)}

Sample rows:
{json.dumps(preview, indent=2, default=str)}
""".strip()


def run_sql(con: duckdb.DuckDBPyConnection, sql: str) -> pd.DataFrame:
    return con.execute(sql).df()


def extract_sql(text: str) -> str:
    code_block = re.search(r"```sql\s*(.*?)```", text, re.IGNORECASE | re.DOTALL)
    if code_block:
        return code_block.group(1).strip()

    select_match = re.search(
        r"(select\s+.*?;?$)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if select_match:
        return select_match.group(1).strip().rstrip(";")

    return text.strip().rstrip(";")


def ask_ollama(prompt: str, model: str, base_url: str) -> str:
    if requests is None:
        raise RuntimeError("The 'requests' package is not installed.")

    url = f"{base_url.rstrip('/')}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    data = response.json()
    return data.get("response", "")


def generate_sql_with_llm(question: str, df: pd.DataFrame, table_name: str) -> str:
    schema_info = get_schema_prompt(df, table_name)
    prompt = f"""
You are an expert data analyst.
Convert the user's question into one valid DuckDB SQL query.
Return only SQL in a ```sql``` block.

Rules:
- Use only the table `{table_name}`.
- Do not invent columns.
- Prefer simple, correct SQL.
- If the user asks for top values, use ORDER BY and LIMIT.
- If the question is ambiguous, make the most reasonable assumption based on the available columns.

{schema_info}

User question:
{question}
""".strip()

    raw = ask_ollama(
        prompt=prompt,
        model=st.session_state.ollama_model,
        base_url=st.session_state.ollama_base_url,
    )
    return extract_sql(raw)


def generate_fallback_sql(question: str, df: pd.DataFrame, table_name: str) -> Optional[str]:
    q = question.lower().strip()
    cols = list(df.columns)
    numeric_cols = [c for c in cols if pd.api.types.is_numeric_dtype(df[c])]

    if any(x in q for x in ["count", "how many", "number of rows", "total rows"]):
        return f"SELECT COUNT(*) AS total_rows FROM {table_name}"

    if any(x in q for x in ["show all", "preview", "sample", "first rows", "head"]):
        return f"SELECT * FROM {table_name} LIMIT 10"

    if "columns" in q or "schema" in q:
        return None

    if any(x in q for x in ["average", "avg", "mean"]) and numeric_cols:
        col = numeric_cols[0]
        return f"SELECT AVG({col}) AS average_{col} FROM {table_name}"

    if any(x in q for x in ["sum", "total"]) and numeric_cols:
        col = numeric_cols[0]
        return f"SELECT SUM({col}) AS total_{col} FROM {table_name}"

    if "max" in q and numeric_cols:
        col = numeric_cols[0]
        return f"SELECT MAX({col}) AS max_{col} FROM {table_name}"

    if "min" in q and numeric_cols:
        col = numeric_cols[0]
        return f"SELECT MIN({col}) AS min_{col} FROM {table_name}"

    for col in cols:
        if col in q:
            return f"SELECT {col}, COUNT(*) AS count FROM {table_name} GROUP BY {col} ORDER BY count DESC LIMIT 10"

    return f"SELECT * FROM {table_name} LIMIT 10"


def summarize_result(question: str, result_df: pd.DataFrame) -> str:
    if result_df is None or result_df.empty:
        return "No rows matched the query."
    if len(result_df) == 1 and len(result_df.columns) == 1:
        return f"The answer is **{result_df.iloc[0, 0]}**."
    return f"I found **{len(result_df)}** row(s). Review the table below."


def maybe_plot(df: pd.DataFrame):
    if df is None or df.empty:
        return

    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    non_numeric_cols = [c for c in df.columns if c not in numeric_cols]

    if len(df) > 0 and numeric_cols:
        st.subheader("Quick chart")

        if non_numeric_cols and numeric_cols:
            x_col = non_numeric_cols[0]
            y_col = numeric_cols[0]
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(df[x_col].astype(str).head(20), df[y_col].head(20))
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{y_col} by {x_col}")
            plt.xticks(rotation=45, ha="right")
            st.pyplot(fig)
        elif numeric_cols:
            y_col = numeric_cols[0]
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(df[y_col].head(50).reset_index(drop=True))
            ax.set_xlabel("Row index")
            ax.set_ylabel(y_col)
            ax.set_title(f"Trend of {y_col}")
            st.pyplot(fig)


# -----------------------------
# UI
# -----------------------------
init_state()

st.title("📊 AI Data Analyst App")
st.caption("Upload a file, ask questions in plain English, generate DuckDB SQL, and explore results locally.")

with st.sidebar:
    st.header("Settings")
    st.session_state.llm_enabled = st.toggle("Use local LLM via Ollama", value=st.session_state.llm_enabled)
    st.session_state.ollama_model = st.text_input("Ollama model", value=st.session_state.ollama_model)
    st.session_state.ollama_base_url = st.text_input("Ollama base URL", value=st.session_state.ollama_base_url)

    st.markdown("### Local setup")
    st.code("""pip install streamlit pandas duckdb openpyxl matplotlib requests\nollama pull llama3\nstreamlit run streamlit_data_analyst_app.py""", language="bash")

    st.markdown("### Example questions")
    st.write("- How many rows are in this file?")
    st.write("- Show the first 10 rows")
    st.write("- What is the average sales amount?")
    st.write("- Group by department and show counts")

uploaded_file = st.file_uploader("Upload CSV, Excel, or JSON", type=["csv", "xlsx", "xls", "json"])

if uploaded_file is not None:
    try:
        df = load_file(uploaded_file)
        st.session_state.df = df
        st.success(f"Loaded file successfully: {uploaded_file.name}")
    except Exception as e:
        st.error(f"Failed to load file: {e}")

if st.session_state.df is not None:
    df = st.session_state.df
    table_name = st.session_state.table_name
    con = register_df_in_duckdb(df, table_name)

    tab1, tab2, tab3 = st.tabs(["Data Preview", "Ask Questions", "Schema"])

    with tab1:
        st.subheader("Preview")
        st.dataframe(df.head(50), use_container_width=True)
        st.write(f"Rows: {len(df)} | Columns: {len(df.columns)}")

    with tab2:
        st.subheader("Ask a question")
        question = st.text_input("Ask about your data", placeholder="Example: What is the average sales amount by region?")

        col1, col2 = st.columns([1, 1])
        with col1:
            ask_btn = st.button("Generate answer", use_container_width=True)
        with col2:
            clear_btn = st.button("Clear history", use_container_width=True)

        if clear_btn:
            st.session_state.chat_history = []
            st.session_state.last_sql = ""
            st.session_state.last_result = None
            st.rerun()

        if ask_btn and question:
            sql = ""
            try:
                if st.session_state.llm_enabled:
                    sql = generate_sql_with_llm(question, df, table_name)
                else:
                    fallback = generate_fallback_sql(question, df, table_name)
                    if fallback is None and ("schema" in question.lower() or "columns" in question.lower()):
                        st.info("Columns: " + ", ".join(df.columns))
                    else:
                        sql = fallback or f"SELECT * FROM {table_name} LIMIT 10"
            except Exception as e:
                st.warning(f"LLM unavailable. Using fallback SQL. Details: {e}")
                sql = generate_fallback_sql(question, df, table_name) or f"SELECT * FROM {table_name} LIMIT 10"

            if sql:
                st.session_state.last_sql = sql
                try:
                    result_df = run_sql(con, sql)
                    st.session_state.last_result = result_df
                    answer = summarize_result(question, result_df)
                    st.session_state.chat_history.append({
                        "question": question,
                        "sql": sql,
                        "answer": answer,
                    })
                except Exception as e:
                    st.error(f"SQL execution failed: {e}")

        if st.session_state.last_sql:
            st.markdown("### Generated SQL")
            st.code(st.session_state.last_sql, language="sql")

        if st.session_state.last_result is not None:
            st.markdown("### Answer")
            st.write(summarize_result(question if question else "", st.session_state.last_result))
            st.dataframe(st.session_state.last_result, use_container_width=True)
            maybe_plot(st.session_state.last_result)

        if st.session_state.chat_history:
            st.markdown("### History")
            for idx, item in enumerate(reversed(st.session_state.chat_history), start=1):
                with st.expander(f"Question {idx}: {item['question']}"):
                    st.write(item["answer"])
                    st.code(item["sql"], language="sql")

    with tab3:
        st.subheader("Schema")
        schema_df = pd.DataFrame({
            "column_name": df.columns,
            "dtype": [str(x) for x in df.dtypes],
            "null_count": [int(df[c].isna().sum()) for c in df.columns],
            "unique_count": [int(df[c].nunique(dropna=True)) for c in df.columns],
        })
        st.dataframe(schema_df, use_container_width=True)

        st.markdown("### SQL reference")
        st.code(f"SELECT * FROM {table_name} LIMIT 10;", language="sql")
        st.code(f"SELECT COUNT(*) FROM {table_name};", language="sql")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            st.code(f"SELECT AVG({numeric_cols[0]}) FROM {table_name};", language="sql")
else:
    st.info("Upload a file to begin.")
