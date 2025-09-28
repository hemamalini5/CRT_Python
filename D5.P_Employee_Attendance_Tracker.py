#Employee Attendance Tracker

attendance=input("Enter attendance string: ") 
present="P"
Absent="A"
Late="L"
num_P=0
num_A=0
num_L=0
for ch in attendance:
    if ch==present:
        num_P+=1
    elif ch==Absent:
        num_A+=1
    elif ch==Late:
        num_L+=1
if num_A>5 or num_L>3:
    print("Not Eligible")
else:
    print("Eligible")