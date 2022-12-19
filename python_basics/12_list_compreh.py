"""
List comprehension in Python is a compact way of creating a list from a sequence.
It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.
"""
# Syntax
# [i for i in iterable if expression]

language = "Python"
lst = list(language)
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(11)]
print(numbers)

# It is possible to do math operations during iteration
squares = [i * i for i in range(11)]
print(squares)       # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)       # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# List comprehension can be combined with if expression
## Even numbers
even_nums = [i for i in range(21) if i % 2 == 0]
print(even_nums)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

## Odd numbers
odd_nums = [i for i in range(21) if i % 2 != 0]
print(odd_nums)     # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

## Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

## Flattening a 3-D array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in list_of_lists for number in row]
print(flat_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

