# Variables in Python

firstname = "Alexander"
lastname = "Caicedo"
age = 31
height = 175
weight = 78.6
country = "Colombia"
city = "Neiva"
is_married = False
skills = ["Python", "Excel", "English", "Numpy", "Seaborn", "Pandas"]
person_info = {
    "firstname": firstname,
    "lastname": lastname,
    "age": age,
    "height": height,
    "weight": weight,
    "country": country,
    "city": city
}

# Printing the values stores in variables

print("First name:", firstname)
print("First name length:", len(firstname))            # len() is a Built-in function
print("Last name:", lastname)
print("Last name length:", len(lastname))
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Married:", is_married)
print("Skills:", skills)
print("Person information:", person_info)

# Declaring multiple variables in one line

x, y, z = 20, "Treinta", False

print(x)
print(y)
print(z)

# Getting user input

# first_name = input("What's your name?: ")
# age = input("What's your age?: ")

# print(first_name)
# print(age)

# Casting: Converting one data type into another

float_age = float(age)
print(float_age)

int_weight = int(weight)
print(int_weight)

firstname_to_list = list(firstname)
print(firstname_to_list)