# Define a custom exception class which takes a string message as attribute.

class CustomError(Exception):
    """
    Custom Error Exception
    Attributes:
        message -> the error message
    """
    
    def __init__(self,  msg):
        self.msg = msg


lst = list(input("Enter a list of numbers: ").split(' '))

try:
    if len(lst) > 5:
        raise CustomError("List length is greater than 5")
    elif len(lst) < 5:
        raise CustomError("List length is less than 5")
except CustomError as CustErr:
    print(f"The message error is: {CustErr.msg}")
