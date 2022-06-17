# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# v1
result = []

def validateNumber(num):
    return all(ord(x) % 2 == 0 for x in num)

for number in range(1000, 3001):
    if validateNumber(str(number)):
        result.append(str(number))

print(", ".join(result))

#short version
short_result = [str(i) for i in range(1000,3001)]
short_result = list(filter(validateNumber, short_result))
print(", ".join(short_result))
                 