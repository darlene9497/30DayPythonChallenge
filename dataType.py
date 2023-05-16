# Different python data types
# Let's declare variables with various data types

# first_name = 'Darlene'     # str
# last_name = 'Nandabi'       # str
# country = 'Kenya'         # str
# city= 'Naitobi'            # str
# age = 26                   # int

# # Printing out types
# print(type('Asabeneh'))     # str
# print(type(first_name))     # str
# print(type(10))             # int
# print(type(3.14))           # float
# print(type(1 + 1j))         # complex
# print(type(True))           # bool
# print(type([1, 2, 3, 4]))     # list
# print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
# print(type((1,2)))          # tuple
# print(type(zip([1,2],[3,4])))      # set

# Casting: Converting one data type to another data type
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
# print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Darlene'
print(first_name)               # 'Darlene'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['D', 'a', 'r', 'l', 'e', 'n', 'e']