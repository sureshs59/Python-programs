# 🐼 Pandas Programming Exercises — Beginner to Expert

A comprehensive collection of Pandas exercises covering everything from basic DataFrame creation to advanced data pipelines. Each exercise includes a problem description, hints, and a collapsible solution.

---

## 📋 Table of Contents

- [Level Guide](#-level-guide)
- [🟢 Beginner — Core Basics](#-beginner--core-basics)
- [🟡 Elementary — Data Inspection & Selection](#-elementary--data-inspection--selection)
- [🟠 Intermediate — Data Cleaning & Transformation](#-intermediate--data-cleaning--transformation)
- [🔵 Upper Intermediate — GroupBy, Merge & Reshape](#-upper-intermediate--groupby-merge--reshape)
- [🔴 Advanced — Time Series, Apply & Performance](#-advanced--time-series-apply--performance)
- [⚫ Expert — Real-World Pipelines & Optimisation](#-expert--real-world-pipelines--optimisation)

---

## 📊 Level Guide

| Level | Label | Description |
|-------|-------|-------------|
| 🟢 **1** | Beginner | Creating Series/DataFrames, basic reading/writing, simple indexing |
| 🟡 **2** | Elementary | Inspection methods, slicing, filtering, basic stats |
| 🟠 **3** | Intermediate | Handling nulls, string ops, type conversion, apply/map |
| 🔵 **4** | Upper Intermediate | GroupBy, merge/join, pivot tables, reshaping |
| 🔴 **5** | Advanced | Time series, window functions, multi-index, custom aggregations |
| ⚫ **6** | Expert | Memory optimisation, method chaining pipelines, custom extensions |

---

## 🟢 Beginner — Core Basics

---

### B1 — Create a Series from a List

**Question:**
Create a Pandas Series from the list `[10, 20, 30, 40, 50]` and print it with its data type.

**Hints:**
- Use `pd.Series()`
- Access dtype with `.dtype`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
print("Data type:", s.dtype)
```

**Output:**
```
0    10
1    20
2    30
3    40
4    50
dtype: int64
Data type: int64
```
</details>

---

### B2 — Create a Series with Custom Index

**Question:**
Create a Series representing the population of 4 cities with city names as the index.

**Hints:**
- Pass an `index` parameter to `pd.Series()`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

population = pd.Series(
    [8_336_817, 3_979_576, 2_693_976, 2_300_000],
    index=["New York", "Los Angeles", "Chicago", "Houston"]
)
print(population)
print("\nPopulation of Chicago:", population["Chicago"])
```

**Output:**
```
New York       8336817
Los Angeles    3979576
Chicago        2693976
Houston        2300000
dtype: int64
```
</details>

---

### B3 — Create a DataFrame from a Dictionary

**Question:**
Create a DataFrame from the following data and print the first 3 rows:

| Name    | Age | Score |
|---------|-----|-------|
| Alice   | 25  | 85.5  |
| Bob     | 30  | 92.0  |
| Charlie | 22  | 78.3  |
| Diana   | 28  | 95.1  |
| Eve     | 35  | 88.7  |

**Hints:**
- Use a dictionary where keys are column names
- Use `.head(n)` to view first n rows

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

data = {
    "Name":  ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age":   [25, 30, 22, 28, 35],
    "Score": [85.5, 92.0, 78.3, 95.1, 88.7]
}

df = pd.DataFrame(data)
print(df.head(3))
```

**Output:**
```
      Name  Age  Score
0    Alice   25   85.5
1      Bob   30   92.0
2  Charlie   22   78.3
```
</details>

---

### B4 — Read a CSV File

**Question:**
Read a CSV file called `students.csv` into a DataFrame, display the first 5 rows, and print the shape of the DataFrame.

**Hints:**
- Use `pd.read_csv()`
- Use `.shape` to get (rows, columns)

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

# Create a sample CSV for demonstration
import io
csv_data = """Name,Age,Score,Grade
Alice,25,85.5,B
Bob,30,92.0,A
Charlie,22,78.3,C
Diana,28,95.1,A
Eve,35,88.7,B"""

df = pd.read_csv(io.StringIO(csv_data))

print("First 5 rows:")
print(df.head())
print("\nShape:", df.shape)
print("Rows:", df.shape[0], "| Columns:", df.shape[1])
```
</details>

---

### B5 — Write a DataFrame to CSV

**Question:**
Create a simple DataFrame and save it to `output.csv` without saving the row index.

**Hints:**
- Use `df.to_csv()`
- Pass `index=False` to exclude the index column

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Product": ["Apple", "Banana", "Cherry"],
    "Price":   [1.50, 0.75, 3.00],
    "Stock":   [100, 250, 80]
})

df.to_csv("output.csv", index=False)
print("Saved to output.csv")
print(df)
```
</details>

---

### B6 — Access Columns and Rows

**Question:**
Given a DataFrame of employees, demonstrate how to:
1. Select a single column
2. Select multiple columns
3. Access a specific row by index

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Name":       ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"],
    "Salary":     [60000, 85000, 72000]
})

# 1. Single column (returns a Series)
print("Single column:")
print(df["Name"])

# 2. Multiple columns (returns a DataFrame)
print("\nMultiple columns:")
print(df[["Name", "Salary"]])

# 3. Specific row by integer index
print("\nRow at index 1:")
print(df.iloc[1])

# 4. Row by label
print("\nRow where index label is 2:")
print(df.loc[2])
```
</details>

---

### B7 — Add and Remove Columns

**Question:**
Start with a DataFrame of products. Add a `Total Value` column (Price × Stock), then drop the `Stock` column.

**Hints:**
- Assign a new column using `df["new_col"] = ...`
- Use `df.drop(columns=[...])` to remove a column

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Product": ["Apple", "Banana", "Cherry"],
    "Price":   [1.50, 0.75, 3.00],
    "Stock":   [100, 250, 80]
})

# Add computed column
df["Total Value"] = df["Price"] * df["Stock"]
print("After adding column:")
print(df)

# Remove a column
df = df.drop(columns=["Stock"])
print("\nAfter dropping Stock:")
print(df)
```
</details>

---

### B8 — Basic Arithmetic on Columns

**Question:**
Given exam scores out of 50, create a percentage column and a pass/fail column (pass if percentage ≥ 60%).

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "Diana"],
    "Score":   [42, 28, 35, 47]
})

df["Percentage"] = (df["Score"] / 50) * 100
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 60 else "Fail")

print(df)
```

**Output:**
```
   Student  Score  Percentage Result
0    Alice     42        84.0   Pass
1      Bob     28        56.0   Fail
2  Charlie     35        70.0   Pass
3    Diana     47        94.0   Pass
```
</details>

---

## 🟡 Elementary — Data Inspection & Selection

---

### E1 — Inspect a DataFrame

**Question:**
Load a dataset and perform a full initial inspection: shape, column names, data types, summary statistics, and null counts.

**Hints:**
- Use `.info()`, `.describe()`, `.isnull().sum()`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":   ["Alice", "Bob", None, "Diana", "Eve"],
    "Age":    [25, 30, 22, None, 35],
    "Salary": [60000, 85000, 72000, 90000, 68000],
    "Dept":   ["HR", "IT", "IT", "Finance", "HR"]
})

print("=== Shape ===")
print(df.shape)

print("\n=== Column Names ===")
print(df.columns.tolist())

print("\n=== Data Types ===")
print(df.dtypes)

print("\n=== Summary Statistics ===")
print(df.describe())

print("\n=== Null Value Counts ===")
print(df.isnull().sum())

print("\n=== Info ===")
df.info()
```
</details>

---

### E2 — Boolean Filtering

**Question:**
Given a DataFrame of employees, filter to show:
1. Employees with salary > 70,000
2. Employees in the IT department
3. Employees in IT with salary > 80,000

**Hints:**
- Use `df[condition]`
- Combine conditions with `&` and `|` (not `and`/`or`)

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Dept":   ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [60000, 85000, 95000, 72000, 68000]
})

# 1. Salary > 70,000
print("Salary > 70,000:")
print(df[df["Salary"] > 70000])

# 2. IT department
print("\nIT Department:")
print(df[df["Dept"] == "IT"])

# 3. IT AND salary > 80,000
print("\nIT with Salary > 80,000:")
print(df[(df["Dept"] == "IT") & (df["Salary"] > 80000)])
```
</details>

---

### E3 — loc vs iloc

**Question:**
Demonstrate the difference between `.loc[]` (label-based) and `.iloc[]` (position-based) indexing using a DataFrame with a custom string index.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "City":       ["London", "Paris", "Tokyo", "Sydney"],
    "Population": [9_000_000, 2_100_000, 13_960_000, 5_312_000],
    "Country":    ["UK", "France", "Japan", "Australia"]
}, index=["LDN", "PAR", "TKY", "SYD"])

