# Hostel Room Allocation

# Monthly rents dictionary
monthly_rents = {
    "Single": 5000,
    "Shared": 3000
}

class Hostel:
    def __init__(self, name, room_type, duration_months):
        self.name = name
        self.room_type = room_type
        self.duration_months = duration_months

    def room_allocation(self):
        # Get monthly rent
        monthly_rent = monthly_rents.get(self.room_type, 0)
        
        # Total rent before discount
        total_rent = monthly_rent * self.duration_months
        print(f"Total Rent before discount: ₹{total_rent:.2f}")
        
        # Apply 5% discount if duration is 12 months (yearly)
        if self.duration_months == 12:
            final_rent = total_rent * 0.95  # 5% discount
            print(f"Final Rent after yearly discount: ₹{final_rent:.2f}")
        else:
            final_rent = total_rent
            print(f"Final Rent: ₹{final_rent:.2f}")


# Reading input
name = input()
room_type = input()
duration_months = int(input())

# Create Hostel object
student = Hostel(name, room_type, duration_months)

# Calculate and print rent
student.room_allocation()
