# Day 4 strings
#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
challenge = ['Thirty', 'Days', 'Of', 'Python']
single_string = ' '.join(challenge)
print(single_string) #Thirty Days Of Python

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
challenge = ['Coding', 'For', 'All']
single_string = ' '.join(challenge)
print(single_string) #Coding For All

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4 Print the variable company using print().
print(company) #Coding For All

#5 Print the length of the company string using len() method and print().
print(len(company)) #14

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper()) #CODING FOR ALL

#7 Change all the characters to lowercase letters using lower() method.
print(company.lower()) #coding for all

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string_value = 'Coding For All'
print(string_value.capitalize()) #Coding for all
print(string_value.title()) #Coding For All
print(string_value.swapcase()) #cODING fOR aLL

#9 Cut(slice) out the first word of Coding For All string.
string = "Coding For All"
words = string.split()
cut_string = ' '.join(words[1:])
print(cut_string)  #For All

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
string = "Coding For All"
print(string.find('Coding')) #0
print(string.index('Coding')) #0

#11 Replace the word coding in the string 'Coding For All' to Python.
string = "Coding For All"
replace_string = string.replace('Coding', 'Python')
print(replace_string) #Python For All

#12 Change Python for Everyone to Python for All using the replace method or other methods.
string = 'Python for Everyone'
print(string.replace('Everyone', 'All')) #Python for All

#13 Split the string 'Coding For All' using space as the separator (split()) .
string = "Coding For All"
print(string.split()) #['Coding', 'For', 'All']

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
brand = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(brand.split(", "))

#15 What is the character at index 0 in the string Coding For All.
string = "Coding For All"
character_at_index_0 = string[0]
print(character_at_index_0) #C

#16 What is the last index of the string Coding For All.
string = "Coding For All"
character_at_last_index = string[-1]
print(character_at_last_index) #l

#17 What character is at index 10 in "Coding For All" string.
string = "Coding For All"
tenth_index = string[10]
print(tenth_index) #

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python For Everyone'
acronym = ''.join(word[0] for word in string.split())
print(acronym) #PFE

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
string = 'Coding For All'
acronym = ''.join(word[0] for word in string.split())
print(acronym) #CFA

#20 Use index to determine the position of the first occurrence of C in Coding For All.
string = 'Coding For All'
print(string.index('C')) #0

#21 Use index to determine the position of the first occurrence of F in Coding For All.
string = 'Coding For All'
print(string.index('F')) #7

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding For All People'
print(string.rindex('l')) #19

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because')) #31
print(string.index('because')) #31

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.rindex('because')) #47

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string[31:55]) #because because because

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because')) #31

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string[31:55]) #because because because

#28 Does ''Coding For All' start with a substring Coding?
string = 'Coding for all'
print(string.startswith('Coding')) #True

#29 Does 'Coding For All' end with a substring coding?
string = 'Coding for all'
print(string.endswith('coding'))  #False

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      ' 
print(string.strip(' ')) #Coding For All

#31 Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
string = '30DaysOfPython'
print(string.isidentifier()) #False
#thirty_days_of_python
string= 'thirty_days_of_python'
print(string.isidentifier()) #True

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = '# '.join(libraries)
print(joined_string) #Django# Flask# Bottle# Pyramid# Falcon

#33 Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')

#34 Use a tab escape sequence to write the following lines
# Name      Age     Country   City
# Darlene   26      Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Darlene\t26\tKenya\tNairobi')

#35 Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
string = 'The area of a circle with radius {} is {:.2f} meters square.'.format(radius, area) #The area of a circle with radius 10 is 314.00 meters square.
print(string)

#36 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print('{} + {} = {}'.format(a,b, a+b))
print('{} - {} = {}'.format(a,b, a-b))
print('{} * {} = {}'.format(a,b, a*b))
print('{} / {:.2f} = {}'.format(a,b, a/b))
print('{} % {} = {}'.format(a,b, a%b))
print('{} // {} = {}'.format(a,b, a//b))
print('{} ** {} = {}'.format(a,b, a**b))