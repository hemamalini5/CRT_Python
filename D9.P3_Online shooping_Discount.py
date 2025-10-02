# Online Shopping Discount
def apply_discount(discount_fn, amount):
    return discount_fn(amount)

# Discount functions
def discount_10(amount):
    return amount * 0.9

def discount_5(amount):
    return amount * 0.95

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def final_price(self):
        total = self.price * self.quantity
        # Decide discount
        if total > 1000:
            final = apply_discount(discount_10, total)
        else:
            final = apply_discount(discount_5, total)

        # Print results
        print(f"\nProduct: {self.name}")
        print(f"Total before discount: ₹{total:.2f}")
        print(f"Final Price after discount: ₹{final:.2f}")

# -------- Driver Code --------
product_name = input()
price = input()
quantity = input()

p = Product(product_name, price, quantity)
p.final_price()
