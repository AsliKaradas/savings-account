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
usernames = ['savings1', 'savings2', 'savings3']
passwords = ['0001', '0002', '0003', '0004']
amounts = [10000, 20000, 30000]
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

# While loops will confirm the passwords to verify the user's login
while count <= 3:
    pin = input('Please Enter Your PIN: ')

    if pin.isdigit():
        if user == 'savings1':
            if pin == passwords[0]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()

        if user == 'savings2':
            if pin == passwords[1]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()

        if user == 'savings3':
            if pin == passwords[2]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()
    else:
        print('\nPIN must Consists of 4 Digits.\n')
        count += 1
