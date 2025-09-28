#Cafe Biling System
coffee=float(input("Price of one coffee: "))
snack=float(input("Price of one snack: "))
num_coffee=int(input("Number of coffees ordered: "))
num_snacks=int(input("Number of snacks ordered: "))

total_bill= (coffee*num_coffee) + (snack*num_snacks)

service_charge= total_bill * 0.05
total= total_bill + service_charge

print(total) #print total bll