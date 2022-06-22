# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

my_tuple = tuple(input().split(','))

result = []
for x in my_tuple:
    if int(x) % 2 == 0:
        result.append(x)
        

print(tuple(result))