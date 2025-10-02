# Loan EMI Calculator

class Loan:
    def __init__(self, principal, annual_interest_rate, tenure_months):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.tenure_months = tenure_months

    def calculate_emi(self):
        # Convert annual rate to monthly decimal rate
        R = self.annual_interest_rate / 12 / 100
        
        # EMI formula
        P = self.principal
        N = self.tenure_months
        emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
        print(f"Monthly EMI: ₹{emi:.2f}")


# Reading input
principal = float(input())
annual_interest_percent = float(input())
tenure_months = int(input())

# Create Loan object
loan = Loan(principal, annual_interest_percent, tenure_months)

# Calculate and print EMI
loan.calculate_emi()
