"""
HIGH ORDER FUNCTIONS:
In Python, functions are treated as first class citizens, allowing you to perform the following operations on functions:
- A function can take one or more function as parameters.
- A function can be returned as a result of another function.
- A function can be modified.
- A function can be assigned to a variable.
"""
# Function as a Paramater
def sum_numbers(nums):   # Normal function
    return sum(nums)     # A sad function abusing the built-in sum function :<

def high_order_function(f, lst):     # Function as a parameter
    summation = f(lst)
    return summation

result = high_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)    # 15

# Function as a Return Value
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def hof(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = hof("square")
print(result(3))
result = hof("cube")
print(result(3))
result = hof("absolute")
print(result(-3))

### Python Closures
"""
Python allows a nested function to access the outer scope of the enclosing function.
This is known as Closure. Let us have alook at how closures work in Python.
In Python, a Closure is created by nesting a function inside another encapsulating function
and then returning the inner function. See the example below:
"""
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))    # 15
print(closure_result(10))   # 20