##read the name and print the length of the name and check if it more than 5 characters
name = input("Enter the name: ")
print(f"Length of the name is {len(name)}")
if len(name) >5 :
    print("More than 5 characters ")
else:
    print("5 or less characters ")

#teranary operator
res="More than 5 characters " if len(name)>5 else "5 or less characters"
print(res)