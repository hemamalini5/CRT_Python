#Electricity Bill Generator
def calculate_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return bill

# -------- Driver Code --------
customer_name = input().strip()
units_consumed = int(input().strip())

bill_amount = calculate_bill(units_consumed)

print(f"Customer: {customer_name}")
print(f"Bill: ₹{bill_amount:.2f}")
