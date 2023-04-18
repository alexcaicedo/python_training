## DECORATORS
# Decorators work as a way of adding extra functionality to functions and methods, without changing those original functions or methods.

# Function Decorators
# def decorator_function(original_func):
#     def wrapper_function(*args, **kwargs):
#         print(f"wrapper executed this before {original_func.__name__}")
#         return original_func(*args, **kwargs)
#     return wrapper_function

# Class Decorators
# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
    
#     def __call__(self, *args, **kwargs):
#         print(f"call method executed this before {self.original_function.__name__}")
#         return self.original_function(*args, **kwargs)

# Calling decorators
# @decorator_function
# def display():
#     print("display function ran")

# @decorator_function
# def display_info(name, age):
#     print(f"display_info ran with arguments ({name}, {age})")

# @decorator_class
# def display():
#     print("display function ran")

# @decorator_class
# def display_info(name, age):
#     print(f"display_info ran with arguments ({name}, {age})")

# Calling functions with extra functionality
# display()
# display_info("Alex", 32)

# decorated_display = decorator_function(display)  # This is the same as adding the "@" before the original function
# decorated_display()

# Example of decorators for logging
# def my_logger(original_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
#         )

#         return original_func(*args, **kwargs)
    
#     return wrapper

# Example of decorators for timing
# def my_timer(original_func):
#     import time

#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = original_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(original_func.__name__, t2))

#         return result
    
#     return wrapper

# Using one decorator
# @my_timer
# def display_info(name, age):
#     print(f"display_info ran with arguments ({name}, {age})")

# display_info("Alex", 31)

# Using several decorators at once
from functools import wraps

def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )

        return original_func(*args, **kwargs)
    
    return wrapper

def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_func.__name__, t2))

        return result
    
    return wrapper

@my_logger
@my_timer
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

print(display_info.__name__)

