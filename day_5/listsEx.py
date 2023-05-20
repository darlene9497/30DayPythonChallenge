#  Exercises: Day 5
# Exercises: Level 1
#1 Declare an empty list
empty_list = []

#2 Declare a list with more than 5 items
lst = ['Nairobi', 'Kisumu', 'Mombasa', 'Nakuru', 'Eldoret']

#3 Find the length of your list
print(len(lst)) #5

#4 Get the first item, the middle item and the last item of the list
first_item = lst[0]
middle_item = lst[2]
last_item = lst[-1]
print(first_item) #Nairobi
print(middle_item) #Mombasa
print(last_item) #Eldoret

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Darlene', 26, 5.4, 'Single', 1234]

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print(it_companies) #['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#8 Print the number of companies in the list
print(len(it_companies)) #7

#9 Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]
print(first_company) #Facebook
print(middle_company) #Apple
print(last_company) #Amazon

#10 Print the list after modifying one of the companies
it_companies[0] = 'FB'
print(it_companies) #['FB', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#11 Add an IT company to it_companies
it_companies.append('LG')
print(it_companies) #['FB', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'LG']

#12 Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Samsung')
print(it_companies) #['FB', 'Google', 'Microsoft', 'Apple', 'Samsung', 'IBM', 'Oracle', 'Amazon', 'LG']

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies) #['FB', 'GOOGLE', 'Microsoft', 'Apple', 'Samsung', 'IBM', 'Oracle', 'Amazon', 'LG']

#14 Join the it_companies with a string '#;  '
joined_string = '#;  '.join(it_companies)
print(joined_string) #FB#;  GOOGLE#;  Microsoft#;  Apple#;  Samsung#;  IBM#;  Oracle#;  Amazon#;  LG

#15 Check if a certain company exists in the it_companies list.
does_exist = 'Amazon' in it_companies
print(does_exist) #True
does_exist = 'Infinix' in it_companies
print(does_exist) #False

#16 Sort the list using sort() method
it_companies.sort()
print(it_companies) #['Amazon', 'Apple', 'FB', 'GOOGLE', 'IBM', 'LG', 'Microsoft', 'Oracle', 'Samsung']

#17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies) #['Samsung', 'Oracle', 'Microsoft', 'LG', 'IBM', 'GOOGLE', 'FB', 'Apple', 'Amazon']

#18 Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three) #['Samsung', 'Oracle', 'Microsoft']

#19 Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three) #['FB', 'Apple', 'Amazon']

#20 Slice out the middle IT company or companies from the list
middle_it = it_companies[4]
print(middle_it) #IBM

#21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies) #['Oracle', 'Microsoft', 'LG', 'IBM', 'GOOGLE', 'FB', 'Apple', 'Amazon']

#22 Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies) #['Oracle', 'Microsoft', 'LG', 'FB', 'Apple', 'Amazon']

#23 Remove the last IT company from the list
it_companies.pop()
print(it_companies) #['Oracle', 'Microsoft', 'LG', 'FB', 'Apple']

#24 Remove all IT companies from the list
del it_companies[0:]
print(it_companies) #[]

#25 Destroy the IT companies list
del it_companies

#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end) #['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'Python')
print(full_stack) #['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'Node', 'Express', 'MongoDB']
full_stack.insert(6, 'SQL')
print(full_stack) #['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']

# Exercises: Level 2
#1 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages) #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
min_age = min(ages)
print(min_age) #19
max_age = max(ages)
print(max_age) #26
#Add the min age and the max age again to the list
ages.append(min_age)
print(ages) #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19]
ages.append(max_age)
print(ages) #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
#Find the median age (one middle item or two middle items divided by two)
import statistics
median_age = statistics.median(ages)
print(median_age) #24.0
#Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age) #22.75
#Find the range of the ages (max minus min)
ages_range = max_age - min_age
print(ages_range) #7
#Compare the value of (min - average) and (max - average), use abs() method
average_age = sum(ages) / len(ages)
minimum_age = min(ages)
maximum_age = max(ages)
diff_min_average = abs(minimum_age - average_age)
diff_max_average = abs(maximum_age - average_age)
print(diff_min_average) #3.75
print(diff_max_average) #3.25

#1. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
num_countries = len(countries)
middle_index = num_countries // 2
if num_countries % 2 == 0:
    middle_countries = [countries[middle_index - 1], countries[middle_index]]
else:
    middle_countries = [countries[middle_index]]
print(middle_countries) #['Lesotho']

#2 Divide the countries list into two equal lists if it is even if not one more country for the first half.
num_countries = len(countries)
middle_index = num_countries // 2
if num_countries % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]
print(first_half) #['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho']
print(second_half) #['Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
#3 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
unpack_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = unpack_countries
print(first_country) #China
print(second_country) #Russia
print(third_country) #USA
print(scandic) #['Finland', 'Sweden', 'Norway', 'Denmark']