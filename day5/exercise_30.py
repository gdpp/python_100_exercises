# Define a function that can accept two strings as input 
# and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line.

results = []
def word_max_lenght(word1, word2):
    if len(word1) > len(word2):
        results.append(word1)
    elif len(word1) < len(word2):
        results.append(word2)
    else:
        results.append(word1)
        results.append(word2)
        
    return results

words = input("Enter two words separates by comma: ").split(',')

word1, word2 = words

print('\n'.join(word_max_lenght(word1, word2)))