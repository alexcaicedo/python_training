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
