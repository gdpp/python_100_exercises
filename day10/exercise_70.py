# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

import random

result = [x for x in range(random.randint(0, 11)) if x % 2 == 0 ]

print(random.choice(result))