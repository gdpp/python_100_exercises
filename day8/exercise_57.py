# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

word  = input("Enter a word: \n")

unicode_word = word.encode('utf-8')

print(unicode_word)