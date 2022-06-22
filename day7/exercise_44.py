# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

def squareRoot(num):
    return num ** 2

squaredList = list(map(squareRoot, range(1,21)))

print (squaredList)