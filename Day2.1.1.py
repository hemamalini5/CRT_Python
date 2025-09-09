#ATM Withdrawal Validation
amount=int(input("Enter the amount : "))
if(amount<=5000 and amount%100==0):
    print("Withdrawl Successful")
else:
    print("Insufficient Balance")