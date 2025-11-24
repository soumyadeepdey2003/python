
"""
Write a Python program that:
Separates them into two lists: one for even numbers and one for odd numbers
Displays both lists
Shows the sum of even numbers and sum of odd numbers
"""

# ans:


n = int(input("Please enter a limit: "))
numbers = []

for i in range(n):
    numbers.append(int(input("Please enter a number: ")))
print(numbers)
odd=[]
oddsum=0
even=[]
evensum=0
for i in numbers:
    if(i%2==0):
        even.append(i)
        evensum=evensum+i
    else:
        odd.append(i)
        oddsum=oddsum+i

print("odd numbers:",odd)
print("sum of all odd numbers:",oddsum)
print("even numbers:",even)
print("sum of all even numbers:",evensum)

