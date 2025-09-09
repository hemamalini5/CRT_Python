num1= int (input("enter a integer: "))
num2= int (input("enter a integer: "))
num3= int (input("enter a integer: "))
if(num1>num2) and (num1>num3):
    print(f"{num1} is largest")
elif(num2>num1) and (num2>num3):
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")
#ternery operator
largest=num1 if(num1>num2 and num1>num3) and (num1>num3) else num2
res=num3 if(num3>num1 and num1>num3) else largest
print(f"{res} is largest number ")