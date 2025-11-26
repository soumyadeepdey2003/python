import pandas as pd

df = pd.DataFrame({
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve' ],
    'Math': [85, 92, None, 78, 88],
    'Science': [90, None, 88, 95, 92],
    'English': [88, 85, 90, None, 95]
})

print(df)
print(df.dropna())
print(df)

df2=df.dropna()

df2.to_csv("Pandas/test.csv")
