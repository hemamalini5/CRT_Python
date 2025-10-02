#Food Ordering System
# Higher-order function for applying discount
def apply_discount(discount_fn, amount):
    return discount_fn(amount)

# Discount functions
def discount_10(amount):   # 10% discount
    return amount * 0.10

def discount_5(amount):    # 5% discount
    return amount * 0.05

# Service charge lambda (5%)
service_charge = lambda amount: amount * 0.05

class Order:
    def __init__(self, food, price, qty):
        self.food = food
        self.price = float(price)
        self.qty = int(qty)

    def generate_invoice(self):
        subtotal = self.price * self.qty

        # Decide discount function
        if subtotal > 500:
            discount = apply_discount(discount_10, subtotal)
        else:
            discount = apply_discount(discount_5, subtotal)

        after_discount = subtotal - discount
        service = service_charge(after_discount)
        final_amount = after_discount + service

        # Print Invoice
        print(f"Bill: ₹{subtotal:.2f}")
        print(f"Discount: ₹{discount:.2f}")
        print(f"Service Charge: ₹{service:.2f}")
        print(f"Final Amount: ₹{final_amount:.2f}")

# -------- Driver Code --------
food_name = input().strip()
price = input().strip()
quantity = input().strip()

order = Order(food_name, price, quantity)
order.generate_invoice()
