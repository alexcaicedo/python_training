"""
By default, statements in Python script are executed sequentially from top to bottom.
If the processing logic require so, the sequential flow of execution can be altered in two way:
- Conditional execution: a block of one or more statements will be executed if a certain expression is true
- Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
"""

# If statement
# Syntax
# if condition:
#     this part of the code runs for thruthy conditions

a = 3
if a > 0:
    print("a is a positive number")   # a is a positive number

# If, else statements
# Syntax
# if condition:
#     this part of the code runs for TRUE conditions
# else:
#     this part of the code runs for FALSE conditions

a = 3
if a < 0:
    print("a is a negative number")
else:
    print("a is a positive number")  # a is a positive number

# If, elif, else statements
# Syntax
# if condition:
#     this part of the code runs for TRUE conditions
# elif condition:
#     this part of the code runs for TRUE conditions in the elif statement
#     as long as the if statement is FALSE
# else:
#     this part of the code runs for FALSE conditions on both of the last statements 

a = 0
if a > 0:
    print("a is a positive number")
elif a < 0:
    print("a is a negative number")
else:
    print("a is zero")

# Short Hand
a = 3
print("a is positive") if a > 0 else print("a is negative")  # first condition met, 'A is positive' will be printed

# Nested conditions
# if condition:
#     this part of the code runs for TRUE conditions
#     if condition:
#         this part of the code runs for TRUE conditions in the elif statement
a = 0
if a > 0:
    if a % 2 == 0:
        print("a is positive and even integer")
    else:
        print("a is a positive integer")
elif a == 0:
    print("a is zero")
else:
    print("a is a negative integer")

# If conditons and logical operators
# if condition or condition:
#     code
user = "Alex"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied :'(")
