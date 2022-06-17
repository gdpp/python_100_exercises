# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    # Suppose the following input is supplied to the program:
# 9
    # Then, the output should be:
# 11106

number = input("Enter a number: ")

tmp = ''
result = 0

while len(tmp) != 4:
    tmp = tmp + number
    result = result + int(tmp)

print(result)