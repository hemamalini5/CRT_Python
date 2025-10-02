# Flight Ticket Booking
def apply_discount(discount_fn, amount):
    return discount_fn(amount)

# Discount functions
def discount_50(amount):  # For children < 12
    return amount * 0.5

def discount_30(amount):  # For seniors > 60
    return amount * 0.7

def no_discount(amount):  # For others
    return amount

class Passenger:
    def __init__(self, name, age, ticket_price):
        self.name = name
        self.age = int(age)
        self.ticket_price = float(ticket_price)

    def final_bill(self):
        # Choose discount based on age
        if self.age < 12:
            final = apply_discount(discount_50, self.ticket_price)
        elif self.age > 60:
            final = apply_discount(discount_30, self.ticket_price)
        else:
            final = apply_discount(no_discount, self.ticket_price)

        # Print result
        print(f"Passenger: {self.name}")
        print(f"Final Ticket Price: ₹{final:.2f}")

# -------- Driver Code --------
name = input()
age = input()
ticket_price = input()

p = Passenger(name, age, ticket_price)
p.final_bill()
