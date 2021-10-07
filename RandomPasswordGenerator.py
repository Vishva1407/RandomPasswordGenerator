# importing random module
import random

# funtion to create random password
def random_password_generator(length,possibilities):
    password = ""
    for i in range(length):
        possible = random.choice(possibilities)
        if possible == alphabets:
            password = password + random.choice(alphabets)
        elif possible == numbers:
            password = password + random.choice(numbers)
        else:
            password = password + random.choice(special_characters) 
    return password

alphabets = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numbers = "1234567890"
special_characters = "!@#$%^&*()_+<>/?-,.\|"
# Length of the password
length = 16
possibilities = [alphabets,numbers,special_characters]
#calling the random_password_generator funtion
randomPassword = random_password_generator(length,possibilities)
#printing the result
print(randomPassword)