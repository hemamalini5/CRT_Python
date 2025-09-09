#Train Ticket Concession
age = int(input("Enter your age: "))
if(age<=5):
    print("Free")
elif(5<=age<=12):
    print("Half Ticket")
elif(13<=age<=59):
    print("Ful ticket")
else:
    print("30% Senior Citizen Ticket")