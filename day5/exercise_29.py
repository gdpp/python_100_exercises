# Define a function that can accept two strings as input and concatenate them and then print it in console.

def sentence(a, b):
    return f"{a} {b}"

exit = 'n'
while exit == 'n':
    words = input("Enter two words separate by whitespace: ").split(' ')
    
    a, b = words
    print(a)
    print(b)
    
    print(sentence(a, b))
    
    exit = input("Exit (y/n): ")
    