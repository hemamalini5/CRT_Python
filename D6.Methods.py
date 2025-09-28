class Student:
    print()
    print("Student object is created.....!")
    print()
    #Motutor or Setter Method 
    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age=age
    def set_branch(self,branch):
        self.branch=branch
    #Accessor or Getter Method
    def get_name(self):
        print(f"Student Name : {self.name}")
    def get_age(self):
        print(f"Student age : {self.age}")
    def get_branch(self):
        print(f"Student Branch : {self.branch}")