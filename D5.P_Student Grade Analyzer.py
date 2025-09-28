# Student Grade Analyzer 
marks=tuple(map(int,input().split()))

avg=sum(marks)/len(marks)
if avg==int(avg):
        print(f"{avg:.1f}")
else:
        print(f"{avg:.2f}")

if avg>=40 and all(i>=35 for i in marks):
        print("Passed")
else:
        print("Failed")