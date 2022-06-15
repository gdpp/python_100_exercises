# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated 
# sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be:40320

n = int(input('Enter a number: '))
acc = 1
res = []

for i in range(1, n + 1):
    acc = acc * i
    res.append(str(acc))
    
print(', '.join(res))

acc = 1

print(([acc := acc * x for x in range(1, n + 1)]))