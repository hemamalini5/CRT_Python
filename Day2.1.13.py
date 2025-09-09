#Temperature eligiblity
Temperature=int(input("Enter the TEmperature: "))
if Temperature <0:
    print("Freezing weather")
elif Temperature>0 and Temperature<=10:
    print(" Cold Weather")
elif Temperature>=21 and Temperature <=35:
    print("Hot Weather")