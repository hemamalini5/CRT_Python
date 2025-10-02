# Hotel Room Billing

# Room rates dictionary
room_rates = {
    "Standard": 2000,
    "Deluxe": 3500,
    "Suite": 5000
}

class Hotel:
    def __init__(self, guest_name, room_type, days, season):
        self.guest_name = guest_name
        self.room_type = room_type
        self.days = days
        self.season = season

    def final_bill(self):
        # Room charge
        rate = room_rates.get(self.room_type, 0)
        room_charge = rate * self.days
        print(f"Room charge ({self.days} nights at ₹{rate}): ₹{room_charge:.2f}")
        
        # Seasonal discount
        discount = 0
        if self.season.upper() == "OFF_SEASON":
            discount = 0.2 * room_charge
            print(f"Seasonal discount (20%): ₹{discount:.2f}")
        else:
            print("Seasonal discount (0%): ₹0.00")
        
        # Amount after discount
        amount_after_discount = room_charge - discount
        print(f"Amount after discount: ₹{amount_after_discount:.2f}")
        
        # Service tax 12%
        service_tax = 0.12 * amount_after_discount
        print(f"Service Tax (12%): ₹{service_tax:.2f}")
        
        # Final bill
        final_amount = amount_after_discount + service_tax
        print(f"Final Bill: ₹{final_amount:.2f}")


# Reading input
guest_name = input()
room_type = input()
days = int(input())
season = input()

# Create Hotel object
guest = Hotel(guest_name, room_type, days, season)

# Calculate and print final bill
guest.final_bill()
