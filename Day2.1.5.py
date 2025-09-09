#Restraurant Discount System
Bill=int(input("Enter the total bill  amount:"))
if(Bill>1000):
    Dis=Bill*0.1
    print(f"Discount amount is : {Dis}")
elif(Bill>500):
    Dis=Bill*0.5
    print(f"Discount amount is : {Dis}")
elif(Bill<=500):
    print("No discount available")