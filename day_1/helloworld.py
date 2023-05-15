# Exercise: Level 2
# Question 1 
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# Question 2
print('Darlene')
print('Nandabi')
print('Kenya')
print('I am enjoying 30 days of python')

# Question 3
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Darlene', 'Python', 'Kenya']))
print(type('Darlene'))
print(type('Nandabi'))
print(type('Kenya'))

# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Number
print(-2, -1, 0, 1, 2) #integer
print(-1.0, -0.75, 0.0, 1.0, 1.75) #float/decimal numbers
print(2-2j, 3-6j) #complex 
#String
print('My name is Darlene and I will be a big name in tech')
#Boolean
print(True)
print(False) #T&&F should be in uppercase
#List
print(['Darlene', 199, True, 'incredible', 3.14, 1-1j]) #array in JS
#Tuple
print(('Mercury', 'Venus', 'Earth')) #cannot be modified
#Set
print({18, 7, 14})
print({3.14, 6.9, 5.32}) #order is not important
#Dictionary
print({
    'name':'Darlene',
    'age':20, #something
    'big_name':True,
    'pi':3.14
})

# Find an Euclidian distance between (2, 3) and (10, 8)
print('Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)',
      'Distance = sqrt((10 - 2)^2 + (8 - 3)^2)',
      '= sqrt(8^2 + 5^2)',
      '= sqrt(64 + 25)',
      '= sqrt(89)',
      'Ans = 9.43'
)