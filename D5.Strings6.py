#Print the 12 digit number where last 4 digits or written last 4 digits being visible
adhaar= input("Enter the 12 digit adhaar number:")
masked_Adhaar="*"*8+adhaar[-4:]
print(f"Masked Adhaar : {masked_Adhaar}")