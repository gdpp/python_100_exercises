# Please write a program to output a random number, which is divisible by 5 and 7, 
# between 10 and 150 inclusive using random module and list comprehension.

import random

result = [x for x in range(random.randint(10, 151)) if x % 5 == 0 and x % 7 == 0]

print(random.choice(result))