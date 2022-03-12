# Update User.py so that each instance's methods are chained

class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

mike = User("mike")
cleighton = User("cleighton")
marco = User("marco")

# Use the methods to test 

mike.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(400).display_user_balance()

cleighton.make_deposit(200).make_deposit(200).make_withdrawal(300).display_user_balance()

marco.make_deposit(300).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

mike.transfer_money(100, marco)
