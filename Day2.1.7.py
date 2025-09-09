#Water Reminder App
hours=int(input("enter the number of hours since the user last drank water: "))
if(hours>=4):
    print("You are dehydrated Drink water now!")
elif(hours>2 and hours<3):
    print("Drink a glass of water")
elif(hours<2):
    print("You're fine")