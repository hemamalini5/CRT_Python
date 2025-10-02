#Bank Account Simulator

# Lambda for transaction fee (1%)
transaction_fee = lambda amount: amount * 0.01

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        amount=float(amount)
        fee=transaction_fee(amount)
        total_deduction=amount+fee
        if total_deduction > self.balance:
            print("Insufficient Balance.withdrawal refused")
        else:
            self.balance-=total_deduction
    def display_balance(self):
        print(f"Account Holder : {self.name}")
        print(f"Final Balance: {self.balance}")
        

name=input()
initial_balance=input()
withdraw_amount=input()
deposit_amount=input()

#create account object
account=BankAccount(name,initial_balance)

#Perform withdrwal and deposit
account.withdraw(withdraw_amount)
account.deposit(deposit_amount)

account.display_balance()