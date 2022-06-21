# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def square_list():
    my_list =  [ x ** 2 for x in range(1, 21)]
    print(my_list)
    

square_list()