# loc — label based
print("loc['PAR']:")
print(df.loc["PAR"])

print("\nloc['LDN':'TKY', 'City':'Population']:")
print(df.loc["LDN":"TKY", "City":"Population"])

# iloc — position based
print("\niloc[0] (first row):")
print(df.iloc[0])

print("\niloc[1:3, 0:2] (rows 1-2, cols 0-1):")
print(df.iloc[1:3, 0:2])
```
</details>

---

### E4 — Sorting Data

**Question:**
Sort a sales DataFrame by revenue descending, then by region ascending when revenue is equal.

**Hints:**
- Use `df.sort_values(by=[...], ascending=[...])`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Region":  ["North", "South", "East", "West", "North", "South"],
    "Product": ["A", "B", "A", "C", "C", "A"],
    "Revenue": [15000, 22000, 15000, 8000, 31000, 19000]
})

sorted_df = df.sort_values(by=["Revenue", "Region"], ascending=[False, True])
print(sorted_df.reset_index(drop=True))
```
</details>

---

### E5 — Value Counts and Unique Values

**Question:**
From a survey DataFrame, find:
1. All unique departments
2. How many employees per department
3. The percentage breakdown by department

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"],
    "Dept":     ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance"]
})

print("Unique departments:", df["Dept"].unique())
print("Number of unique:", df["Dept"].nunique())

print("\nCount per department:")
print(df["Dept"].value_counts())

print("\nPercentage breakdown:")
print(df["Dept"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%")
```
</details>

---

### E6 — Conditional Column with np.where

**Question:**
Classify students as "High", "Medium", or "Low" performers based on their score.
- High: score ≥ 80
- Medium: score ≥ 60 and < 80
- Low: score < 60

**Hints:**
- Use `np.where()` or `pd.cut()`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Score":   [92, 55, 74, 88, 61]
})

# Method 1: np.where (nested)
df["Band_where"] = np.where(
    df["Score"] >= 80, "High",
    np.where(df["Score"] >= 60, "Medium", "Low")
)

# Method 2: pd.cut
df["Band_cut"] = pd.cut(
    df["Score"],
    bins=[0, 60, 80, 100],
    labels=["Low", "Medium", "High"],
    right=False
)

print(df)
```
</details>

---

### E7 — Renaming Columns and Index

**Question:**
Rename messy column names to clean snake_case names and reset the index.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "First Name": ["Alice", "Bob"],
    "Last Name ": ["Smith", "Jones"],
    " AGE":       [25, 30],
    "Salary ($)": [60000, 85000]
})

print("Before:")
print(df.columns.tolist())

