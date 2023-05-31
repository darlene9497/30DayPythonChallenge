# Create main.py file in your project directory and import the mymodule.py file.

# Importing a Module
# To import the file we use the import keyword and the name of the file only.

# main.py file
import day_12.mymodule as mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

# Import Functions from a Module
# We can have many functions in a file and we can import all the functions differently.
# main.py file
from day_12.mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

# Import Functions from a Module and Renaming
# During importing we can rename the name of the module.
# main.py file
from day_12.mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])