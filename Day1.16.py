num=int(input("Enter the Integer :"))
if (num%3==0 and num%5==0):
    print("FrizzBuzz")
elif(num%3==0):
    print("Frizz")
elif(num%5==0):
    print("Buzz")