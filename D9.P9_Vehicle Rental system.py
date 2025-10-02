#Vehicle Rental system
# Higher-order function
def apply_discount(discount_fn, amount):
    return discount_fn(amount)

# Discount functions
def discount_10(amount):   # 10% discount
    return amount * 0.9

def discount_5(amount):    # 5% discount
    return amount * 0.95

def no_discount(amount):   # No discount
    return amount

# Vehicle class
class Vehicle:
    def __init__(self, vehicle_type, rate_per_day, days):
        self.vehicle_type = vehicle_type
        self.rate_per_day = float(rate_per_day)
        self.days = int(days)

    def rental_cost(self):
        total = self.rate_per_day * self.days

        # Apply discount rules
        if self.vehicle_type.lower() == "car" and self.days > 7:
            final = apply_discount(discount_10, total)
        elif self.vehicle_type.lower() == "bike" and self.days > 5:
            final = apply_discount(discount_5, total)
        else:
            final = apply_discount(no_discount, total)

        print(f"Total Rent: ₹{final:.2f}")

# -------- Driver Code --------
vehicle_type = input().strip()
rate_per_day = input().strip()
days = input().strip()

v = Vehicle(vehicle_type, rate_per_day, days)
v.rental_cost()