# Method 1: rename specific columns
df = df.rename(columns={
    "First Name":  "first_name",
    "Last Name ":  "last_name",
    " AGE":        "age",
    "Salary ($)":  "salary_usd"
})

# Method 2 (general): strip and lowercase all at once
# df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w]", "", regex=True)

print("\nAfter:")
print(df.columns.tolist())
print(df)
```
</details>

---

## 🟠 Intermediate — Data Cleaning & Transformation

---

### I1 — Handle Missing Values

**Question:**
Given a DataFrame with missing values:
1. Identify columns with nulls and their counts
2. Fill numeric nulls with column median
3. Fill string nulls with "Unknown"
4. Drop rows where more than 2 values are missing

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":   ["Alice", None, "Charlie", "Diana", None],
    "Age":    [25, 30, None, 28, 35],
    "Salary": [60000, None, 72000, None, 68000],
    "Dept":   ["HR", "IT", None, "Finance", "HR"]
})

print("Null counts before:")
print(df.isnull().sum())

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill string columns with "Unknown"
string_cols = df.select_dtypes(include="object").columns
df[string_cols] = df[string_cols].fillna("Unknown")

print("\nAfter filling:")
print(df)
print("\nNull counts after:")
print(df.isnull().sum())
```
</details>

---

### I2 — Remove Duplicates

**Question:**
Given a dataset with duplicate entries:
1. Count duplicate rows
2. View the duplicate rows
3. Drop duplicates keeping the last occurrence
4. Drop duplicates based on a subset of columns

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Alice", "Charlie", "Bob", "Diana"],
    "Email":  ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com", "d@x.com"],
    "Score":  [85, 92, 85, 78, 95, 88]
})

print("Total rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("\nDuplicate entries:")
print(df[df.duplicated(keep=False)])

# Keep last occurrence
df_deduped = df.drop_duplicates(keep="last")
print("\nAfter dedup (keep last):")
print(df_deduped)

# Dedup by Name only
df_by_name = df.drop_duplicates(subset=["Name"], keep="first")
print("\nDedup by Name only:")
print(df_by_name)
```
</details>

---

### I3 — String Operations

**Question:**
Clean a messy names column: strip whitespace, standardise to title case, extract first and last names into separate columns, and filter names starting with "A".

**Hints:**
- Use `df["col"].str.strip()`, `.str.title()`, `.str.split()`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "full_name": ["  alice smith ", "BOB JONES", "charlie BROWN", " diana prince", "EVE ADAMS  "]
})

# Clean
df["full_name"] = df["full_name"].str.strip().str.title()

# Split into first / last
df[["first_name", "last_name"]] = df["full_name"].str.split(" ", n=1, expand=True)

# Filter names starting with A
starts_with_a = df[df["first_name"].str.startswith("A")]

print("Cleaned DataFrame:")
print(df)
print("\nNames starting with 'A':")
print(starts_with_a)
```
</details>

---

### I4 — Type Conversion

**Question:**
A DataFrame imported from CSV has all columns as strings. Convert them to appropriate types: date, integer, float, and category.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "date":     ["2024-01-15", "2024-02-20", "2024-03-10"],
    "quantity": ["100", "250", "80"],
    "price":    ["19.99", "34.50", "5.75"],
    "category": ["Electronics", "Clothing", "Electronics"]
})

print("Before:")
print(df.dtypes)

df["date"]     = pd.to_datetime(df["date"])
df["quantity"] = df["quantity"].astype(int)
df["price"]    = df["price"].astype(float)
df["category"] = df["category"].astype("category")

print("\nAfter:")
print(df.dtypes)
print("\nDataFrame:")
print(df)
```
</details>

---

### I5 — Apply and Map

**Question:**
Use `.apply()`, `.map()`, and `.applymap()` (`.map()` in newer Pandas) to transform columns.
1. Map a letter grade to a numeric GPA
2. Apply a function to normalise scores (0–1 range)
3. Apply a function element-wise to capitalise all strings

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "Diana"],
    "Grade":   ["A", "B", "C", "A"],
    "Score":   [92, 74, 61, 88]
})

# 1. map — dictionary lookup
grade_to_gpa = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
df["GPA"] = df["Grade"].map(grade_to_gpa)

# 2. apply — row/column level function
def normalise(series):
    return (series - series.min()) / (series.max() - series.min())

df["Score_norm"] = normalise(df["Score"])

# 3. apply on a string column
df["Student_upper"] = df["Student"].apply(str.upper)

print(df)
```
</details>

---

### I6 — Replace Values

**Question:**
Replace coded values in a dataset with human-readable labels, and replace outlier values with NaN.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Status": [1, 2, 3, 1, 2, 3, 1],
    "Score":  [85, 999, 72, 91, -1, 88, 76]
})

# Replace numeric codes
df["Status"] = df["Status"].replace({1: "Active", 2: "Inactive", 3: "Pending"})

# Replace invalid outliers with NaN
df["Score"] = df["Score"].replace(-1, np.nan)
df.loc[df["Score"] > 100, "Score"] = np.nan

print(df)
```
</details>

---

### I7 — String Pattern Extraction with Regex

**Question:**
Extract phone numbers, email domains, and numeric codes from messy text columns.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "contact": [
        "Call me at 555-123-4567",
        "Email: user@gmail.com, ID: #A001",
        "Phone: (800) 555-9876, Email: admin@company.org"
    ]
})

# Extract phone number
df["phone"] = df["contact"].str.extract(r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})")

# Extract email domain
df["email_domain"] = df["contact"].str.extract(r"@([\w.]+)")

# Extract ID code
df["id_code"] = df["contact"].str.extract(r"#([A-Z0-9]+)")

print(df[["phone", "email_domain", "id_code"]])
```
</details>

---

## 🔵 Upper Intermediate — GroupBy, Merge & Reshape

---

