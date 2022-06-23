# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.1416*(self.radius**2)


circle = Circle(10)

print(circle.area())

circle2 = Circle(22)

print(circle2.area())