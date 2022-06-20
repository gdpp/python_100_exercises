# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers. 
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

numbers = input("Enter sequence of numbers separates by comma: ").split(',')
result = [str(int(x) ** 2) for x in numbers if int(x) % 2 != 0]
print(', '.join(result))