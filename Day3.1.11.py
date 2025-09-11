#remove negative numbers from list
list=[10,-5,2,14,-9]
i=0
while i <len(list):
    if list[i]<0:
       del list[i]
    i=i+1
print(list)