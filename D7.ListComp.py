#print a list of even numbers from 1-11 using list comprehension
list=[]
for i in range(1,11):
    if i%2==0:
        list.append(i)
print(list)