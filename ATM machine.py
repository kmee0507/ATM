#Swamp Donkeys
#CS 21
#ATM MACHINE

#See the opening message
print('HELLO')
print()
#get pin number
def main():
    pin_number = input('Enter your PIN number: ')

    if pin_number == '1994':
        menu()
    else:
        print('Invalid PIN')
        
#This function displays the menu if the pin number is correct
def menu():
    keep_going = 'yes'
    while keep_going == 'yes':
        #display menu options
        print("Menu Options")
        print("1: Deposit")
        print("2: Withdrawal")
        print("3: $100 Fast-Cash Withdrawal")
        print("4: Check Balance")
        print("5: Transfer Balance")
        print("6: Quit")
        selection=input("Please select an option: ")
    #determine which selection is chose
    
        if selection == "1":
            print("You've selected deposit")
            deposit()
            keep_going = input('Do you want to keep going(yes/no)? ')
        elif selection == "2":
            print("You've selected withdrawal")
            withdrawal()
            keep_going = input('Do you want to keep going(yes/no)? ')
        elif selection == "3":
            print("You've selected $100 Fast-Cash Withdrawal")
            fast_cash()
            keep_going = input('Do you want to keep going(yes/no)? ')
        elif selection == "4":
            print("You've selected Check Balance")
            check_balance()
            keep_going = input('Do you want to keep going(yes/no)? ')
        elif selection == "5":
            print("You've selected Transfer Balance")
            transfer_balance()
            keep_going = input('Do you want to keep going(yes/no)? ')
        elif selection == "6":
            keep_going = input('Did you mistakenly hit quit program? ')
            quit_program()
        else:
            print('That was not one of the choices')
            keep_going = input('Do you want to keep going(yes/no)? ')
            
        
        

        

#This function allows the user to deposit an amount into checkings or savings
def deposit():

    #label the variables

    account=input('Choose account type to make a deposit(checking or savings): ')
    deposit_amount=float(input('Please enter an amount to deposit: $'))

    #calculate the account type and amount of money deposited

    if deposit_amount>0 and account=='checking':
        print(format(deposit_amount,'.2f'),'has been added\
 to your checking account')
    elif deposit_amount>0 and account=='savings':
        print(format(deposit_amount,'.2f'),'has been added\
 to your savings account')
    else:
        print('The amount entered was invalid')
#This function allows the user to withdraw an amount from checking or savings
def withdrawal():
    CHECKING_BALANCE = 100000
    SAVING_BALANCE = 250000
    #determine which account to withdraw from
    withdrawal= (input("Would you like to withdraw from \
checking or savings: "))

    #if account is checkings figure out an amount to withdraw
    #amount must be divisble by 20 and no more than 240
    if withdrawal=="checking":
        withdrawal_1=int(input("How much would you like to \
withdraw from checking \n (increments of 20 no more than 240): "))
        if withdrawal_1 % 20 == 0 and withdrawal_1 <=  240:
            CHECKING_BALANCE=CHECKING_BALANCE - withdrawal_1
            print("You're new checking balance is :$",\
                  format(CHECKING_BALANCE,'.2f'))
        #display error        
        else:
            print("Error needs to be in denominations of $20 or less than $240")

    #if account is savings figure out an amount to withdraw
    #amount must be divisble by 20 and no more than 240       
    elif withdrawal=="savings":
        withdrawal_2=int(input("How much would you like to \
withdraw from savings \n (increments of 20 no more than 240): "))
        if withdrawal_2 % 20 == 0 and withdrawal_2 <= 240:
                SAVING_BALANCE=SAVING_BALANCE - withdrawal_2
                print("You're new saving balance is :$",\
                      format(SAVING_BALANCE,'.2f'))
        #display error
        else:
            print("Error needs to be in denominations of $20 or less than $240")
  

    #error if account is not checking or savings
    else:
        print("Error")

        

#This function will allow the user to transfer money between their checking
#and savings accounts
#define the function
def transfer_balance():

    #label the variables
    
    destination=input('Choose an account to transfer \
into (checking or savings): ')
    
    transfer_amount=int(input('Enter the amount you wish to transfer: '))
    
    checking_balance=100000
    
    savings_balance=250000

    #calculate the change in checking

    if destination=="checking" and 0<transfer_amount<savings_balance:
        
        new_checking_balance= transfer_amount + checking_balance
        new_savings_balance= savings_balance - transfer_amount
        
        #display new balance
                              
        print('You now have $',format(new_checking_balance,'.2f'),
              'in your checking account.')
        print('You now have $',format(new_savings_balance,'.2f'),
              'in your savings account.')

        #Calculate change in savings
        
    elif destination=="savings" and 0<transfer_amount<checking_balance:
        
            new_savings_balance= transfer_amount + savings_balance
            new_checking_balance= checking_balance - transfer_amount
        
        #display new balance
                             
            print('You now have $',format(new_savings_balance,'.2f'),
              'in your savings account.')
            print('You now have $',format(new_checking_balance,'.2f'),
                  'in your checking account.')
            
    #display appropriate errors if necessary                
    else:           
        print('Invalid amount to transfer.')

#this functions allows the user to check the balance of both there accounts        
def check_balance ():
    CHECKINGS_BALANCE = 100000
    SAVINGS_BALANCE = 250000
    #ask user which account they need
    account_wanted= str(input(\
        "Would you like your checking or savings account: "))

    #display if user wants savings
    if account_wanted=="savings":
        print("Your account balance is: $", \
              format(SAVINGS_BALANCE, '.2f'))

    #display if user wants checking
    elif account_wanted=="checking":
        print("Your account balance is: $", \
              format(CHECKINGS_BALANCE, '.2f'))

    #otherwise an error message
    else:
        print("Error. Enter either 'checking' or 'savings'") 

#this function gives the user 100$ of cash from one of two accounts
#and subtracts the money from the account
def fast_cash():
    CHECKINGS_BALANCE = 100000
    SAVINGS_BALANCE = 250000
    #figure out which account you want to access
    balance_type = input('Which account do you want \
to access(checking/savings): ')
    
    #subtract 100 from savings
    if balance_type == 'savings':
        print('Your new account balance is: $',\
          format(SAVINGS_BALANCE - 100, '.2f'))
        
    #subtract 100 from checkings
    elif balance_type == 'checking':
        print('Your new account balance is: $',\
          format(CHECKINGS_BALANCE - 100, '.2f'))
    #display error if its not one of the two options
    else:
        print('Error must be either checkings or savings')
    
#this function ends the atm program
def quit_program():
    print('This session is now over, please come back again!')
                
main()
