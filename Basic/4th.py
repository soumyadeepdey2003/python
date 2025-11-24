"""
Given a tuple of numbers: numbers = (45, 23, 67, 89, 12, 34, 56, 78, 90, 11)
Write code that:
Extracts and prints every 2nd element (using slicing)
Extracts and prints the last 3 elements in reverse order
Counts how many times the digit "1" appears in ALL numbers combined (convert each number to string)
Unpacks the first 3 and last 3 elements into separate variables and print them

"""
# ans

numbers = (45, 23, 67, 89, 12, 34, 56, 78, 90, 11)
print(numbers[0:len(numbers):2])
print(numbers[:-4:-1])

c=0
for i in numbers:
    n=i
    while(n!=0):
            if(n%10==1):
                    c=c+1
            n=n//10

print(c)
a=numbers[0:3]
b=numbers[-3::]

print(a)
print(b)