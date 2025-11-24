# Predict the output of this code:
x = [1, 2, 3]
y = x
y.append(4)
z = x.copy()
z.append(5)

print("x:", x)
print("y:", y)
print("z:", z)

a = (1, 2, 3)
b = a
b = b + (4,)
print("a:", a)
print("b:", b)

"""
Ans:
x: [1, 2, 3, 4]
y: [1, 2, 3, 4]
z: [1, 2, 3, 4, 5]
a: (1, 2, 3)
b: (1, 2, 3, 4)

Here why is a pointer Which directly point To the address of x where the list is stored That's Why Appending any element In y
Is also reflecting on x In the same way Z is Creating A list which pointing to the same address of the least Pointing to x That's Why appending any element
In z also reflects In X

Same process is going on for a and b But it is Tuple
"""
