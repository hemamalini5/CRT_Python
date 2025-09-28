#Print the next 25 Leap Years 
year=int(input("Enter the year:  "))
count=0
while count<25:
    year+=1
    if (year%4==0) or (year%4==0 and year%100!=0):
        print(year,end=" ")
        count+=1