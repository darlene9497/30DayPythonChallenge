#  Exercises: Day 8
#1 Create an empty dictionary called dog
dog = {} 

#2 Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Baileys',
    'color': 'white',
    'legs': 4,
    'age': 3.5
}
print(dog) #{'name': 'Baileys', 'color': 'white', 'legs': 4, 'age': 3.5}

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Darlene',
    'last_name': 'Nandabi',
    'gender': 'female',
    'age': 26,
    'is_married': False,
    'skills': ['HTML', 'CSS', 'JS', 'React'],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': 1234
}

#4 Get the length of the student dictionary
print(len(student)) #9

#5 Get the value of skills and check the data type, it should be a list
skills = ['HTML', 'CSS', 'JS', 'React']
print(skills) #['HTML', 'CSS', 'JS', 'React']
print(type(skills)) #<class 'list'>

#6 Modify the skills values by adding one or two skills
skills.append('Python')
skills.append('Ruby')
print(skills) #['HTML', 'CSS', 'JS', 'React', 'Python', 'Ruby']

#7 Get the dictionary keys as a list
dct_keys = student.keys()
print(dct_keys) #dict_keys(['first_name', 'last_name', 'gender', 'age', 'is_married', 'skills', 'country', 'city', 'address'])

#8 Get the dictionary values as a list
dct_values = student.values()
print(dct_values) #dict_values(['Darlene', 'Nandabi', 'female', 26, False, ['HTML', 'CSS', 'JS', 'React'], 'Kenya', 'Nairobi', 1234])

#9 Change the dictionary to a list of tuples using items() method
student.items()
print(student) #{'first_name': 'Darlene', 'last_name': 'Nandabi', 'gender': 'female', 'age': 26, 'is_married': False, 'skills': ['HTML', 'CSS', 'JS', 'React'], 'country': 'Kenya', 'city': 'Nairobi', 'address': 1234}

#10 Delete one of the items in the dictionary
student.pop('last_name')
print(student) #{'first_name': 'Darlene', 'gender': 'female', 'age': 26, 'is_married': False, 'skills': ['HTML', 'CSS', 'JS', 'React'], 'country': 'Kenya', 'city': 'Nairobi', 'address': 1234}

#11 Delete one of the dictionaries
del student