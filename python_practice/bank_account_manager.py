'''
Bank Account Manager
Abstract Account class with three other classes
- CheckingAccount
- SavingsAccount
-BusinessAccount
ATM style program
'''

class Account():
    # All things shared by other accounts

    def __init__(self,account_number, opening_deposit):
        self.account_number = account_number
        self.balance = opening_deposit

    def __str__(self):
        return 'Your balance is {}'.format(self.balance)

    def deposit(self,dep_amount):
        self.balance += dep_amount

    def withdraw(self,wit_amount):
        if self.balance > wit_amount:
            self.balance -= wit_amount
        else:
            return 'Funds Too Low'


class Checking(Account):
    def __init__(self,account_number,opening_deposit):
        # Run the base class __init__
        super().__init__(account_number,opening_deposit)

    # Define a __str__ method that returns a string specific to Checking accounts
    def __str__(self):
        return f'Checking Account #{self.account_number}\n  Balance: {Account.__str__(self)}'


class BusinessAccount(Account):
    def __init__(self,account_number,opening_deposit):
        super().__init__(account_number,opening_deposit)

    def __str__(self):
        return 'Business Account has a balance of {}'.format(Account.__str__(self))

class SavingsAccount(Account):
    def __init__(self,account_number,opening_deposit):
        super().__init__(account_number,opening_deposit)

    def __str__(self):
        return 'Savings Account has a balane of {}'.format(Account.__str__(self))


class Customer():
    def __init__(self,name,PIN):
        self.name = name
        self.PIN = PIN

        self.accounts = {'C':[],'B':[],'S':[]}

    def __str__(self):
        return self.name

    def open_checking(self,account_number,opening_deposit):
        self.accounts['C'].append(Checking(account_number,opening_deposit))

    def open_savings(self,account_number,opening_deposit):
        self.accounts['S'].append(SavingsAccount(account_number,opening_deposit))

    def open_business(self,account_number,opening_deposit):
        self.accounts['B'].append(BusinessAccount(account_number,opening_deposit))

    def total_deposit(self):
        total = 0
        for account in self.accounts['C']:
            total += account.balance
        for account in self.accounts['S']:
            total += account.balance
        for account in self.accounts['B']:
            total += account.balance
        print("Total amount is {}".format(total))
