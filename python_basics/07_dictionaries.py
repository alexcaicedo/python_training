"""
A dictionary is a collection of unordered, modifiable(mutable),
paired (key: value) data type.
A value could be any data types:
- integer, string, boolean, list, tuple, set or dictionary.
"""

# Syntax
empty_dict = {}
dct = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3'
}

person = {
    'first_name': 'Alexander',
    'last_name': 'Caicedo',
    'age': 31,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['Eat', 'Sleep', 'Hangry', 'Tired'],
    'address': {
        'street': 'Cll. 70',
        'zipcode': 410001
    }
}
print(len(person)) # 7

# Accessing dictionary items
person = {
    'first_name': 'Alexander',
    'last_name': 'Caicedo',
    'age': 31,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['Eat', 'Sleep', 'Hangry', 'Tired'],
    'address': {
        'street': 'Cll. 70',
        'zipcode': 410001
    }
}
print(person['first_name']) # Alexader
print(person['country'])    # Colombia
print(person['skills'])     # ['Eat', 'Sleep', 'Hangry', 'Tired']
print(person['skills'][0])  # Eat
print(person['address']['street']) # Cll. 70
print(person['city'])       # Error

"""
Accessing an item by key name raises an error if the key does not exist.
To avoid this error first we have to check if a key exist or
we can use the get method.
The get method returns None, which is a NoneType object data type,
if the key does not exist.
"""
print(person.get('first_name')) # Alexader
print(person.get('country'))    # Colombia
print(person.get('skills'))     # ['Eat', 'Sleep', 'Hangry', 'Tired']
print(person.get('city'))       # None

# Adding items to a dictionary
person = {
    'first_name': 'Alexander',
    'last_name': 'Caicedo',
    'age': 31,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['Eat', 'Sleep', 'Hangry', 'Tired'],
    'address': {
        'street': 'Cll. 70',
        'zipcode': 410001
    }
}

person['job_title'] = 'Data Scientist'
person['skills'].append('Laugh')
print(person)

# Modifying items
person = {
    'first_name': 'Alexander',
    'last_name': 'Caicedo',
    'age': 31,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['Eat', 'Sleep', 'Hangry', 'Tired'],
    'address': {
        'street': 'Cll. 70',
        'zipcode': 410001
    }
}

person['first_name'] = 'Alex'
person['age'] = 32

# Checking keys in dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing key and value pairs from a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()   # removes the last item
del dct['key2'] # removes key2 item

person = {
    'first_name': 'Alexander',
    'last_name': 'Caicedo',
    'age': 31,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['Eat', 'Sleep', 'Hangry', 'Tired'],
    'address': {
        'street': 'Cll. 70',
        'zipcode': 410001
    }
}

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

# Changing dictionary to a list of items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())   # Changes dictionary to a list of tuples - dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# Deleting a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copying a dictionary
# Copying a dictionary can avoid mutation of the original dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Getting dictinary values as a list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])