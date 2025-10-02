#Inventory Management System
# Lambda for tax (let's assume 0% for simplicity, but can change easily)
tax = lambda amount: amount * 0.0   # No tax in sample case

class Inventory:
    def __init__(self):
        # Initial stock (can be extended easily)
        self.stock = {
            "Rice": [50, 60],   # 50 units at ₹60 each
            "Wheat": [30, 40],  # extra example
            "Sugar": [20, 50]   # extra example
        }

    def update_stock(self, product, qty):
        if product not in self.stock:
            print("Product not found!")
            return None

        available_qty, price_per_unit = self.stock[product]
        if qty > available_qty:
            print("Insufficient stock!")
            return None

        # Update stock
        self.stock[product][0] -= qty
        return price_per_unit

    def generate_bill(self, product, qty):
        price_per_unit = self.update_stock(product, qty)
        if price_per_unit is None:
            return

        cost = price_per_unit * qty
        total_with_tax = cost + tax(cost)

        print(f"Purchased {qty} {product} for ₹{total_with_tax:.2f}")
        print(f"Remaining Stock for {product}: {self.stock[product][0]} units")


# -------- Driver Code --------
product_name = input().strip()
quantity = int(input().strip())

inv = Inventory()
inv.generate_bill(product_name, quantity)
