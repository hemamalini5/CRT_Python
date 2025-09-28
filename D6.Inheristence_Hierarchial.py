#Hierarchial Inheritence
# A single parent class (Grandfather) is inherited by multiple child classes (Father and Mother
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
        print(f"Grandfather: {self.grandfathername}")

    def grandfather_method(self):
        print("This is Grandfather Method")
        self.a = 10

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername
        print(f"Father: {self.fathername}")

    def father_method(self):
        print("This is Father Method")
        self.grandfather_method()
        self.b = self.a + 10
        print(f"Result in Father's method: {self.b}")

class Mother(Grandfather):
    def __init__(self, mothername, grandfathername):
        super().__init__(grandfathername)
        self.mothername = mothername
        print(f"Mother: {self.mothername}")

    def mother_method(self):
        print("This is Mother Method")
        self.grandfather_method()
        self.c = self.a + 20
        print(f"Result in Mother's method: {self.c}")

# Create objects of the child classes (Father and Mother)
# Both Father and Mother are directly descended from Grandfather
f = Father('James', 'Michael')
print("\n--- Calling Father's method ---")
f.father_method()

print("\n")

m = Mother('Jane', 'Michael')
print("\n--- Calling Mother's method ---")
m.mother_method()
