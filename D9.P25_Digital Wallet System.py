# Digital Wallet System

class Wallet:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def add_money(self, amount):
        self.balance += amount
        self.transactions.append(f"Recharge: ₹{amount:.2f}")
        print(f"After Recharge: ₹{self.balance:.2f}")

    def make_payment(self, amount):
        if amount > self.balance:
            print("Insufficient balance for payment.")
            return
        self.balance -= amount
        self.transactions.append(f"Payment: ₹{amount:.2f}")
        cashback = 0.02 * amount  # 2% cashback
        self.balance += cashback
        self.transactions.append(f"Cashback: ₹{cashback:.2f}")
        print(f"After Payment: ₹{self.balance - cashback:.2f}")
        print(f"Cashback (2% of payment): ₹{cashback:.2f}")
        print(f"Final Balance: ₹{self.balance:.2f}")

    def get_balance(self):
        return self.balance

# Reading input
initial_balance = float(input())
recharge_amount = float(input())
payment_amount = float(input())

# Create Wallet object
my_wallet = Wallet(initial_balance)

# Initial balance
print(f"Initial Balance: ₹{my_wallet.get_balance():.2f}")

# Add money
my_wallet.add_money(recharge_amount)

# Make payment
my_wallet.make_payment(payment_amount)
