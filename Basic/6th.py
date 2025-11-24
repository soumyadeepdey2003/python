"""
Write a Python function called calculate_stats() that:

Accepts any number of numbers as arguments (*args)

Has an optional parameter: operation='sum' (can be 'sum', 'avg', 'product', 'max', 'min')

Returns the correct result for the given operation

Prints an error and returns None if no numbers are provided

"""
# ans:
def calculate_stats(*args, operation='sum'):
    if not args:
        print("Error: No numbers provided.")
        return None

    if operation == 'sum':
        return sum(args)
    elif operation == 'avg':
        return sum(args) / len(args)
    elif operation == 'product':
        prod = 1
        for num in args:
            prod *= num
        return prod
    elif operation == 'max':
        return max(args)
    elif operation == 'min':
        return min(args)
    else:
        print("Error: Unknown operation.")
        return None


print(calculate_stats(5, 10, 15))                       
print(calculate_stats(5, 10, 15, operation='avg'))       
print(calculate_stats(2, 3, 4, operation='product'))     
print(calculate_stats(8, 3, 12, operation='max'))        
print(calculate_stats())                                 
