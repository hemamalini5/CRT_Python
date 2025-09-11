#print the maximum number present in the list of numbers
list=[10,52,14,32,47,85,95,63]
m=0
i=0
while i <len(list):
    if list[i]>m:
        m=list[i]
    i=i+1
print(f"Maximum Number in the list {m}")

list=[10,52,14,32,47,85,95,63]
print(f"Maximum Number in the list {max(list)}")
