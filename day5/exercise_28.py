# Define a function that can receive two integer numbers in string form 
# and compute their sum and then print it in console.

def addition(x, y):
    return x + y

exit = 'n'
while exit == 'n':
    numbers = input("Enter two numbers separates with comma: ").split(',')
    x , y = numbers
    print(addition(int(x), int(y)))
    exit = input("Exit (y/n): ")