# Please write a program using generator to print the numbers which can be divisible 
# by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70

def divisibleGenerator(num):
    for n in range(0, num):
        if n % 5 == 0 and n % 7 == 0:
            yield n
            

number = int(input())
result = []

for x in divisibleGenerator(number):
    result.append(str(x))


print(', '.join(result))