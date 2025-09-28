# MultiLevel Inheritance

class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
        print("This is Grandfather Class")
        # Store 'a' as an instance attribute
        self.a = 10

    def grandfather_method(self):
        print("This is Grandfather Method")

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        print("This is Father class")
        super().__init__(grandfathername) # Correctly call parent's __init__
        self.fathername = fathername

    def father_method(self):
        self.grandfather_method() # Correct method name
        print("This is father Method")
        self.b = self.a + 10 # Correctly use instance attributes

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        print("This is Son class")
        super().__init__(fathername, grandfathername) # Correctly call parent's __init__
        self.sonname = sonname

    def son_method(self):
        print("This is Son Method")
        # Ensure 'b' is defined before using it
        if not hasattr(self, 'b'):
            self.father_method()
        self.c = self.b + 5

    def display(self):
        self.son_method() # Ensure 'c' is defined before printing
        print(f"GrandFather Name : {self.grandfathername}")
        print(f"Father Name : {self.fathername}")
        print(f"Son Name : {self.sonname}")
        print(f"Result from methods : {self.c}") # Better output formatting

# Create an object of the Son class and call display
s = Son("David", "Ram", "Shyam")
s.display()
