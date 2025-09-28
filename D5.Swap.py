#Swapping two integers in different ways 
a=int(input("Enter the first Number: "))
b=int(input("Enter the second Number: "))
print("\n Original Values : a=",a ,"b=",b)

#Using Aithmetic Operators 
a=a+b
b=a-b
a=a-b
print("\n After Swapping using arithmetic operator ")
print("a=",a,"b=",b)

#Reset values for next method
a=int(input("Enter the first Number : "))
b=int(input("Enter the second Number: "))
#using  a third variable
temp=a
a=b
b=temp

print("\n After the Swapping Using a third variable ")
print("a= ",a,"b= ",b)

#Reset values for next method
a=int(input("Enter the first number: "))
b=int(input("Enter the second Number: "))
a,b=b,a
print("\n After the Swapping without using third variable: ")
print("a= ",a,"b= ",b)