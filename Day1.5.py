num=int(input("Enter the integer: "))
if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000)):
    print("Fourth Digit Number")
else:
    print("Not a Fourth Digit Number")
#ternery operator
res="Fourth Digit Number" if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000)) else "Not a Fourth Digit Number"
print(res)