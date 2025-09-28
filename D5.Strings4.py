#check how many alphabets,digits and special characters are there in the given string
string=input("Enter the string :")
alphabets,digits,special=0,0,0
for ch in string:
    if ch.isalpha():
        alphabets+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1
print(f"Count of alphabet character: {alphabets}")
print(f"Count of digits {digits} ")
print(f"Count of the special characters {special}")