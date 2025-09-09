#Loan eligiblity
Salary=int(input("Enter the Salary: "))
Credit_Score=int(input("Enter the Credit Score: "))
if Salary>=30000 and Credit_Score>=700:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")