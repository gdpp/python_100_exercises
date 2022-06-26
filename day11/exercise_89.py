# Define a class Person and its two child classes: Male and Female. 
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    def __init__(self, gender):
        self.gender = "Unknown"

    def printGender(self):
        return self.gender
        
class Male(Person):
    def __init__(self):
        self.gender = 'Male'
    
    def printGender(self):
        return self.gender

class Female(Person):
    def __init__(self):
        self.gender = "Female"
    
    def printGender(self):
        print(self.gender)

male = Male()
female = Female()

print(male.printGender())
print(female.printGender())
