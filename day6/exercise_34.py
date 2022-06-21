# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the first 5 elements in the list.

def square_list():
    my_list =  [ x ** 2 for x in range(1, 21)]
    print(my_list[0:5])
    
    
square_list()