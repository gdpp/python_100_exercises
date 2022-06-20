# Write a method which can calculate square value of number

def square_root(x, y):
    return x ** y

exit = 'n'
while exit == 'n':
    numbers = input("Enter two numbers separates with comma: ").split(',')
    x , y = numbers
    print(square_root(int(x), int(y)))
    exit = input("Exit (y/n): ")