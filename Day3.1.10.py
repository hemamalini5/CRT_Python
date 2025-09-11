Guest_List=[]
while(True):
    print("-------------------Guest List Menu ------------------------")
    print("1.To view the Guest List ")
    print("2.To Add the Guest ")
    print("3.To chechk the particular guest is attendind the party or not")
    print("4.Remove the Guest List")
    print("5.To print the finalized guest list & exits ")
    choice=int(input("Enter your Choice: "))
    if(choice==1):
        if(len(Guest_List)==0):
            print("Guest List is Empty")
        else:
            print(Guest_List)
        print()
    elif(choice==2):
        guest=input("Enter the Guest Name : ")
        Guest_List.append(guest)
        print(f"{guest} is added to guest list.....!")
        print()
    elif(choice==3):
        guest=input("Enter the guest name to check the status of attending the party : ")
        if guest in Guest_List:
            print(f"{guest} is attending the party.....! ")
        else:
            print(f"{guest} is not attending the party.........!")
        print()
    elif(choice==4):
        guest=input("Enter the name of the guest name who's attending the party: ")
        if guest in Guest_List:
            Guest_List.remove(guest)
            print(f"{guest} is removed from the guest list......! ")
        print()
    elif(choice==5):
        print("Finalised the Guest List : ")
        print()
        print(Guest_List)
        break