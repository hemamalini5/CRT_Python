# Insurance Premium Calculator

# Dictionary for base premiums by vehicle type (optional)
base_premiums = {
    "Car": 5000,
    "Bike": 3000,
    "Truck": 8000
}

class Insurance:
    def __init__(self, name, age, vehicle_type, base_premium):
        self.name = name
        self.age = age
        self.vehicle_type = vehicle_type
        self.base_premium = base_premium

    def calculate_premium(self):
        # Lambda to calculate risk factor: 20% extra if age < 25
        risk_factor = lambda age: 1.2 if age < 25 else 1.0
        final_premium = self.base_premium * risk_factor(self.age)
        return final_premium

# Reading input
name = input()
age = int(input())
vehicle_type = input()
base_premium_input = float(input())

# Optionally, override base premium using dictionary
# base_premium = base_premiums.get(vehicle_type, base_premium_input)
base_premium = base_premium_input

# Create Insurance object
customer = Insurance(name, age, vehicle_type, base_premium)

# Calculate and display premium
print(f"Final Premium: ₹{customer.calculate_premium():.2f}")