### U1 — GroupBy Aggregation

**Question:**
Group a sales DataFrame by region and product, computing total revenue, average revenue, and transaction count for each group.

**Hints:**
- Use `df.groupby().agg()`
- Pass a dictionary of `{column: function}` pairs

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Region":  ["North", "South", "North", "East", "South", "North", "East"],
    "Product": ["A", "A", "B", "A", "B", "A", "B"],
    "Revenue": [15000, 22000, 18000, 9000, 31000, 12000, 25000],
    "Units":   [100, 150, 120, 60, 200, 80, 170]
})

summary = df.groupby(["Region", "Product"]).agg(
    Total_Revenue=("Revenue", "sum"),
    Avg_Revenue=("Revenue", "mean"),
    Transactions=("Revenue", "count"),
    Total_Units=("Units", "sum")
).round(2)

print(summary)
```
</details>

---

### U2 — GroupBy with Transform

**Question:**
Add a column showing each employee's salary as a percentage of their department's total salary budget.

**Hints:**
- Use `groupby().transform()` to return a Series aligned with the original index

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Dept":   ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Salary": [85000, 92000, 60000, 65000, 78000, 82000]
})

df["Dept_Total"]   = df.groupby("Dept")["Salary"].transform("sum")
df["Pct_of_Dept"]  = (df["Salary"] / df["Dept_Total"] * 100).round(1)
df["Dept_Avg"]     = df.groupby("Dept")["Salary"].transform("mean").round(0)
df["Above_Avg"]    = df["Salary"] > df["Dept_Avg"]

print(df)
```
</details>

---

### U3 — Merge DataFrames (Joins)

**Question:**
Demonstrate all four types of joins (inner, left, right, outer) using an employees table and a departments table.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5],
    "name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "dept_id": [10, 20, 10, 30, 99]  # 99 has no match
})

departments = pd.DataFrame({
    "dept_id":   [10, 20, 30, 40],  # 40 has no match
    "dept_name": ["IT", "HR", "Finance", "Marketing"]
})

print("INNER JOIN (only matches):")
print(pd.merge(employees, departments, on="dept_id", how="inner"))

print("\nLEFT JOIN (all employees):")
print(pd.merge(employees, departments, on="dept_id", how="left"))

print("\nRIGHT JOIN (all departments):")
print(pd.merge(employees, departments, on="dept_id", how="right"))

print("\nOUTER JOIN (everything):")
print(pd.merge(employees, departments, on="dept_id", how="outer"))
```
</details>

---

### U4 — Concatenate DataFrames

**Question:**
Combine monthly sales reports (same columns) into a single yearly DataFrame, and combine employee info and their performance data (different column sets) side by side.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

# Vertical stack (same columns)
jan = pd.DataFrame({"Month": ["Jan"]*3, "Product": ["A","B","C"], "Sales": [100, 200, 150]})
feb = pd.DataFrame({"Month": ["Feb"]*3, "Product": ["A","B","C"], "Sales": [120, 180, 160]})
mar = pd.DataFrame({"Month": ["Mar"]*3, "Product": ["A","B","C"], "Sales": [110, 210, 140]})

yearly = pd.concat([jan, feb, mar], ignore_index=True)
print("Yearly (vertical stack):")
print(yearly)

# Horizontal stack (different columns, same rows)
info = pd.DataFrame({"Name": ["Alice", "Bob"], "Dept": ["IT", "HR"]})
perf = pd.DataFrame({"Score": [92, 78], "Rating": ["A", "B"]})

combined = pd.concat([info, perf], axis=1)
print("\nCombined (horizontal):")
print(combined)
```
</details>

---

### U5 — Pivot Table

**Question:**
Create a pivot table showing average sales by Region (rows) and Product (columns), with totals.

**Hints:**
- Use `pd.pivot_table()` with `margins=True`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Region":  ["North","South","East","West","North","South","East","West"],
    "Product": ["A","A","A","A","B","B","B","B"],
    "Sales":   [1200, 980, 1450, 870, 2100, 1800, 2300, 1600]
})

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc=np.mean,
    margins=True,
    margins_name="Total"
).round(0)

print(pivot)
```
</details>

---

### U6 — Melt (Wide to Long)

**Question:**
Convert a wide-format DataFrame (one column per month) to long format for easier plotting and analysis.

**Hints:**
- Use `pd.melt()`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

# Wide format
df_wide = pd.DataFrame({
    "Product": ["Widget A", "Widget B", "Widget C"],
    "Jan":     [100, 200, 150],
    "Feb":     [120, 180, 160],
    "Mar":     [110, 210, 140]
})

print("Wide format:")
print(df_wide)

# Melt to long format
df_long = pd.melt(
    df_wide,
    id_vars=["Product"],
    value_vars=["Jan", "Feb", "Mar"],
    var_name="Month",
    value_name="Sales"
)

print("\nLong format:")
print(df_long.sort_values(["Product", "Month"]).reset_index(drop=True))
```
</details>

---

### U7 — Stack and Unstack

**Question:**
Use `.stack()` and `.unstack()` to reshape a multi-level column DataFrame.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    ("Sales", "Q1"): {"North": 1000, "South": 1200},
    ("Sales", "Q2"): {"North": 1100, "South": 1300},
    ("Cost", "Q1"):  {"North": 600,  "South": 700},
    ("Cost", "Q2"):  {"North": 650,  "South": 720},
})

print("Original (MultiIndex columns):")
print(df)

# Stack columns into rows
stacked = df.stack()
print("\nStacked:")
print(stacked)

