# Define a class which has at least two methods:
    # getString: to get a string from console input
    # printString: to print the string in upper case.

#Also please include simple test function to test the class methods.

from sys import argv
 
class Player():
    def getString(self):
        print("Getting word. . . ")
        self.word = argv[1]
    
    def getInputString(self):
        self.word2 = input("Enter the second word: ")
        
    def printString(self):
        print(f"This is the word: {self.word.upper()}")
        print(f"This is the second word: {self.word2.upper()}")
        
        

playerOne = Player()

playerOne.getString()
playerOne.getInputString()
playerOne.printString()


