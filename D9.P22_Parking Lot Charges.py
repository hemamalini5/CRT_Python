# Parking Lot Charges

# Hourly rates dictionary
hourly_rates = {
    "Car": 50,
    "Bike": 20
}

class Parking:
    def __init__(self, vehicle_type, hours_parked):
        self.vehicle_type = vehicle_type
        self.hours_parked = hours_parked

    def calculate_fee(self):
        if self.hours_parked > 12:
            fee = 1000  # Flat penalty
        else:
            fee = hourly_rates.get(self.vehicle_type, 0) * self.hours_parked
        
        print(f"Parking Fee: ₹{fee:.2f}")


# Reading input
vehicle_type = input()
hours_parked = int(input())

# Create Parking object
parking = Parking(vehicle_type, hours_parked)

# Calculate and print fee
parking.calculate_fee()
