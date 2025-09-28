#Sales Data Analysis (Lists & Loops)
sales_input=[]
for i in range(1):
    for j in range(7):
        ele=input()
        sales_input.append(ele)
sales_list=[int(x) for x in +sales_input.split()]
max_sales=max(sales_list)
total_sales=sum(sales_list)

print(max_sales)
print(total_sales)