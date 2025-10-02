# Railway Reservation System

# Fare dictionary
class_fares = {
    "Sleeper": 500,
    "AC": 1000
}

class Reservation:
    def __init__(self, name, age, class_type):
        self.name = name
        self.age = age
        self.class_type = class_type

    def ticket_summary(self):
        # Get base fare from dictionary
        base_fare = class_fares.get(self.class_type, 0)
        
        # Apply senior citizen discount if age > 60
        if self.age > 60:
            final_fare = base_fare * 0.9  # 10% discount
        else:
            final_fare = base_fare
        
        print(f"Ticket Price: ₹{final_fare:.2f}")


# Reading input
name = input()
age = int(input())
class_type = input()

# Create Reservation object
passenger = Reservation(name, age, class_type)

# Print ticket summary
passenger.ticket_summary()
