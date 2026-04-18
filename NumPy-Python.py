import numpy as np
import pandas as pd

arr = np.array([10,60,30,70,20])

print("Mean of array:: ",arr.mean())

print("Sum of array:: ",arr.sum())

print("Max of array:: ",arr.max())

print("Min of array:: ",arr.min())

print("Median of array:: ",np.median(arr))

arr = arr * 2  # Used in ML calculations

print(arr)

# 3. NumPy 2D Arrays (Matrix)
arr = np.array([[1,2], [3,4]])

print(arr.shape)
#Used for datasets (rows = data, columns = features)


# 4. Pandas Basics (DataFrame)

data = {'Name': ['Suresh','Sathish', 'Shanker'],
        'Salary': [50000, 60000, np.nan] };
df = pd.DataFrame(data);
print("DataSet created as below")
print(df);

print("Dataframe method head() called as below")
print(df.head())

print("Dataframe method info() called as below")
print(df.info())

print("Dataframe method describe() called as below")
print(df.describe())

print("Dataframe method salary column called as below")
print(df['Salary'])

print("Dataframe method salary column (> 50000) filter called as below")
print(df[df['Salary'] > 50000])

print("Dataframe method salary has any nulls then fillna() used or dropna() called as below")

df['Salary'] = df['Salary'].fillna(df['Salary'].median(),inplace=True)
print(df)

df['bonus'] = df['Salary'] * 2;

print(df)

#8. Grouping (Real-world use)
X = df[['Salary']].values

print(X)
