# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

try:
    # Get index from user
    index_input = input("Enter index (0-4): ")
    index = int(index_input)
    
    # Get the number at that index
    number = numbers[index]
    
    # Get divisor from user
    divisor_input = input("Enter divisor: ")
    divisor = int(divisor_input)
    
    # Divide the number by divisor
    result = number / divisor
    
except IndexError:
    # This runs if index is out of range
    print(f"Error: Index out of range! List has only {len(numbers)} elements (0-{len(numbers)-1})")
    
except ZeroDivisionError:
    # This runs if user enters 0 as divisor
    print("Error: Cannot divide by zero!")
    
except ValueError:
    # This runs if user enters non-integer input
    print("Error: Please enter valid integers only!")
    
except Exception as e:
    # Generic handler for any other unexpected errors
    print(f"Unexpected error occurred: {e}")
    
else:
    # This runs ONLY if no exception occurred
    print(f"Result: {number} / {divisor} = {result}")
