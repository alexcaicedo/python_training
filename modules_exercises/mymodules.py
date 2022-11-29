import random as rd
import string

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return "Full Name: " + full_name

def add_two_numbers(num1, num2):
    return num1 + num2

def weight(mass, g=9.81):
    return str(mass * g) + " N"

def random_user_id():
    """
    Function that generates a six-digit/characters random user id
    Args:
        None
    Returns:
        user_id. Type String object.
    """
    letters = string.ascii_letters
    numbers = string.digits
    characters = letters + numbers
    
    count = 1
    user_id = str()
    while count <= 6:
        char = rd.choice(characters)
        user_id += char
        count += 1
    return user_id

def user_id_gen_by_user():
    """
    Function that takes two inputs:
    - Number of characters.
    - Number of ID's to create.
    And creates the specified number of randomly generated user ID's with a specified number of characters.

    Args:
        None
    Returns:
        Prints out one by one the characters of the users ID's.

    """
    letters = string.ascii_letters
    numbers = string.digits
    characters = letters + numbers
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of ID's: "))

    for id in range(1, num_ids + 1):
        count = 1
        user_id = str()
        while count <= num_chars:
            char = rd.choice(characters)
            user_id += char
            count += 1
        print("User {}: {}".format(id, user_id))

def rgb_color_gen():
    """
    Function that generates rgb colors with 3 values ranging from 0 to 255.
    Args:
        None
    Returns:

    """
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    rgb = (r, g, b)
    rgb = str(rgb)
    return "rgb" + rgb