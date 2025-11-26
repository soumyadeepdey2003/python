import pandas as pd

try:
    # Load the JSON file into a DataFrame
    df = pd.read_json("Pandas/data.json")
    print("Original DataFrame:")
    print(df.head())
    print("\nMissing values by column:")
    print(df.isnull().sum())

    # Fill NULLs in Duration, Pulse, Maxpulse, Calories with mean for each
    for col in ['Duration', 'Pulse', 'Maxpulse', 'Calories']:
        df[col].fillna(df[col].mean(), inplace=True)

    # Validate: Duration > 120, set to 120 and print warning
    if (df['Duration'] > 120).any():
        print("Warning: Duration values >120 found. Replacing with 120.")
        df.loc[df['Duration'] > 120, 'Duration'] = 120

    # Validate: Pulse out of 60–200 range, print warning
    if ((df['Pulse'] < 60) | (df['Pulse'] > 200)).any():
        print("Warning: Pulse values outside 60–200 found.")

    print("\nCleaned DataFrame sample:")
    print(df.head())
    print("\nAll operations completed successfully!")

except FileNotFoundError:
    print("Error: data.json file not found!")
except ValueError as e:
    print(f"Error: Invalid JSON format – {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
