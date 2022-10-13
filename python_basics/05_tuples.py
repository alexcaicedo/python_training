"""
Tuples are one of four collection data types in python.
The other three are: Lists, Sets and Dictionaries.
Tuples are ordered and unchangeable.
Once a tuple is created we cannot change its values.
We cannot use add, insert, remove methods in a tuple because it is not modifiable (unmutable).
Unlike list, tuple has few methods.
"""
# How to create a tuple
# Using built in function tuple()
empty_tpl = tuple()

# Using round brackets ()
empty_tpl = ()

tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

tuple_length = len(fruits)  # built in function len() gives the number of elements in a tuple.
print(tuple_length)

# Accessing tuple items
# Positive index
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

# Negative index
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# Slicing tuples
"""
Slicing works the same as in lists.
"""

# Changing tuples
# We can change tuples to lists and lists to tuples.
# Since tuples are immutable, if we want to modify a tuple we should change it to a list.
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Checking an item in a tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# Joining tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')

# Deleting tuples
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
tpl = ('item1', 'item2', 'item3')
del tpl
print(tpl) # NameError: name 'tpl' is not defined