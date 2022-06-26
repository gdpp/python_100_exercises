# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# In case of input data being supplied to the question, it should be assumed to be a console input.


def fib(num):
    if num < 2:
        result[num] = num
        return result[num]
    
    result[num] = fib(num - 1) + fib(num - 2)
    return result[num]

n = int(input())

result = [0] * (n + 1)

fib(n)
    
result = [str(x) for x in result]

print(', '.join(result))


