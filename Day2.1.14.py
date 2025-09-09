#Mobile Data Balance Checker
balance = int(input("ENter the data balance in MB: "))
if balance==0:
    print("Recharge Now")
elif balance<=100:
    print("Low data Warning")
else:
    print("Sufficient data available")