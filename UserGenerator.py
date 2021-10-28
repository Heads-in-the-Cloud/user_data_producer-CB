import random
from easy_password_generator import PassGen
import json

# seed random for deterministic results
random.seed(100)

# load firstnames and lastnames into lists
first_names = []
with open("firstnames.txt", "r") as fnames:
    for line in fnames.readlines():
        first_names.extend(line.split(","))

last_names = []
with open("lastnames.txt", "r") as lnames:
    for line in lnames.readlines():
        last_names.extend(line.split(","))


def f_name():
    return first_names[random.randint(0, 999)]


def l_name():
    return last_names[random.randint(0, 999)]


# get random phone number
# parameter n allows for country codes to be added, though default will be 10 digits
def rand_phone(n =10):
    range_min = 10**(n-1)
    range_max = (10**n) -1
    return random.randint(range_min, range_max)


def get_email(uname):
    domain = random.randint(1, 4)
    if domain == 1:
        domain = "@gmail.com"
    elif domain == 2:
        domain = "@yahoo.com"
    elif domain == 3:
        domain = "@protonmail.com"
    elif domain == 4:
        domain = "@mail.com"
    return uname + domain

# included for possible future use of generating passengers
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


def get_role():
    r_id = random.randint(1,4)
    r_name = ""
    if r_id == 1:
        r_name = "ROLE_USER"
    elif r_id == 2:
        r_name = "ROLE_AGENT"
    elif r_id == 3:
        r_name = "ROLE_GUEST"
    elif r_id == 4:
        r_name = "ROLE_ADMIN"
    return [r_id, r_name]


def gen_pass():
    pwo = PassGen()
    # defaults include 1 digit, 1 uppercase letter, 1 lowercase letter, and 1 symbol
    # total length of 6-16 digits by default
    return pwo.generate()

num_users = int(input("Enter the number of users to be generated: "))
user = ""
for num in range(num_users):
    role = get_role()
    fname = f_name()
    lname = l_name()
    username = fname[0:4] + "." + lname
    email = get_email(username)
    password = gen_pass()
    phone = rand_phone()

    user = '{"id":0, "role_id":' + str(role[0]) + ', "given_name":"' + fname + '", "family_name":"' + lname +\
           '", "username":"' + username + '", "email":"' + email + '", "password":"' + password +\
           '", "phone":"' + str(phone) + '", "roles":"' + role[1] + '"}'
    json_user = json.loads(user)
    print(json_user)

    # create POST request