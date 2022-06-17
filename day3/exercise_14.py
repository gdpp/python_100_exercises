# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
    # Suppose the following input is supplied to the program:
# Hello world!
    # Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9


sentence = input('Enter a sentence: \n')

uppercase = 0
lowercase = 0

for w in sentence:
    if w.isupper():
        uppercase += 1
    elif w.islower():
        lowercase += 1
        
print(f'UPPER CASE: {uppercase}')
print(f'LOWER CASE: {lowercase}')