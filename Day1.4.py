num=int(input("Enter the integer: "))
if((num>=100 and num<=999) or (num>=-999 and num<=-100)):
    print("Three Digit Number")
else:
    print("Not a Three Digit Number")
#ternery operator
res="Three Digit Number" if((num>=100 and num<=999) or (num>=-999 and num<=-100)) else "Not a Three Digit Number"
print(res)