# Unstack back
print("\nUnstacked (back to original):")
print(stacked.unstack())
```
</details>

---

## 🔴 Advanced — Time Series, Apply & Performance

---

### A1 — Time Series Basics

**Question:**
Create a daily time series for a full year, resample to monthly totals and weekly averages.

**Hints:**
- Use `pd.date_range()` and `.resample()`

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

# Generate daily data
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
np.random.seed(42)
df = pd.DataFrame({
    "date":  dates,
    "sales": np.random.randint(100, 500, size=len(dates))
}).set_index("date")

print("Daily (first 5 rows):")
print(df.head())

# Monthly totals
monthly = df.resample("ME").sum()
print("\nMonthly totals:")
print(monthly)

# Weekly average
weekly = df.resample("W").mean().round(1)
print("\nWeekly averages (first 5):")
print(weekly.head())
```
</details>

---

### A2 — Rolling Windows

**Question:**
Calculate a 7-day rolling average and 30-day rolling standard deviation on a stock price series. Also compute the exponentially weighted moving average (EWMA).

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=90, freq="D")
prices = 100 + np.cumsum(np.random.randn(90))

df = pd.DataFrame({"price": prices}, index=dates)

df["MA_7"]    = df["price"].rolling(window=7).mean().round(2)
df["Std_30"]  = df["price"].rolling(window=30).std().round(2)
df["EWMA_12"] = df["price"].ewm(span=12, adjust=False).mean().round(2)

print(df.head(15))
print(f"\nFirst valid MA_7 at row: {df['MA_7'].first_valid_index()}")
```
</details>

---

### A3 — Lag Features and Diff

**Question:**
Create lag features (previous day, previous week) and compute day-over-day differences and percentage changes for a sales time series.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame({
    "date":  pd.date_range("2024-01-01", periods=14, freq="D"),
    "sales": np.random.randint(200, 600, 14)
}).set_index("date")

df["lag_1"]       = df["sales"].shift(1)           # yesterday
df["lag_7"]       = df["sales"].shift(7)           # last week
df["diff_1"]      = df["sales"].diff(1)            # day-over-day change
df["pct_change"]  = df["sales"].pct_change().mul(100).round(1)

print(df)
```
</details>

---

### A4 — Multi-Index DataFrames

**Question:**
Create a multi-index DataFrame (Region × Year), perform slicing on multiple index levels, and compute cross-section statistics.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

arrays = [
    ["North","North","South","South","East","East"],
    [2023, 2024, 2023, 2024, 2023, 2024]
]
index = pd.MultiIndex.from_arrays(arrays, names=["Region", "Year"])

df = pd.DataFrame({
    "Revenue": [150, 180, 130, 155, 200, 220],
    "Units":   [1000, 1200, 900, 1050, 1400, 1500]
}, index=index)

print("Multi-index DataFrame:")
print(df)

print("\nNorth only:")
print(df.loc["North"])

print("\nAll regions for 2024 (cross-section):")
print(df.xs(2024, level="Year"))

print("\nRevenue by Region (sum across years):")
print(df.groupby("Region")["Revenue"].sum())
```
</details>

---

### A5 — Custom Aggregation Functions

**Question:**
Apply multiple custom aggregation functions to groups: coefficient of variation, interquartile range, and a custom scoring formula.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Region":  ["North"]*5 + ["South"]*5,
    "Sales":   [120, 145, 110, 160, 130,  95, 200, 175, 190, 210]
})

def coeff_variation(x):
    return (x.std() / x.mean() * 100).round(2)

def iqr(x):
    return x.quantile(0.75) - x.quantile(0.25)

def performance_score(x):
    return ((x.mean() - x.min()) / (x.max() - x.min()) * 100).round(1)

result = df.groupby("Region")["Sales"].agg(
    Mean="mean",
    Median="median",
    Std="std",
    CV=coeff_variation,
    IQR=iqr,
    Perf_Score=performance_score
).round(2)

print(result)
```
</details>

---

### A6 — Window Functions with groupby

**Question:**
Rank each employee within their department by salary, and calculate the percentile of each salary within its department.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

df = pd.DataFrame({
    "Name":   ["Alice","Bob","Charlie","Diana","Eve","Frank","Grace","Hank"],
    "Dept":   ["IT","IT","IT","HR","HR","Finance","Finance","Finance"],
    "Salary": [92000,85000,98000,65000,72000,80000,88000,76000]
})

df["Rank_in_Dept"] = df.groupby("Dept")["Salary"].rank(ascending=False, method="min").astype(int)
df["Pct_in_Dept"]  = df.groupby("Dept")["Salary"].rank(pct=True).mul(100).round(1)
df["Dept_Max"]     = df.groupby("Dept")["Salary"].transform("max")
df["Gap_to_Top"]   = df["Dept_Max"] - df["Salary"]

print(df.sort_values(["Dept","Rank_in_Dept"]))
```
</details>

---

### A7 — Handling Large Files with Chunks

**Question:**
Process a large CSV file in chunks to compute the total revenue per region without loading the entire file into memory.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import io

# Simulate a large CSV
large_csv = "Region,Product,Revenue\n" + "\n".join(
    [f"{'North' if i%2==0 else 'South'},P{i%5},{(i+1)*100}" for i in range(1000)]
)

# Process in chunks
chunk_results = []
chunk_size = 200

for chunk in pd.read_csv(io.StringIO(large_csv), chunksize=chunk_size):
    chunk_summary = chunk.groupby("Region")["Revenue"].sum()
    chunk_results.append(chunk_summary)

# Combine all chunk results
final_result = pd.concat(chunk_results).groupby(level=0).sum()
print("Total Revenue by Region:")
print(final_result)
```
</details>

---

## ⚫ Expert — Real-World Pipelines & Optimisation

---

### X1 — Method Chaining Pipeline

**Question:**
Build a clean, readable data processing pipeline using method chaining to transform a raw sales dataset from ingestion to final analytical form.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

