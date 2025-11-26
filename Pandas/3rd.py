import pandas as pd

df = pd.DataFrame({
    'ID': [1, 2, 3, 2, 4, 1, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Diana', 'Alice', 'Eve'],
    'City': ['NYC', 'LA', 'Chicago', 'LA', 'NYC', 'NYC', 'Boston']
})

print(df)


print("Duplicate check (True means duplicated):")
print(df.duplicated())

# 3. Remove duplicates
df_cleaned = df.drop_duplicates()
print("\nCleaned DataFrame (after removing duplicates):")
print(df_cleaned)

# 4. Show row counts before/after
print(f"\nRows before cleaning: {len(df)}")
print(f"Rows after cleaning: {len(df_cleaned)}")