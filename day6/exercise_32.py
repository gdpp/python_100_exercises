# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
# and the values are square of keys. The function should just print the keys only.

def keys_dict():
    return {x : x ** 2 for x in range(1, 21)}.keys()


print(keys_dict())