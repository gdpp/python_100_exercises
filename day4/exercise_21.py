# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. 
# Please write a program to compute the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# Then, the output of the program should be:
# 2
import math

result = 0
exit = 'n'
x, y = 0, 0

while exit == 'n':
    instruction = tuple(input("Enter instructions (UP, DOWN, LEFT, RIGHT,) and number: ").split(' '))
    
    if instruction[0] == 'UP':
        y += int(instruction[1])
    
    if instruction[0] == 'LEFT':
        x += int(instruction[1])
        
    if instruction[0] == 'DOWN':
        y -= int(instruction[1])
        
    if instruction[0] == 'RIGHT':
        x -= int(instruction[1])
    
    exit = input("Exit (y/n): ")

distance = round(math.sqrt(x ** 2 + y ** 2))
print(f"Result: {distance}")
