# Write a program which accepts basic mathematic expression from console and print the evaluation result.
# Example: If the following n is given as input to the program:
# 35 + 3
# Then, the output of the program should be:
# 38

mathExpression = input("Write math basic mathematic expression: \n")
result = eval(mathExpression)

print(result)