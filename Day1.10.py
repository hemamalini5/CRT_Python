num1=int(input('Enter the integer: '))
num2=int(input('Enter the integer: '))
num3=int(input('Enter the integer: '))
if((num1<=num2 <=num3) or (num3<= num2 <=num1)):
    print(f"{num2} is middle number  ")
elif((num2<=num1<=num3) or (num3<=num1<=num2)):
    print(f"{num1} is middle number  ")
else:
    print(f"{num3} is middle number  ")
#ternery operator
middle = (
    num2 if ((num1 <= num2 <= num3) or (num3 <= num2 <= num1))
    else num1 if ((num2 <= num1 <= num3) or (num3 <= num1 <= num2))
    else num3
)
print(f"{middle} is middle number  ")