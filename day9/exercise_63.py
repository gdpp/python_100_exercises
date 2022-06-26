# Please write a program using generator to print the even numbers between 0 and n 
# in comma separated form while n is input by console.
# Example: If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10

def enterNumber() -> int:
    num = input("Enter a number: \n")
    return int(num)

def evenNumbersGenerator(num: int): # can iterate
    for x in range(1, num + 1):
        if x % 2 == 0:
            yield x

num = enterNumber()

myList = []
for x in evenNumbersGenerator(num):
    myList.append(str(x))    

print(', '.join(myList))