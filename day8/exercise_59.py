# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.

num =  int(input("Enter a number: \n"))
res = 0

for n in range(1, num + 1): 
    res += n / (n + 1)
    
print(round(res, 2))