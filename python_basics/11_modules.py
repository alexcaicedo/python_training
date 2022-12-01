"""
A module is a file containing a set of functions which can be included to an application.
A module could be a file containing a single variable, a function or a big source code.
"""
# Importing Modules and renaming
# from mymodules import generate_full_name as gfn, add_two_numbers as add
# from mymodules import weight

# print(gfn("Alexander", "Caicedo"))   # Full Name: Alexander Caicedo
# print(add(2, 3))                     # 5
# print(weight(100))                   # 981.0 N
# print(weight(100, g=1.62))           # 162.0 N (Moon's gravity)

# Importing Built-in modules
"""
Like other programming languages we can also import modules by importing the file/function using the key word import.
Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os, sys, random,
statistics, collections, json, re.
"""
# OS Module
# import os
# os.mkdir("directory_name")    # Creating a directory
# os.chdir("path")              # Changing to the specified path directory
# os.getcwd()                   # Getting current working directory 
# os.rmdir()                    # Removing directory

# Sys Module
# import sys
# print("Welcome {}. Enjoy {} challenge!".format(sys.argv[1], sys.argv[2])) # Run in the terminal: Python3 main.py Alex 30_days
# Output: Welcome Alex. Enjoy 30_days challenge!

# Statistics Module
# from statistics import * # Imports all statistics modules
# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))    # ~21.09090909090909
# print(median(ages))  # 22
# print(mode(ages))    # 20
# print(stdev(ages))   # ~6.106628291529549

# Math Module
# import math
# print(math.pi)           # 3.141592653589793 - pi constant
# print(math.sqrt(2))      # 1.4142135623730951 - square root
# print(math.pow(2, 3))    # 8.0 - exponential function
# print(math.floor(9.81))  # 9 - round to the lowest
# print(math.ceil(9.81))   # 10 - round to the highest
# print(math.log10(100))   # 2.0 - logarithm with 10 as base

# It is also possible to import multiple functions at once
# from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)           # 3.141592653589793 - pi constant
# print(sqrt(2))      # 1.4142135623730951 - square root
# print(pow(2, 3))    # 8.0 - exponential function
# print(floor(9.81))  # 9 - round to the lowest
# print(ceil(9.81))   # 10 - round to the highest
# print(log10(100))   # 2.0 - logarithm with 10 as base

# String Module
# import string
# print(string.ascii_letters)     # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)            # 0123456789
# print(string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.__name__)          # string
# print(string.octdigits)         # 01234567
# print(string.hexdigits)         # 0123456789abcdefABCDEF

# Random Module
# from random import random, randint
# print(random())        # It doesn't take any arguments. It returns a value between 0 and 0.9999
# print(randint(5, 20))  # It returns a random integer between [5, 20] inclusive

