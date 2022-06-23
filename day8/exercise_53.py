# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# In case of input data being supplied to the question, 
# it should be assumed to be a console input.

exit = 'n'
while exit == 'n':
    email = input("Enter email: \n")
    
    if email:
        user, domain = email.split('@')
        print(user)
    else:
        print("introduce an email")
    exit = input("Exit (y/n): ")
