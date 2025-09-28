class Employee:
    def __init__(self,emp_name,emp_num,resignation,emp_salary,dept_num):
        self.name = emp_name
        self.num=emp_num
        self.resignation=resignation
        self.salary=emp_salary
        self.dept=dept_num
    def display(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee Number : {self.num}")
        print(f"Employee Ressignation : {self.resignation}")
        print(f"Employee Salary : {self.salary}")
        print(f"Employee Department Number : {self.dept}")

e1=Employee("John",101,False,50000,10)
e2=Employee("Doe",102,True,60000,20)
e3=Employee("SMith",103,False,50000,30)
e4=Employee("Jane",104,True,70000,40)
e5=Employee("Emily",105,False,80000,50)
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()
