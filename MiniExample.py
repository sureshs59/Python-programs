import pandas as pd
from sklearn.linear_model import LinearRegression

# data
df = pd.DataFrame({
    "experience": [1,2,3],
    "salary" : [30000,40000,50000]
})

# features
X = df[["experience"]]
y = df["salary"]

# model
model = LinearRegression()
model.fit(X, y)

print(model.predict([[4]]))

