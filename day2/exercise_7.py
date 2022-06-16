# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i * j.
    # Suppose the following inputs are given to the program: 3,5
    # Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

result = []
numbers = input('Enter two numbers separates by coma: ').split(',')
X, Y = numbers

for i in range(int(X)):
    tmp = []
    for j in range(int(Y)):
        tmp.append(i*j)
    
    result.append(tmp)

print(result)