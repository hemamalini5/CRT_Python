num1=int(input("Enter the first Integer:"))
num2=int(input("Enter the Second Integer:"))
if(num1>num2):
    print(f"{num1}is largest")
else:
    print(f"{num2} is largest")
#ternery operator 
res=num1 if(num1>num2) else num2
print(f"{res} is largest number")