# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
# Example: If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

words = list(input('Enter words separates by whitespace: \n').split(' '))
result = []

for word in words:
    if word.isdigit():
        result.append(word)


print(result)


# using list comprehension method
result2 = [word for word in words if word.isdigit()]

print(result2)