# Write a program that accepts a sentence and calculate the number of letters and digits.
    # Suppose the following input is supplied to the program:
# hello world! 123
    # Then, the output should be:
# LETTERS 10
# DIGITS 3


sentence = input('Enter a sentence: \n')

letters = 0
digits = 0

for w in sentence:
    if w.isalpha():
        letters += 1
    elif w.isnumeric():
        digits += 1
        
print(f'LETTERS: {letters}')
print(f'DIGITS: {digits}')