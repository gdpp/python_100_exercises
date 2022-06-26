# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

my_list = [x for x in [12,24,35,24,88,120,155] if x != 24]
print(my_list)