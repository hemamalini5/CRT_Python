#CHeck whether it is  prime palindrome or not 
num=int(input("Enter the number: "))
prie= True
if num<=1:
    prime=False
for i in range(2,num):
    if num%i==0:
        prime=False
        break

original=str(num)
reverse=original[::-1]
palindrome=True if(original==reverse) else False
if prime and palindrome:
    print(f"{num} is a prime palindrome number")
else:
    print(f"{num} is not a prime palindrome number ")