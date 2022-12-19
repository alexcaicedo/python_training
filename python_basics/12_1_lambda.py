"""
A Lambda function is a small anonymous function without a name.
It can take any number of arguments, but can only have one expression.
A Lambda function is similar to anonymous functions in JS.
We need it when we want to write anonymous function inside another function.
"""
# Syntax
# To create a lambda function we use lambda keyword followed by a parameter(s),
# followed by an expression. A Lambda function doesn't use return keyword but explicitly returns the expression.
# x = lambda param1, param2, param3: param1 + param2 + param3
# Invoking the function:
# x(arg1, arg2, arg3))

add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))                   # 5

# Self-invoking lambda function
print((lambda a, b: a + b)(4, 3))           # 7

square = lambda x: x ** 2
print(square(3))                            # 9
cube = lambda x: x ** 3
print(cube(3))                              # 27

# Multiple variables
multiple_variables = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variables(5, 5, 3))          # 22

# Lambda function inside another function
def power(x):
    return lambda n: x ** n

cube = power(2)(3)
# The function now needs 2 args to run, in separate parentheses

print(cube)                                 # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)                    # 32