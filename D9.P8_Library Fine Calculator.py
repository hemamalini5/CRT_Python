#Library Fine Calculator
# Function to calculate fine
def calculate_fine(days):
    if days <= 5:
        return days * 2
    elif days <= 10:
        return days * 5
    else:
        return days * 10

# BookLoan class
class BookLoan:
    def __init__(self, title, late_days):
        self.title = title
        self.late_days = int(late_days)

    def calculate_fine(self):
        fine = calculate_fine(self.late_days)
        print(f"Fine: ₹{fine:.2f}")

# -------- Driver Code --------
book_title = input().strip()
late_days = input().strip()

loan = BookLoan(book_title, late_days)
loan.calculate_fine()
