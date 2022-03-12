# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class

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

# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

savings = BankAccount(0.05,1000)
checking = BankAccount(0.02,5000)

savings.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
checking.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(50).yield_interest().display_account_info()

BankAccount.all_accounts_info()