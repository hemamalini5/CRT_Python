#Palindrome Number
n=int(input("Enter the value of n : "))
rem,rev=0,0
temp=n
print(f"User entered value {n}")
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(f"Reverse Number is {rev}")
if(temp==rev):
    print("Palindrome")
else:
    print("Not a Palindrome")
