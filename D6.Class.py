class Student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age= age
        self.branch= branch
    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Student age : {self.age}")
        print(f"Student Branch : {self.branch}")
    
s1= Student("Alice",20,"CSE")
s1.display()