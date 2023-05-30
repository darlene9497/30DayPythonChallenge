# Exercises: Day 11
# Exercises: Level 1
#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(10,18)) #28

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = 3.14 * r * r
    return area
print(area_of_circle(20)) #1256.0

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "Invalid input. All arguments must be numbers."
print(add_all_nums(1, 2, 3))  #6
print(add_all_nums(1, 2, "3"))  #Invalid input. All arguments must be numbers.
print(add_all_nums(1, 2, 3.5, 4.2))  #10.7

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temperature_celsius = 25
temperature_fahrenheit = convert_celsius_to_fahrenheit(temperature_celsius)
print(f"The temperature {temperature_celsius}°C is equivalent to {temperature_fahrenheit}°F.") #The temperature 25°C is equivalent to 77°F.

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"
    elif month in (12, 1, 2):
        return "Winter"
    else:
        return "Invalid month"
month = 7
season = check_season(month)
print(f"The season for month {month} is {season}.") #The season for month 7 is Summer.

#6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath
def solve_quadratic_eqn(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    sqrt_discriminant = cmath.sqrt(discriminant)

    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)

    return root1, root2

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for element in lst:
        print(element)

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

#10 