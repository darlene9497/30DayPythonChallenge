# 'Day 2: 30 Days of python programming'

# Exercises: Level 1
#3 Declare a first name variable and assign a value to it
first_name = 'Darlene'
#4 Declare a last name variable and assign a value to it
last_name = 'Nandabi'
#5 Declare a full name variable and assign a value to it
full_name = 'Darlene Nandabi'
#6 Declare a country variable and assign a value to it
country = 'Kenya'
#7 Declare a city variable and assign a value to it
city = 'Nairobi'
#8 Declare an age variable and assign a value to it
age = 26
#9 Declare a year variable and assign a value to it
year = 1997
#10 Declare a variable is_married and assign a value to it
is_married = False
#11 Declare a variable is_true and assign a value to it
is_true = True
#12 Declare a variable is_light_on and assign a value to it
is_light_on = False
#13 Declare multiple variable on one line

name, grade, age, is_tall = 'Val', 11, 18, True

# Exercises: Level 2
#1 Check the data type of all your variables using type() built-in function
print(type(first_name)) #str
print(type(last_name))  #str
print(type(full_name))  #str
print(type(country))    #str
print(type(city))       #str
print(type(age))        #int
print(type(year))       #int
print(type(is_married)) #bool
print(type(is_true))    #bool
print(type(is_light_on))#bool
# Var question 13
print(type(name))      #str
print(type(grade))     #int
print(type(age))       #int
print(type(is_tall))   #bool

#2 Using the len() built-in function, find the length of your first name
print(len(first_name))

#3 Compare the length of your first name and your last name
first_name_length = len(first_name)
last_name_length = len(last_name)

if first_name_length > last_name_length:
    print("The length of the first name is greater than the length of the last name.")
elif first_name_length < last_name_length:
    print("The length of the first name is less than the length of the last name.")
else:
    print("The length of the first name is equal to the length of the last name.")

#4 Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#i. Add num_one and num_two and assign the value to a variable total
sum = num_one + num_two
print(sum) #9
#ii. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)#1
#iii. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product) #20
#iv. Divide num_one by num_two and assign the value to a variable division
div = num_one / num_two
print(div) #1.25
#v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
mod = num_two % num_one
print(mod) #4
#vi. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp) #625
#vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
div = num_one // num_two
print(div) #1

#5. The radius of a circle is 30 meters.
import math
radius = 30
#i. Calculate the area of a circle and assign the value to a variable name of 'area_of_circle'
area_of_circle = math.pi * radius ** 2
print("Area of the circle:", area_of_circle)      #2827.4333882308138
#ii. Calculate the circumference of a circle and assign the value to a variable name of 'circum_of_circle'
circum_of_circle = 2 * math.pi * radius
print("Circumference of the circle:", circum_of_circle)  #188.49555921538757
#iii. Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius ** 2
print("Area of the circle:", area_of_circle)

#6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
#Get user input
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
country = input('Enter your country:')
age = input('Enter your age:')
#Print the values
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)

#7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))