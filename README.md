# SAVINGS ACCOUNT PROGRAM


This Python program facilitates the management of savings accounts, allowing users to check their account balance, make withdrawals (cash withdrawals), and deposits.

![image](/mockup.png)

## USER EXPERIENCE

The user is required to provide an existing username initially, and upon successful matching of the username, the system will prompt for a PIN number. Once the user completes these sign-in procedures, they gain access to all functionalities. The process is straightforward; users can easily verify their account statements. Upon entering the system, users can check their account balance by inputting "1". To initiate a withdrawal, they should enter "2" followed by specifying the desired amount. For depositing money, users need to select "3" and then input the amount they wish to add to their account. Finally, users can exit the system by selecting "4".



## FEATURES


**WELCOME**

![messge](/welcome_message.png)

______

**LOGIN** 

 Users can execute transactions by confirming their own account statements; all user inputs are validated, and errors permit  multiple attempts to enter a valid username and password.

**Successful Login**<br>
**User: savings1**

![login](/correct_username.png)

**INVALID USERNAME**

![login](/invalid_username.png)

**INVALID PASSWORD**<br>
**User: savings2**

![login](/invalid_pin1.png)



**FAILED LOGIN**

![login](/invalid_pin1.png)

______

**MENU** 

 Transaction Menu: This functionality enables users to select transactions from the menu according to their preferences.      Users can check their account balance and perform withdrawals or deposits into specified accounts.

![menu](/choose.png)



**INVALID** 

![login](/invalid_pin1.png)


______

**SAVINGS A/C BALANCE**

 This feature allows users to check the amount of balance they have on their account so they can make a valid transaction.

![login](/balance.png)

____________

**CASH WITHDRAW**

 This feature allows users to withdraw the amount they wish. Here also, all user inputs are validated, and errors allow repeat opportunities to input a valid amount. For withdrawal, the user must enter an integer amount. This program does not accept float numbers for cash withdrawal. Furthermore, users cannot withdraw more than their balance.

![deposit](/withdraw.png)

___________________

**CASH DEPOSIT**

 Users can utilize this feature to deposit their desired amount. Here as well, all user inputs are validated, and errors      provide multiple opportunities to input a valid amount. Users can make deposits exceeding ten dollars. This program does     not  accept floating-point numbers for cash deposits.

![deposit](/withdrawal_amount.png)

_______________________


**EXIT SYSTEM**

Upon completion of a transaction, users can exit the system by selecting option 4.

![exit](/exit.png)



##Libraries
- **OS** - to clear the system after user login.
- **String** - To capitalize the usernames.
- **Time** - To add the sleep() function to make a delay in the terminal.

##Programs
- **Github** - To store my repository.
- **python** - To write Saving Account Program.
- **Heroku** - To deploy the program.

## Testing

- Tested on https://www.online-ide.com/online_python_syntax_checker and fixed some bugs.
- Tested in my Gitpod local terminal.

## Bugs

### Solved Bugs

![bug](/bug.png)
![bug](/bug_1.png)
![bug](/bug_2.png)
![bug](/bug_3.png)

## Deployment

Steps for deployment:
1. Click "New" and select "Create new app".
2. Input a meaningful name for your app and choose the region best suited to your location.
3. Select "Settings" from the tabs.
4. Set the buildbacks to python and NodeJS in that order.
5. Select "Deploy" from the tabs.
6. Link the Heroku app to the respository.
7. Select "GitHub - Connect to GitHub" from deployment methods.
8. Type GitHub repository by name.
9. Click Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
10. Click on Deploy.
11. Click View button to view the deployed site.

### Credits

- [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) 
- [Source Code Hero](https://sourcecodehero.com/atm-program-in-python-with-source-code/)
- Youtube Tutorials

