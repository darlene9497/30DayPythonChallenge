# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
#1 Find the length of the set it_companies
print(len(it_companies)) #7

#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies) #{'Twitter', 'Oracle', 'Facebook', 'IBM', 'Amazon', 'Apple', 'Google', 'Microsoft'}

#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Instagram', 'Accenture', 'DXC'])
print(it_companies) #{'Microsoft', 'IBM', 'Google', 'DXC', 'Facebook', 'Oracle', 'Instagram', 'Amazon', 'Accenture', 'Twitter', 'Apple'}

#4 Remove one of the companies from the set it_companies
it_companies.remove('Instagram')
print(it_companies) #{'Facebook', 'IBM', 'Microsoft', 'DXC', 'Amazon', 'Twitter', 'Google', 'Apple', 'Accenture', 'Oracle'}

#5 What is the difference between remove and discard
print('The remove() method will raise an error if the specified item does not exist, and the discard() method will not.')

# Exercises: Level 2
#1 Join A and B
print(A.union(B)) #{19, 20, 22, 24, 25, 26, 27, 28}

#2 Find A intersection B
print(A.intersection(B)) #{19, 20, 22, 24, 25, 26}

#3 Is A subset of B
print(A.issubset(B)) #True

#4 Are A and B disjoint sets
print(A.isdisjoint(B)) #False

#5 Join A with B and B with A
print(A.union(B)) #{19, 20, 22, 24, 25, 26, 27, 28}
print(B.union(A)) #{19, 20, 22, 24, 25, 26, 27, 28}

#6 What is the symmetric difference between A and B
print(A.symmetric_difference(B)) #{27, 28}

#7 Delete the sets completely
del A
del B

# Exercises: Level 3
#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_to_set = set(age)
print(ages_to_set) #{19, 22, 24, 25, 26}
print(len(age)) #8
print(len(ages_to_set)) #5
print('The list of ages is bigger than the set of ages')

#2 Explain the difference between the following data types: string, list, tuple and set
print('String - a word enclosed in either double, single or triple quotes')
print('List - collection of different data types enclosed in square brackets []' )
print('Tuple - collection of different data types that are immutable or unchangeable and enclosed in round brackets ()')
print('Set - a collection of items enclosed in curly braces {}')

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
# Split the sentence into individual words
words = sentence.split()
# Create a set to store unique words
unique_words = set(words)
# Get the count of unique words
num_unique_words = len(unique_words)
print(num_unique_words) #10