# Raw messy data
raw = pd.DataFrame({
    "  date ":    ["2024-01-15", "2024-02-20", "2024-01-15", "2024-03-10", None],
    "REGION":     ["North ", " South", "north", "EAST", "North"],
    "revenue":    ["$1,200", "$980", "$1,450", "$870", "$2,100"],
    "units":      ["100", "80", "120", "60", None],
    "rep name":   ["Alice Smith", "Bob Jones", "Alice Smith", "Charlie Brown", "Diana Prince"]
})

df = (
    raw
    # Clean column names
    .rename(columns=lambda c: c.strip().lower().replace(" ", "_"))
    # Drop rows with no date (critical field)
    .dropna(subset=["date"])
    # Parse types
    .assign(
        date     = lambda d: pd.to_datetime(d["date"]),
        region   = lambda d: d["region"].str.strip().str.title(),
        revenue  = lambda d: d["revenue"].str.replace(r"[$,]", "", regex=True).astype(float),
        units    = lambda d: pd.to_numeric(d["units"], errors="coerce").fillna(0).astype(int),
    )
    # Derived features
    .assign(
        month        = lambda d: d["date"].dt.month_name(),
        avg_price    = lambda d: (d["revenue"] / d["units"].replace(0, np.nan)).round(2),
        revenue_band = lambda d: pd.cut(d["revenue"], bins=[0,1000,1500,np.inf],
                                        labels=["Low","Medium","High"])
    )
    # Sort
    .sort_values("date")
    .reset_index(drop=True)
)

print(df)
print("\nDtypes:")
print(df.dtypes)
```
</details>

---

### X2 — Memory Optimisation

**Question:**
Optimise a large DataFrame's memory usage by downcasting numeric types and converting appropriate string columns to categorical.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

# Simulate a large dataset
np.random.seed(42)
n = 100_000

df = pd.DataFrame({
    "id":       np.random.randint(1, 10_000, n),
    "region":   np.random.choice(["North","South","East","West"], n),
    "product":  np.random.choice([f"P{i:03d}" for i in range(50)], n),
    "revenue":  np.random.uniform(100, 10000, n),
    "units":    np.random.randint(1, 500, n),
    "rating":   np.random.randint(1, 6, n),
})

def memory_usage(df):
    return df.memory_usage(deep=True).sum() / 1024**2  # MB

print(f"Before: {memory_usage(df):.2f} MB")
print(df.dtypes)

# Optimise
df_opt = df.copy()
df_opt["id"]      = pd.to_numeric(df_opt["id"],      downcast="unsigned")
df_opt["revenue"] = pd.to_numeric(df_opt["revenue"],  downcast="float")
df_opt["units"]   = pd.to_numeric(df_opt["units"],    downcast="unsigned")
df_opt["rating"]  = pd.to_numeric(df_opt["rating"],   downcast="unsigned")
df_opt["region"]  = df_opt["region"].astype("category")
df_opt["product"] = df_opt["product"].astype("category")

print(f"\nAfter: {memory_usage(df_opt):.2f} MB")
print(df_opt.dtypes)
reduction = (1 - memory_usage(df_opt)/memory_usage(df)) * 100
print(f"\nMemory reduced by {reduction:.1f}%")
```
</details>

---

### X3 — Custom Pandas Accessor (Extension)

**Question:**
Create a custom DataFrame accessor called `.profiler` that adds domain-specific helper methods: `.summary()`, `.outlier_report()`, and `.completeness()`.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

@pd.api.extensions.register_dataframe_accessor("profiler")
class ProfilerAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def summary(self):
        df = self._obj
        return pd.DataFrame({
            "dtype":    df.dtypes,
            "nulls":    df.isnull().sum(),
            "null_pct": (df.isnull().mean() * 100).round(1),
            "unique":   df.nunique(),
        })

    def outlier_report(self, cols=None):
        df = self._obj
        num_cols = cols or df.select_dtypes(include="number").columns.tolist()
        records = []
        for col in num_cols:
            q1, q3 = df[col].quantile([0.25, 0.75])
            iqr = q3 - q1
            outliers = df[(df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)]
            records.append({"column": col, "outlier_count": len(outliers),
                            "lower_fence": q1 - 1.5*iqr, "upper_fence": q3 + 1.5*iqr})
        return pd.DataFrame(records).set_index("column")

    def completeness(self):
        pct = (1 - self._obj.isnull().mean()) * 100
        return f"Overall completeness: {pct.mean():.1f}%\n" + str(pct.round(1))


# Demo
np.random.seed(0)
df = pd.DataFrame({
    "age":    [25, 30, None, 28, 999, 35],
    "salary": [60000, None, 72000, 90000, 68000, 85000],
    "dept":   ["HR", "IT", None, "Finance", "HR", "IT"]
})

print("=== Summary ===")
print(df.profiler.summary())

print("\n=== Outlier Report ===")
print(df.profiler.outlier_report())

