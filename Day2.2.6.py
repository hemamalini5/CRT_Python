#print the odd numbers from n to 1
n=int(input("Enter the Integer : "))
print(f"Odd numbers from  {n} to 1: ")
for i in range(n,0,-1):
    if(i%2!=0):
        print(i)