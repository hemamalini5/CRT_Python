# Expense Tracker

class Expense:
    def __init__(self, food, travel, bills):
        self.food = food
        self.travel = travel
        self.bills = bills

    def category_percentages(self):
        total = self.food + self.travel + self.bills
        print(f"Total: ₹{total:.2f}")
        
        # Lambda to calculate percentage
        percent = lambda amount: (amount / total) * 100
        
        print(f"Food: {percent(self.food):.2f}%")
        print(f"Travel: {percent(self.travel):.2f}%")
        print(f"Bills: {percent(self.bills):.2f}%")

# Reading input
food_amount = float(input())
travel_amount = float(input())
bills_amount = float(input())

# Create Expense object
my_expense = Expense(food_amount, travel_amount, bills_amount)

# Calculate and print category percentages
my_expense.category_percentages()
