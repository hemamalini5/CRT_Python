#Print the Multiplication tables from 1 to n 
n=int(input("enter the value : "))
for n in range(1,n+1):
    print(f"Multipication of {n}:")
    for i in range(1,11):
        print(f"{n}*{i} = {n*i}")