print("\n=== Completeness ===")
print(df.profiler.completeness())
```
</details>

---

### X4 — Full ETL Pipeline

**Question:**
Build a complete Extract-Transform-Load pipeline that:
1. Loads data from multiple sources
2. Cleans and validates it
3. Enriches with derived features
4. Aggregates into a reporting table
5. Exports to CSV and prints a quality report

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np
from datetime import datetime

# ── EXTRACT ──────────────────────────────────────────────────────────────────
np.random.seed(42)
n = 200

transactions = pd.DataFrame({
    "txn_id":     range(1, n+1),
    "date":       pd.date_range("2024-01-01", periods=n, freq="D").strftime("%Y-%m-%d"),
    "customer_id": np.random.randint(1000, 1050, n),
    "product_id": np.random.choice(["P01","P02","P03","P04"], n),
    "quantity":   np.random.randint(1, 20, n),
    "unit_price": np.random.uniform(10, 200, n).round(2),
    "region":     np.random.choice(["North","South","East","West"], n),
})
# Inject nulls and bad data
transactions.loc[[5,15,25], "quantity"] = None
transactions.loc[[10,20],    "unit_price"] = -99

products = pd.DataFrame({
    "product_id":   ["P01","P02","P03","P04"],
    "product_name": ["Widget A","Widget B","Gadget X","Gadget Y"],
    "category":     ["Widgets","Widgets","Gadgets","Gadgets"],
    "cost_price":   [20, 35, 60, 45]
})

# ── TRANSFORM ─────────────────────────────────────────────────────────────────
quality_report = {}

def etl_pipeline(txn, prod):
    # 1. Parse and clean
    df = (
        txn
        .assign(date=lambda d: pd.to_datetime(d["date"]))
        .assign(quantity=lambda d: pd.to_numeric(d["quantity"], errors="coerce"))
        .assign(unit_price=lambda d: d["unit_price"].where(d["unit_price"] > 0, np.nan))
    )

    quality_report["rows_raw"] = len(df)
    quality_report["nulls_before"] = df.isnull().sum().sum()

    # 2. Fill / drop
    df["quantity"] = df["quantity"].fillna(df["quantity"].median()).astype(int)
    df = df.dropna(subset=["unit_price"])

    quality_report["rows_after_clean"] = len(df)

    # 3. Enrich
    df = df.merge(prod, on="product_id", how="left")
    df["revenue"]      = (df["quantity"] * df["unit_price"]).round(2)
    df["gross_profit"] = (df["revenue"] - df["quantity"] * df["cost_price"]).round(2)
    df["margin_pct"]   = (df["gross_profit"] / df["revenue"] * 100).round(1)
    df["month"]        = df["date"].dt.to_period("M")

    # 4. Aggregate
    report = (
        df.groupby(["month","region","category"])
        .agg(
            Total_Revenue=("revenue", "sum"),
            Total_Profit=("gross_profit", "sum"),
            Avg_Margin=("margin_pct", "mean"),
            Transactions=("txn_id", "count")
        )
        .round(2)
        .reset_index()
    )

    quality_report["output_rows"] = len(report)
    return report

report_df = etl_pipeline(transactions, products)

# ── LOAD ──────────────────────────────────────────────────────────────────────
report_df.to_csv("sales_report.csv", index=False)

print("=== ETL QUALITY REPORT ===")
for k, v in quality_report.items():
    print(f"  {k}: {v}")

print("\n=== OUTPUT SAMPLE ===")
print(report_df.head(8).to_string(index=False))
```
</details>

---

### X5 — Vectorised Operations vs loops (Performance)

**Question:**
Compare the performance of a loop-based approach vs vectorised Pandas operations vs NumPy for computing a compound scoring formula across 1 million rows.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np
import time

np.random.seed(0)
n = 1_000_000

df = pd.DataFrame({
    "revenue":  np.random.uniform(100, 10000, n),
    "units":    np.random.randint(1, 500, n),
    "discount": np.random.uniform(0, 0.3, n),
    "rating":   np.random.randint(1, 6, n),
})

# Formula: score = (revenue * (1 - discount)) / units * log(rating + 1)

# Method 1: Python loop (slow — shown on small sample)
sample = df.head(10_000).copy()
t0 = time.time()
scores = []
for _, row in sample.iterrows():
    score = (row["revenue"] * (1 - row["discount"])) / row["units"] * np.log(row["rating"] + 1)
    scores.append(score)
sample["score_loop"] = scores
t_loop = time.time() - t0
print(f"Loop (10k rows):      {t_loop:.3f}s")

# Method 2: Pandas vectorised
t0 = time.time()
df["score_pandas"] = (
    (df["revenue"] * (1 - df["discount"])) / df["units"] * np.log(df["rating"] + 1)
)
t_pandas = time.time() - t0
print(f"Pandas vectorised (1M rows): {t_pandas:.3f}s")

# Method 3: NumPy (fastest)
t0 = time.time()
df["score_numpy"] = (
    (df["revenue"].values * (1 - df["discount"].values)) /
    df["units"].values *
    np.log(df["rating"].values + 1)
)
t_numpy = time.time() - t0
print(f"NumPy (1M rows):     {t_numpy:.3f}s")

print(f"\nLoop is ~{t_loop/(t_numpy*(10_000/n)):.0f}x slower per row than NumPy")
```
</details>

---

### X6 — Advanced GroupBy with Named Aggregations and Filtering

**Question:**
Perform a complex grouped analysis: compute multiple named aggregations, filter groups based on aggregate conditions, and rank groups.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

np.random.seed(7)
df = pd.DataFrame({
    "rep":     np.random.choice([f"Rep_{i}" for i in range(1, 11)], 300),
    "region":  np.random.choice(["North","South","East","West"], 300),
    "product": np.random.choice(["A","B","C"], 300),
    "revenue": np.random.uniform(500, 5000, 300).round(2),
    "closed":  np.random.choice([True, False], 300, p=[0.6, 0.4])
})

# Named aggregations
summary = df.groupby(["region","rep"]).agg(
    Total_Rev     = ("revenue","sum"),
    Deals_Won     = ("closed","sum"),
    Total_Deals   = ("closed","count"),
    Avg_Deal_Size = ("revenue","mean"),
    Best_Deal     = ("revenue","max"),
).round(2)

summary["Win_Rate"]      = (summary["Deals_Won"] / summary["Total_Deals"] * 100).round(1)
summary["Region_Rank"]   = summary.groupby("region")["Total_Rev"].rank(ascending=False, method="min").astype(int)

# Filter: only reps with win rate > 55% and total revenue > 50,000
top_reps = summary[(summary["Win_Rate"] > 55) & (summary["Total_Rev"] > 50_000)]

print("Top reps (Win rate > 55%, Revenue > 50k):")
print(top_reps.sort_values("Total_Rev", ascending=False))
```
</details>

