#Define a class, which have a class parameter and have a same instance parameter.

class Cat:
    name = 'Sally'
    
    def __init__(self, name = ''):
        self.name = name
        

salem = Cat('Salem')
print(salem.name)
print(Cat.name)