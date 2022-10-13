"""
Sets are one of four collection data types in python.
The other three are: Lists, Tuples and Dictionaries.
The Mathematics definition of a set can be applied also in Python. 
Set is a collection of unordered and unindexed distinct elements.
In Python set is used to store unique items, and it is possible to find:
- union
- intersection
- difference
- symmetric difference
- subset
- super set
- and disjoint set among sets.
"""

# How to create a set
# Using built in function set()
empty_tpl = set()

# Using curly brackets {}
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

set_length = len(fruits)  # built in function len() gives the number of elements in a set.
print(set_length)

# Accessing items in sets
"""
We use loops to access items. These are covered in the loop files.
"""

# Checking an item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# Adding items
# Add one item using .add()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)    # {'banana', 'orange', 'mango', 'lemon', 'lime'}

# Add multiple items using .update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)    # {'carrot', 'mango', 'tomato', 'cabbage', 'potato', 'onion', 'banana', 'orange', 'lemon'}

# Removing items
"""
We can remove an item from a set using .remove() method.
If the item is not found .remove() method will raise errors,
so it is good to check if the item exist in the given set.
However, .discard() method doesn't raise any errors.
"""
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# Clearing items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# Deleting a set
st = {'item1', 'item2', 'item3'}
del st

# Converting sets into lists
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# Joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)     # {'item2', 'item1', 'item6', 'item5', 'item3', 'item7', 'item8', 'item4'} - random order

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Finding intersection items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

# Checking subset and superset
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# Checking the difference between two sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

# Checking the symmetric difference between two sets
"""
It returns the the symmetric difference between two sets.
It means that it returns a set that contains all items from both sets,
except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
"""
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# Checking disjoint sets
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common items

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

