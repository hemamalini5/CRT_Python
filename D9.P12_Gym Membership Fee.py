#Gym Membership Fee
class Member:
    def __init__(self, name, duration, payment_method):
        self.name = name
        self.duration = duration
        self.payment_method = payment_method

    def final_fee(self):
        # Fee table
        fee_table = {1: 1000, 3: 2700, 12: 10000}
        fee = fee_table.get(self.duration, 0)

        print(f"Fee before discount: ₹{fee:.2f}")

        # Apply discount if payment is Online
        if self.payment_method.lower() == "online":
            discount = fee * 0.05
            final_fee = fee - discount
        else:
            final_fee = fee

        print(f"Final Fee after discount: ₹{final_fee:.2f}")


# -------- Input Section --------
name = input().strip()
duration = int(input().strip())
payment_method = input().strip()

member = Member(name, duration, payment_method)
member.final_fee()
