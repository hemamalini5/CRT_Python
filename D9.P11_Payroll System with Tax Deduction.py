#Payroll System with Tax Deduction
class Employee:
    def __init__(self, name, basic, allowances):
        self.name = name
        self.basic = basic
        self.allowances = allowances

    def net_salary(self):
        gross = self.basic + self.allowances
        # Lambda for tax calculation
        tax_fn = lambda g: g * 0.10 if g > 50000 else g * 0.05
        tax = tax_fn(gross)
        net = gross - tax

        # Printing results
        print(f"Gross Salary: ₹{gross:.2f}")
        print(f"Tax: ₹{tax:.2f}")
        print(f"Net Salary: ₹{net:.2f}")


# -------- Input Section --------
name = input().strip()
basic = float(input().strip())
allowances = float(input().strip())

emp = Employee(name, basic, allowances)
emp.net_salary()
