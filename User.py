class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()

mike = User("mike")
cleighton = User("cleighton")
marco = User("marco")

mike.make_deposit(100)
mike.make_deposit(200)
mike.make_deposit(300)
mike.make_withdrawal(400)
mike.display_user_balance()

cleighton.make_deposit(200)
cleighton.make_deposit(200)
cleighton.make_withdrawal(300)
cleighton.display_user_balance()

marco.make_deposit(300)
marco.make_withdrawal(50)
marco.make_withdrawal(50)
marco.make_withdrawal(50)
marco.display_user_balance()

mike.transfer_money(100, marco)
