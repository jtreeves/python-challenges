def withdraw_money(account_balance):
    amount = input('How much would you like to withdraw today?\n')
    account_balance -= int(amount)
    view_account_balance('Y',account_balance)
def deposit_money(account_balance):
    amount = input('How much would you like to deposit today?\n')
    account_balance += int(amount)
    view_account_balance('Y',account_balance)
def view_account_balance(choice,account_balance):
    if (choice == 'Y'):
        print(f'Your account balance is ${account_balance}')
    else:
        add_or_take = input('Would you like to withdraw or deposit today?\n')
        if (add_or_take == 'deposit'):
            deposit_money(account_balance)
        elif (add_or_take == 'withdraw'):
            withdraw_money(account_balance)
        else:
            view_account_balance('Y',account_balance)
print("Welcome to Chase bank.")
account_balance = 5000
choice = input('Would you like to view your account balance? Y/N\n')
view_account_balance(choice,account_balance)
print("Have a nice day!")