#Hybrid Inheristence
class Grandfather:
    def __init__(self, grandfathername, **kwargs):
        # Call the constructor of the next class in the MRO
        super().__init__(**kwargs)
        self.grandfathername = grandfathername

    def grandfather_method(self):
        print("This is Grandfather Method")
        self.a = 10

class Father(Grandfather):
    def __init__(self, fathername, **kwargs):
        # Call the constructor of the next class in the MRO
        super().__init__(**kwargs)
        self.fathername = fathername

    def father_method(self):
        print("This is Father Method")
        self.grandfather_method()
        self.b = self.a + 10

class Mother(Grandfather):
    def __init__(self, mothername, **kwargs):
        # Call the constructor of the next class in the MRO
        super().__init__(**kwargs)
        self.mothername = mothername

    def mother_method(self):
        print("This is Mother Method")
        self.grandfather_method()
        self.c = self.a + 20

class Son(Father, Mother):
    def __init__(self, sonname, fathername, mothername, grandfathername):
        # The single super() call handles the entire chain based on the MRO.
        # Arguments are passed down the chain using keyword arguments.
        # Note: The `sonname` argument is not passed to `super()` as it is specific to `Son`.
        super().__init__(fathername=fathername, mothername=mothername, grandfathername=grandfathername)
        self.sonname = sonname
        
    def son_method(self):
        print("This is Son Method")
        self.father_method()
        self.mother_method()
        self.d = self.b + self.c + 5
    
    def display(self):
        self.son_method()
        print(f"GrandFather Name : {self.grandfathername}")
        print(f"Father Name : {self.fathername}")
        print(f"Mother Name : {self.mothername}")
        print(f"Son Name : {self.sonname}")
        print(f"Result from methods : {self.d}")

# Create an object of the Son class and call display
s = Son('John', 'James', 'Jane', 'Michael')      
s.display()

