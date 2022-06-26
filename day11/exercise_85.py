# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

my_list = [x for k, x in enumerate([12,24,35,70,88,120,155]) if k != 0 and k != 4 and  k != 5]
print(my_list)