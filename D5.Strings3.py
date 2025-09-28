#Check entered name as the character in or not
name=input("enter the name: ")
char=input("Enter the character to ckeck:")
if char in name:
    print(f"{char} is present in {name}")
else:
    print(f"{char} is not present in {name}")