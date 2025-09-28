#Single LEvel Inheristence
class parent:
    def __init__(self,father_name):
        print("This is a parent class")
        self.father_name=father_name
        self.a=10
    def parent_method(self):
        print("This is a parent method")
        self.b=self.a+10
class child(parent):
    def __init__(self,child_name,father_name):
        self.child_name=child_name
        parent.__init__(self,father_name)
        print("This is a child class")
    def child_method(self):
        print("Child mmethod")
        if not hasattr(self, 'b'):
            self.parent_method()
        self.d=self.b+5
    def display(self):
        self.child_method()
        print("This is a child method")
        print(f"Father Name :{self.father_name}")
        print(F"child Name :{self.child_name}")
        print(self.d)

c=child("john","ram")
c.display()