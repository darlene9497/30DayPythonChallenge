# Exercises - Day 3
#1 Declare your age as integer variable
age = 26
print(age)

#2 Declare your height as a float variable
height = 1.6256
print(height)

#3 Declare a variable that store a complex number
x = 2-3j
print(x)

#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter base: '))      #The float() function is used to convert the user input into a floating-point number.
height = float(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is ', area)

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is ', perimeter)

#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area = length * width
print('The area of the rectangle is ', area)
perimeter = 2 * (length + width)
print('The perimeter of the rectangle is ', perimeter)

#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input('Enter the radius of the circle: '))
pi = 3.14
area = pi * r * r
print('The area of the circle is ', area)
circumference = 2 * pi * r
print('The circumference of the circle is ', circumference)

#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Equation: y = 2x - 2
# Formula (y = mx + b) 
slope1 = 2       #Calculate slope (m)
y_intercept = -2      #Calculate y-intercept (b)
x_intercept = -y_intercept / slope1 #Calculate x-intercept by setting y = 0 and solving for x
print("Slope (m):", slope1)
print("Y-intercept (b):", y_intercept)
print("X-intercept:", x_intercept)


#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1, y1 = 2, 2  #Coordinates of point 1
x2, y2 = 6, 10  #Coordinates of point 2
slope2 = (y2 - y1) / (x2 - x1)  #Calculate the slope (m)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) #Calculate the Euclidean distance between the two points
print("Slope (m):", slope2)
print("Euclidean Distance:", distance)

#10 Compare the slopes in tasks 8 and 9.
print(slope1 == slope2)
print(slope1 != slope2)
print(slope1 > slope2)
print(slope1 < slope2)
print(slope1 >= slope2)
print(slope1 <= slope2)

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
import math
def calculate_y(x):
    return x**2 + 6*x + 9
x_values = [-10, -5, 0, 5, 10] #Calculate y for different x values
for x in x_values:
    y = calculate_y(x)
    print("For x =", x, ", y =", y)
a = 1 #Find x value when y is equal to 0 using the quadratic formula
b = 6
c = 9 
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The x values at which y is 0 are:", x1, "and", x2)
else:
    print("There are no real x values at which y is 0.")

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') > len('dragon'))   #False

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'dragon' and 'on' in 'python')

#14 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('jargon' in 'I hope this course is not full of jargon')

#15 There is no 'on' in both dragon and python
print(not 'on' in 'dragon' and not 'on' in 'python')

#16 Find the length of the text python and convert the value to float and convert it to string
length = float(len('python'))
length_str = str(length)
print(length_str)

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print('Using the modulo operator') #Answer
num = 10
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is not an even number.")

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = 7 // 3   #2
converted = int(2.7) #2
print(floor_div == converted) #True

#19 Check if type of '10' is equal to type of 10
# print('10' == 10) #False-'10'-str, 10-int
string = '10'
integer = 10
print(type(string) == type(integer)) #False-'10'-str, 10-int

#20 Check if int('9.8') is equal to 10
floating_point_value = 9.8
print(int(floating_point_value) == 10) #False

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hrs = int(input('Enter hours: '))
rate = int(input('Enter rate: '))
pay = hrs * rate
print('Your weekly earning is ', pay)

#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years you have lived: '))
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365
seconds_alive = years * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
print('You have lived for', seconds_alive, 'seconds')

#23 Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):  # Rows
    print(i, 1, i ** 2, i ** 3, i ** 4)