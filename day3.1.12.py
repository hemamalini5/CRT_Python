#print the count of even numbers and odd numbers present in the list
list=[10,20,45,80,74,62,15]
even_count=0
odd_count=0
i=0
while i <len(list):
    if list[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i=i+1
print(f"Even count in the list : {even_count}")
print(f"Odd count in the list : {odd_count}")
