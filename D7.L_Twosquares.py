#perform two squares 2 in the list using lambda functions
num=[1,2,3,4,5]
square=lambda:[val * val for val in num]
print(square())

#double the square values
num = [1,2,3,4,5]
res = [i+i for i in num]
print(res)