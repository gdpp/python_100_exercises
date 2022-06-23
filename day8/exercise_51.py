# Write a function to compute 5/0 and use try/except to catch the exceptions.

try:
    result = 5 / 0
    print(result)
except ZeroDivisionError:
    print("Divide with number greater than 0")