---

### X7 — Fuzzy Deduplication with String Similarity

**Question:**
Detect and merge near-duplicate company names in a DataFrame using string distance techniques.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd

# Simulate messy company data
df = pd.DataFrame({
    "company": [
        "Apple Inc", "Apple Incorporated", "Microsoft Corp",
        "microsoft corporation", "Google LLC", "Alphabet Inc",
        "Amazon", "Amazon.com Inc", "Meta Platforms",
        "Facebook Inc", "Netflix", "NETFLIX INC"
    ],
    "revenue": [394, 382, 211, 198, 282, 257, 514, 499, 116, 118, 31, 29]
})

# Normalise names
df["company_clean"] = (
    df["company"]
    .str.lower()
    .str.replace(r"\b(inc|incorporated|corp|corporation|llc|ltd|com|platforms)\b", "", regex=True)
    .str.replace(r"[^\w\s]", "", regex=True)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

print("Normalised names:")
print(df[["company", "company_clean", "revenue"]])

# Group by cleaned name and aggregate
aggregated = (
    df.groupby("company_clean")
    .agg(
        aliases  = ("company", lambda x: " | ".join(sorted(set(x)))),
        total_revenue = ("revenue", "sum"),
        records  = ("company", "count")
    )
    .reset_index()
    .sort_values("total_revenue", ascending=False)
)

print("\nAggregated (deduplicated):")
print(aggregated)
```
</details>

---

### X8 — Time Series Forecasting Features

**Question:**
Engineer a comprehensive set of time series features for a machine learning model: calendar features, lag features, rolling statistics, and holiday flags.

<details>
<summary>💡 View Solution</summary>

```python
import pandas as pd
import numpy as np

# Generate daily sales data for 2 years
np.random.seed(42)
dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")
trend = np.linspace(100, 200, len(dates))
seasonality = 30 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
noise = np.random.normal(0, 10, len(dates))
sales = trend + seasonality + noise

df = pd.DataFrame({"date": dates, "sales": sales.round(2)}).set_index("date")

# ── Calendar features
df["day_of_week"]   = df.index.dayofweek          # 0=Mon
df["day_of_month"]  = df.index.day
df["week_of_year"]  = df.index.isocalendar().week.astype(int)
df["month"]         = df.index.month
df["quarter"]       = df.index.quarter
df["year"]          = df.index.year
df["is_weekend"]    = df["day_of_week"].isin([5, 6]).astype(int)
df["is_month_end"]  = df.index.is_month_end.astype(int)
df["is_month_start"]= df.index.is_month_start.astype(int)

# ── Lag features
for lag in [1, 7, 14, 30]:
    df[f"lag_{lag}"] = df["sales"].shift(lag)

# ── Rolling features
for window in [7, 14, 30]:
    df[f"rolling_mean_{window}"]  = df["sales"].shift(1).rolling(window).mean().round(2)
    df[f"rolling_std_{window}"]   = df["sales"].shift(1).rolling(window).std().round(2)

# ── Simple holiday proxy (US major holidays approximate)
holidays = pd.to_datetime([
    "2023-01-01","2023-07-04","2023-12-25","2023-11-23",
    "2024-01-01","2024-07-04","2024-12-25","2024-11-28"
])
df["is_holiday"] = df.index.isin(holidays).astype(int)

print("Feature-engineered DataFrame shape:", df.shape)
print("\nFeature list:")
print(df.columns.tolist())
print("\nSample (first 35 rows, key cols):")
cols = ["sales","day_of_week","is_weekend","lag_1","lag_7","rolling_mean_7","is_holiday"]
print(df[cols].head(35).tail(10))
```
</details>

---

## 📝 Quick Reference Cheat Sheet

### Creating Data
```python
pd.Series([1,2,3])                          # Series from list
pd.DataFrame({"col": [1,2,3]})              # DataFrame from dict
pd.read_csv("file.csv")                     # Read CSV
pd.read_excel("file.xlsx", sheet_name=0)    # Read Excel
pd.read_json("file.json")                   # Read JSON
```

### Inspection
```python
df.shape          # (rows, cols)
df.dtypes         # column types
df.info()         # full summary
df.describe()     # stats for numeric columns
df.head(n)        # first n rows
df.isnull().sum() # null counts per column
```

### Selection
```python
df["col"]               # single column (Series)
df[["a","b"]]           # multiple columns
df.loc[label]           # row by label
df.iloc[0]              # row by position
df[df["col"] > 5]       # boolean filter
df.query("col > 5")     # query string
```

### Cleaning
```python
df.dropna()                          # drop any null rows
df.fillna(value)                     # fill nulls
df.drop_duplicates()                 # remove duplicates
df["col"].astype(int)                # cast type
df["col"].str.strip().str.lower()    # string cleaning
pd.to_datetime(df["col"])            # parse dates
```

### Aggregation
```python
df.groupby("col").agg({"num": "sum"})   # groupby + agg
df.pivot_table(values, index, columns)   # pivot
df.merge(other, on="key", how="left")    # join
pd.concat([df1, df2])                    # stack vertically
```

### Time Series
```python
pd.date_range("2024-01", periods=12, freq="ME")   # date range
df.resample("ME").sum()                             # resample monthly
df["col"].rolling(7).mean()                        # rolling average
df["col"].shift(1)                                 # lag by 1
df.index.dt.month                                  # extract month
```

---

## 🔧 Setup

```bash
pip install pandas numpy
```

```python
import pandas as pd
import numpy as np

# Recommended display settings
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)
pd.set_option("display.float_format", "{:.2f}".format)
```

---

*Happy wrangling! 🐼*
