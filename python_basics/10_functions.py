"""
A function is a reusable block of code or programming statements designed to perform a certain task.
"""

# Syntax
# def function_name():
#     code goes here
# Calling the function
# function_name()

# Function without Parameters
def generate_full_name():
    first_name = "Alexander"
    last_name = "Caicedo"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()   # Output: Alexander Caicedo

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()     # Output: 5

# Function Returning a Value
# Function can also return values, if a function does not have a return statement, the value of the function is None.
def generate_full_name():
    first_name = "Alexander"
    last_name = "Caicedo"
    space = " "
    full_name = first_name + space + last_name
    return full_name

generate_full_name()         # Output:
print(generate_full_name())  # Output: Alexander Caicedo

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())   # Output: 5

# Function with Parameters
# In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter
# Syntax
# def function_name(parameter):
#     code goes here
# Calling the function
# print(function_name(argument))

def greetings(name):
    message = name + "!, welcome to this Python tutorial"
    return message

print(greetings("Alex"))
# Output: Alex!, welcome to this Python tutorial

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(90))
# Output: 100

def squared_number(x):
    return x * x

print(squared_number(3))
# Output: 9

def area_of_circle(r):
    PI = 3.1415
    area = PI * (r ** 2)
    return area

print("area of circle =", area_of_circle(5))
# Output: area of circle = 78.53750000000001

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(100))
# Output: 5050

# Two parameters:
# Syntax
# def function_name(p1, p2):
#     code goes here
# Calling the function
# print(function_name(arg1, arg2))

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Alexander','Caicedo'))
# Output: Full Name: Alexander Caicedo

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))
# Output: Sum of two numbers: 10

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2022, 1991))
# Output: Age: 31

def weight_of_object(mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons:', weight_of_object(100, 9.81))
# Output: Weight of an object in Newtons: 981.0 N

# Passing Arguments with Key and Value
# Declaring a function
# def function_name(p1, p2):
#     code goes here
# Calling the function
# print(function_name(p1=arg1, p2=arg2))    The order of arguments does not matter here

def generate_full_name(first_name, last_name):
    return first_name + " " + last_name
print(generate_full_name(first_name="Alexander", last_name="Caicedo"))
# Output: Alexander Caicedo

def sum_two_numbers(num_one, num_two):
    return num_one + num_two
print(sum_two_numbers(num_one=1, num_two=9))
# Output: 10

# Returning values
# String
def print_name(name):
    return name
print(print_name("Alexander")) # Alexander

# Number
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(2, 3)) # 5

# Bool
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(10)) # True
print(is_even(5)) # False

# List
def find_even_numbers(n):
    evens = []
    for i in range(n + 2):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10)) # [0, 2, 4, 6, 8, 10]

# Function with Default Parameters
# Declaring a function
# def function_name(param=value):
#     code goes here
# Calling function
# function_name()
# function_name(arg)

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

# Arbitrary Number of Arguments
# syntax
# Declaring a function
# def function_name(*args):
#     code goes here
# Calling function
# function_name(param1, param2, param3,..)

def sum_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(sum_all_nums(2, 3, 5)) # 10

def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Alex','Brook','David','Eyob'))
# Output: 
# Team-1
# Alex
# Brook
# David
# Eyob

# Function as a Parameter of Another Function - High Order Functions
def square_number(n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_number, 3)) # 9