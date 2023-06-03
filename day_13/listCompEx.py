# Exercises: Day 13
#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero) #[-4, -3, -2, -1, 0]

#2 Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
flattened_list = [num for sublist in list_of_lists for inner_list in sublist for num in inner_list]
print(flattened_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#incomplete