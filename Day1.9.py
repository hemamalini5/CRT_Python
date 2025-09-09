num1= int (input("enter a integer: "))
num2= int (input("enter a integer: "))
num3= int (input("enter a integer: "))
if(num1<num2) and (num1<num3):
    print(f"{num1} is Smallest")
elif(num2<num1) and (num2<num3):
    print(f"{num2} is Smallest")
else:
    print(f"{num3} is Smallest")
#ternery operator
Smallest=num1 if(num1<num2 and num1<num3) and (num1<num3) else num2
res=num3 if(num3<num1 and num3<num2) else Smallest
print(f"{res} is Smallest number ")