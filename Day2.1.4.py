#Employee Overtiime Pay
hours=int(input("Enter the number of hours worked: "))
if(hours>8):
    overtime_pay=hours*100
    print(f"Overtime pay is {overtime_pay} rupees")
else:
    print("No overtime pay")