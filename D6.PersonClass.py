class Person:
    def __init__(self, name, age, gender, contact_number, nationality, aadhar_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.nationality = nationality
        self.aadhar_number = aadhar_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Nationality: {self.nationality}")
        print(f"Aadhar Number: {self.aadhar_number}")
        print("-" * 20)

# Create 5 objects of the Person class
person1 = Person("Anya Sharma", 25, "Female", "9876543210", "Indian", "1234 5678 9012")
person2 = Person("Rahul Singh", 30, "Male", "9988776655", "Indian", "9876 5432 1098")
person3 = Person("Maria Rodriguez", 28, "Female", "5551234567", "Spanish", "XYZ-987-654")
person4 = Person("John Doe", 45, "Male", "0123456789", "American", "PQR-012-345")
person5 = Person("Chen Wei", 35, "Male", "8889990001", "Chinese", "CDE-456-789")

# Access and display the data for each person object
print("--- Person 1 Details ---")
person1.display_details()

print("--- Person 2 Details ---")
person2.display_details()

print("--- Person 3 Details ---")
person3.display_details()

print("--- Person 4 Details ---")
person4.display_details()

print("--- Person 5 Details ---")
person5.display_details()