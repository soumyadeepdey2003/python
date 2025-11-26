try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except Exception as e:
    print(f"Error occurred: {e}")
else:
    print(result)