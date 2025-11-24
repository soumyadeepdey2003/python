"""
Given a list of numbers: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Write code that:

Using map() and lambda: Create a new list where each number is squared.

Using filter() and lambda: Create a list of only even numbers.

Using map() and lambda: Convert each number to a string and append "!" to it (e.g., "1!", "2!", etc.).

Combine map() and filter(): Filter numbers > 4, then square them.

Using sorted() with lambda key: Sort the original list in descending order (you can also sort a list of dictionaries with custom logic).

"""

# ans

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

result = list(map(lambda x: x ** 2, filter(lambda x: x > 4, numbers)))
print(result)

# Here Lambda X: - X Denotes Printing from the Ending to starting Where sorting function sort it in Ascending order
descending = sorted(numbers, key=lambda x: -x)
print(descending)

# Sorted function Sort Add a in ascending order But reverse true Make it reverse
descending2 = sorted(numbers, reverse=True)
print(descending2)