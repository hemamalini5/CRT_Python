num1= int (input("enter a integer: "))
num2= int (input("enter a integer: "))
if(num1<num2):
    print(f"{num1}is Smallest")
else:
    print(f"{num2} is Smallest")
#ternery operator 
res=num1 if(num1<num2) else num2
print(f"{res} is Smallest number")