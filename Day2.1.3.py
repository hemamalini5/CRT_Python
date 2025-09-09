#Movie Ticket pricing
age=int(input("Enter customer's age: "))
if(age<12):
    print("Children ticket price is 150 rupees")
elif(age>12 and age<18):
    print("Teenage between 12 to 18 ticket price is 200 rupees")
elif(age>=18):
    print("Adult ticket price is 300 rupees")
