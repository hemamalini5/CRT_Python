num=int(input("Enter the integer: "))
if((num>=10 and num<=99) or (num>=-99 and num<=-10)):
    print("Two Digit Number")
else:
    print("Not a Two Digit Number")
#ternery operator
res="Two Digit Number" if((num>=10 and num<=99) or (num>=-99 and num<=-10)) else "Not a Two Digit Number"
print(res)