# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

exit = 'n'
while exit == 'n':
    response = input("Input a string: ")

    if response == "YES" or response == "Yes" or response == "yes":
        print('Yes')
    else:
        print("No")
        
    exit = input("Exit (y/n): ")