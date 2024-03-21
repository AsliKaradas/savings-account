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

    # If a user types an invalid password three times - exiting, or if valid - continuing.
    if count == 3:
        print('\n 3 failed PIN attempts. EXITING ....')
        print('Your Savings Account Card has been Locked! \n')
        exit()

    print('Login Successful, CONTINUE\n')
    print(str.capitalize(users[n]), 'Welcome to your Savings Account!')

    # Main menu

    def display_balance():
        """
        This function will show the user's savings account balance.
        """
        global amounts
        print()
        print(str.capitalize(usernames[n]), 'You have ',
                                            amounts[n], '$ on Your Account.\n')

    def cash_withdraw(withdrawal_amount):
        """
        This function will process the withdrawal cash amount
        and check if the withdrawal amount was greater than the entered amount,
        It will show a message that the entered amount is not valid.
        """
        global amounts
    
        if withdrawal_amount > amounts[n]:
            print('\nThe Amount is not AVAILABLE!')
        else:
            amounts[n] = amounts[n] - withdrawal_amount
            print()
            print()
            print(f"{withdrawal_amount} Dollars successfully widthdrawn! ")
            print('Your Remaining Balance is', amounts[n], '$')

    def cash_deposit(deposit_amount):
        """
        This function will process the deposit cash amount and
        check if the deposit amount was less than 10€..
        It will show a message that the deposit amount must be greater than 10$
        """
        global amounts
    
        if deposit_amount <= 10:
            print('\n\n The Amount You Want to Deposit must be more than 10$')
        else:
            amounts[n] = amounts[n] + deposit_amount
            print('\n\nYour new Balance is: ', amounts[n], ‚$‘)

