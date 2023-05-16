# Variables in Python
first_name = 'Darlene'
last_name = 'Nandabi'
country = 'Kenya'
city = 'Nairobi'
age = 26
is_rich = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Darlene',
   'lastname':'Nandabi',
   'country':'Kenya',
   'city':'Nairobi'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_rich)
print('Skills: ', skills)
print('Person information: ', person_info)

# Multiple variables can also be declared in one line:
first_name, last_name, country, age, is_rich = 'Darlene', 'Nandabi', 'Kenya', 26, True

print(first_name, last_name, country, age, is_rich)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Rich: ', is_rich)

# Getting user input using the input() built-in function.
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)