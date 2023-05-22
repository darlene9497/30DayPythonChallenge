# Exercises: Day 6
# Exercises: Level 1
#1 Create an empty tuple
empty_tuple = ()

#2 Create a tuple containing names of your sisters and your brothers
brothers = ('Norman', 'Brolin', 'Jensen')
sisters = ('Valerie','Meyer')

#3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings) #('Norman', 'Brolin', 'Jensen', 'Valerie', 'Meyer')

#4 How many siblings do you have?
print(len(siblings)) #5

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
print(siblings) #['Norman', 'Brolin', 'Jensen', 'Valerie', 'Meyer']
siblings.append('Mummy')
siblings.append('Daddy')
print(siblings) #['Norman', 'Brolin', 'Jensen', 'Valerie', 'Meyer', 'Mummy', 'Daddy']
family_members = tuple(siblings)
print(family_members) #('Norman', 'Brolin', 'Jensen', 'Valerie', 'Meyer', 'Mummy', 'Daddy')

# Exercises: Level 2
#1 Unpack siblings and parents from family_members
family_members = ['Norman', 'Brolin', 'Jensen', 'Valerie', 'Meyer', 'Mummy', 'Daddy']
*siblings, first_parent, second_parent = family_members
print(siblings) #['Norman', 'Brolin', 'Jensen', 'Valerie', 'Meyer']
print(first_parent) #Mummy
print(second_parent) #Daddy

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'pineapple', 'pears')
vegetables = ('onions', 'carrots', 'cabbage')
animal_products = ('milk', 'cheese', 'ghee')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp) #('apple', 'pineapple', 'pears', 'onions', 'carrots', 'cabbage', 'milk', 'cheese', 'ghee')

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt) #['apple', 'pineapple', 'pears', 'onions', 'carrots', 'cabbage', 'milk', 'cheese', 'ghee']

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[4:5]
print(middle_item) #('carrots')

#5 Slice out the first three items and the last three items from food_staff_lt list
first_list_items = food_stuff_lt[0:3]
last_list_items = food_stuff_lt[-3:]
print(first_list_items) #['apple', 'pineapple', 'pears']
print(last_list_items) #['milk', 'cheese', 'ghee']

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#i. Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries) #False
#ii. Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries) #True