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

# Excersises Level 1

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

# Excersises Level 2

def list_of_hexa_colors(n):
    """
    Function to create an array of randomly generated hexadecimal colors.
    
    Args:
        n = Number of elements in array -> Int type object.
    Returns:
        colors_array = List of hexa colors -> List type object.
    """
    characters = "0123456789abcdef"
    colors_array = []
    while n > 0:
        count = 1
        user_id = "#"
        while count <= 6:
            char = rd.choice(characters)
            user_id += char
            count += 1
        colors_array.append(user_id)
        n -= 1
    return colors_array

def list_of_rgb_colors(n):
    """
    Function to create an array of randomly generated RGB colors.
    
    Args:
        n = Number of elements in array -> Int type object.
    Returns:
        colors_array = List of RGB colors -> List type object.
    """
    colors_array = []
    while n > 0:
        colors_array.append(rgb_color_gen())
        n -= 1
    return colors_array

def generate_colors(color_type, n):
    if color_type == "hexa":
        return list_of_hexa_colors(n)
    else:
        return list_of_rgb_colors(n)

# Excersises Level 3

def shuffle_list(l):
    """
    Function to shuffle a list.

    Args:
        l = Input list -> List type object.
    Returns:
        result = Shuffled list -> List type object.
    """
    result = rd.sample(l, len(l))
    return result

def random_numbers_list():
    """
    Function which returns an array of seven unique random numbers in a range of 0-9.

    Args:
        None
    Returns:
        num_list = List of 7 unique random numbers -> List type object.
    """
    set_1 = {rd.choice(range(0, 10))}
    while len(set_1) < 7:
        set_2 = {rd.choice(range(0, 10))}
        set_1.update(set_2)
    num_list = list(set_1)
    return rd.sample(num_list, len(num_list))