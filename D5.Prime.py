#check whether the user entered integer is a prime number or not
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num=int(input("Enter the number: "))
result=("is a prime number" if is_prime(num) else "is not a prime number")
output_tuple=(f"The number {num} ",result)

print(" ".join(output_tuple))



"""if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")"""