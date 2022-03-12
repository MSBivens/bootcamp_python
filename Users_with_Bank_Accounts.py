class BankAccount:
    accounts = []
    
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_accounts_info(cls):
        for account in cls.accounts:
            account.display_account_info()

# Update the User class __init__ method
# Update the User class make_deposit method
# Update the User class make_withdrawal method
# Update the User class display_user_balance method

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking": BankAccount(0.02,1000),
            "savings" : BankAccount(0.05,3000)
        }
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

mike = User("mike")

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
mike.account['checking'].deposit(100)
mike.display_user_balance()