""" While Loop """
# Syntax
# while condition:
#     code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1

# Output: 0 1 2 3 4

# Syntax
# while condition:
#     code goes here
# else:
#     code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Output: 0 1 2 3 4 5

# Break and Continue - Part 1
# Break: It is used when we like to get out or stop the loop.
# Continue: It is used to skip the current iteration, and continue with the next one.

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Output: 0 1 2

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# Output: 0 1 2 4

""" For Loop """
# Syntax
# for element in list:
#     code goes here

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)             # Output: 0 1 2 3 4 5

language = "Python"
for letter in language:
    print(letter)             # Output: P y t h o n

for i in range(len(language)):
    print(language[i])        # Output: P y t h o n

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)             # Output: 0 1 2 3 4 5

person = {
    "first_name": "Alexander",
    "last_name": "Caicedo",
    "age": 31,
    "country": "Colombia",
    "is_married": "No",
    "skills": ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    "address": {
        "street": "Cll 70",
        "zipcode": 410001
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)              # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company)

# Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# Output: 0 1 2 3

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print("Loop's end")
    # for short hand conditions need both if and else statements
print("Outside of the loop")

# Nested For Loops
# Syntax
# for x in y:
#     for w in z:
#         code goes here

person = {
    "first_name": "Alexander",
    "last_name": "Caicedo",
    "age": 31,
    "country": "Colombia",
    "is_married": True,
    "skills": ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    "address": {
        "street": "Cll 70",
        "zipcode": 410001
    }
}

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

# For Else
# Syntax
# for element in range(start, stop, step):
#     code goes here
# else:
#     code goes here

for number in range(11):
    print(number)
else:
    print("The loop stops at", number)

# Pass: It is used to avoid erros by not writing any code after the ':'
# for element in iterator:
#     pass

for number in range(11):
    pass