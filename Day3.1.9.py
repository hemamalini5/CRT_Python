#arithmetic OPrations using Iteration
a=int(input("Enter the first value: "))
b=int(input("Enter the Second VAlue: "))
while(True):
    print("----------------------Oprations Menu----------------------")
    print("1.Addition")
    print("2.subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        print(f"Summation of{a} and {b} is {a+b}") 
    elif(choice==2):
        print(f"Subtraction of{a} and {b} is {a-b}") 
    elif(choice==3):
        print(f"Multiplication of{a} and {b} is {a*b}")
    elif(choice==4):
        print(f"Division of {a} and {b} is {a/b}")
    elif(choice==5):
        print("Thanks for using the Operations Menu ")
        break