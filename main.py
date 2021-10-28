import names

with open("lastnames.txt", "w") as lnames:
    for i in range(1000):
        lnames.write(names.get_last_name())

with open("firstnames.txt", "w") as fnames:
    for i in range(500):
        fnames.write(names.get_first_name(gender="female"))
    for i in range(500):
        fnames.write(names.get_first_name(gender="male"))

