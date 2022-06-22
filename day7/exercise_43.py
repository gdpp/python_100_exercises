# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

lst = list(range(1, 21))

result = filter(lambda  x: x % 2 == 0, lst)

print(list(result))

result2 = filter(lambda i: i % 2 == 0, range(1, 21))

print(list(result2))
