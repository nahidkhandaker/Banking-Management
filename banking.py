# Simple static Banking Management Project
# Overview: Develop a static Banking Management system featuring basic functionalities like deposit, withdraw & Balance Inquiry (Get Balance) operations.
# Requirements:
# Default User/Holder Name & Initial Balance:
# * Set up a default User/Holder name and an initial balance for demonstration purposes.
# Deposit Functionality:
# * Ensure that the deposit amount is greater than 0. Negative values are not allowed.
# Withdrawal Functionality:
# * Ensure the withdrawal amount does not exceed the available balance.
# Balance Inquiry:
# * Display the updated balance after every successful deposit or withdrawal transaction.


class Banking:
    def __init__(self, username, initial_balance):
        self.name = username
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return amount
    
    def get_balance(self):
        return self.balance 

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount

        else:
            return f"Insufficient balance"


bkash = Banking('Bkash', 10000)
print(f'Account Name: {bkash.name}')
print(f'Inotial Balance: {bkash.balance}')
print(f'Deposit Balance: {bkash.deposit(5000)}')
print(f'After deposit, Your balance is: {bkash.get_balance()}')
print(f'Withdraw Balance: {bkash.withdraw(8000)}')
print(f'After withdraw, Your balance is: {bkash.get_balance()}')

