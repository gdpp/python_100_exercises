# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

lst = [1,2,3,4,5,6,7,8,9,10]
sqrList = list(map(lambda x: x ** 2, lst))
result = list(filter(lambda x: x % 2 == 0, sqrList))
print(result)