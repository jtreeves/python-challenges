print('Welcome to Chase bank.')
balance = 1000

def choose_action():
    option = input('What would you like to do? (display, deposit, withdraw) ')
    if option == 'display':
        view_balance()
    elif option == 'deposit':
        deposit_money()
    elif option == 'withdraw':
        withdraw_money()
    else:
        print('Have a nice day!')

def view_balance():
    print('Your balance is: ${}'.format(balance))
    choose_action()

def deposit_money():
    money = input('How much money would you like to deposit? ')
    print('You have deposited ${} into your account.'.format(money))
    money_int = int(money)
    balance += money_int
    view_balance()

def withdraw_money():
    money = input('How much money would you like to withrdaw? ')
    print('You have withdrawn ${} from your account'.format(money))
    money_int = int(money)
    balance -= money_int
    view_balance()

choose_action()

# print('Have a nice day!')