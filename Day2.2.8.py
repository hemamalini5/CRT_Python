# Print the Multiplication table of n in reverse order
n=int(input("enter the value : "))
print(f"Reverse Multipication of {n}:")
for i in range(10,-1,-1):
    print(f"{n}*{i} = {n*i}")