# Python has many built-in functions, and if you do not know how to use it, 
# you can read document online or find some books. 
# But Python has a built-in document function for every built-in functions.
#Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#And add document for your own function

print(abs.__doc__)
print(print.__doc__)
print(int.__doc__)
print(input.__doc__)

class Dog():
    """This is my favorite dog and the message appears in the doc dunder method"""
    
    def test(self):
        pass


print(Dog.__doc__)