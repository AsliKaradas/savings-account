# imprt libraries
import time

print("\n\nPlease Insert Your Savings Account Card!\n\n")
time.sleep(2)

# Savings Account
# while loop checks existance of the enterd username
print("****************************************************************************")
print("*                                                                          *")
print("*                               SAVINGS ACCOUNT                            *")
print("*                                                                          *")
print("****************************************************************************")

# Creating user's information for login
usernames = ['savings1', 'savings2', 'savings3', 'savings4']
passwords = ['0001', '0002', '0003', '0004']
amounts = [10000, 20000, 30000, 4000]
count = 0

# Checks users' information 
while True:
    user = input('\nPlease Enter Your  Username: ')
    user = user.lower()

    if user in usernames:
        if user == usernames[0]:
            n = 0
        elif user == usernames[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('\n\n     Invalid Username!!')
