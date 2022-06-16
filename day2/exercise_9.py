# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect

# Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT

import sys

print('press Ctrl + Z and enter to end input sentences...')
print('Enter the sentenses and press enter to break line:')
sentences = sys.stdin.readlines()

for word in sentences:
    print(word.strip().upper())