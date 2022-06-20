# Define a class with a generator which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:
# 7

# Then, the output should be:
# 0
# 7
# 14

class MyClass():    
    def generator_divisible(self, number):
        for x in range(0, number + 1):
            if x % 7 == 0:
                yield x

obj1 = MyClass()

response = obj1.generator_divisible(int(input("Enter a number: ")))

for number in response:
    print(number)