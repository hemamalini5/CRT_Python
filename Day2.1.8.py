#Electricity Bill Calculator
unit=int(input("Enter the number of units consumed: "))
if unit<=100:
    bill=unit*5
    print(f"Electricity Bill is : {bill}") 
elif unit>100 and unit<=200:
    bill=100*5+(unit-100)*7
    print(f"Electricity Bill is : {bill}") 
elif unit>200 and unit<=300:
    bill=100*5+100*7+(unit-200)*10
    print(f"Electricity Bill is : {bill}") 
