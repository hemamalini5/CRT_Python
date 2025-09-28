#Multiple Level Inheristence
class Father:
    def __init__(self,number1):
        self.number1=number1
        print("This Base class 1")
    def Father_method(self):
        print("This is Father Method")
        self.a=self.number1+10

class Mother:
    def __init__(self,number2):
        self.number2=number2
        print("This is Base class 2")
    def Mother_method(self):
        print("This is Mother Method")
        self.b=self.number2+20

class child(Father,Mother):
    def __init__(self, number1,number2):
        Father.__init__(self,number1)
        Mother.__init__(self,number2)
        print("This is Child class")
    def child_method(self):      
        print("This is Child Method")
        if not hasattr(self, 'a'):
            self.Father_method()
        if not hasattr(self, 'b'):
            self.Mother_method()
        self.c=self.a+self.b+5  

    def display(self):
        self.child_method()
        print(f"Father Number : {self.number1}")
        print(f"Mother Number : {self.number2}")
        print(f"Result from methods : {self.c}")
# Create an object of the Child class and call display
c=child(10,20)      
c.display()
