# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

money = 0
exit = 'n'


while exit == 'n':
    movement = input("Enter the movement D - Deposit W -Withdrawal and the amount: ").split(' ')
    
    type = movement[0].upper()
    amount = int(movement[1])
    
    if type == 'D':
        money += amount
    elif movement[0].upper() == 'W':
        if amount > money:
            print("Not enough money")
            continue
        else:
            money -= amount
    
    print(f"Bank account money: {money}")        
    exit = input("Exit (y/n): ")
    
