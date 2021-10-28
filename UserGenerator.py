import random
from password_generator import PasswordGenerator
import json

# seed random for deterministic results
random.seed(100)

# load firstnames and lastnames into lists
first_names = []
with open("firstnames.txt", "r") as fnames:
    for line in fnames.readlines():
        first_names = first_names.append(line.split(","))

last_names = []
with open("lastnames.txt", "r") as lnames:
    for line in lnames.readlines():
        last_names = last_names.append(line.split(","))


def f_name():
    return first_names[random.randint(0, 999)]


def l_name():
    return last_names[random.randint(0, 999)]


# get random phone number
# parameter n allows for country codes to be added, though default will be 10 digits
def rand_phone(n = 10):
    range_min = 10**(n-1)
    range_max = (10**n) -1
    return random.sample(range(range_min, range_max))


def rand_dob():
    year = random.randint(0, 120) + 1901
    month = random.randint(1, 12)
    day = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 30)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                day = random.randint(1,29)
        else:
            day = random.randint(1, 29)
    else: day = random.randint(1, 28)
    return [year, month, day]


def gen_pass():
    pwo = PasswordGenerator()
    # defaults include 1 digit, 1 uppercase letter, 1 lowercase letter, and 1 symbol
    # total length of 6-16 degits by default
    return pwo.generate()

num_users = int(input("Enter the number of users to be generated: "))
user = ""
for num in range(num_users):