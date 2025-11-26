try:
    # Get age from user
    age_input = input("Enter your age: ")
    
    # Convert to integer
    age = int(age_input)
    
    # Validation 1: Check if age is negative
    if age < 0:
        raise ValueError("Age cannot be negative!")
    
    # Validation 2: Check if age is greater than 150
    if age > 150:
        raise ValueError("Age cannot be greater than 150!")
    
    # If all validations pass
    print(f"Age is valid: {age}")

except ValueError as e:
    # Catches both conversion error AND our custom raises
    print(f"Error: {e}")
    
except Exception as e:
    # Catches any other unexpected error
    print(f"Unexpected error: {e}")
