#Hospital Bill Management
# Hospital Bill Management

class Patient:
    def __init__(self, name, room_charges, doctor_fee, medicine_cost):
        self.name = name
        self.room_charges = room_charges
        self.doctor_fee = doctor_fee
        self.medicine_cost = medicine_cost

    def final_bill(self):
        # Step 1: Compute subtotal
        subtotal = self.room_charges + self.doctor_fee + self.medicine_cost
        print(f"Subtotal: ₹{subtotal:.2f}")
        
        # Step 2: Compute GST
        gst = 0.18 * subtotal
        print(f"GST (18%): ₹{gst:.2f}")
        
        # Step 3: Amount after GST
        total_with_gst = subtotal + gst
        print(f"Amount after GST: ₹{total_with_gst:.2f}")
        
        # Step 4: Conditional discount
        discount = 0
        if total_with_gst > 20000:
            discount = 0.05 * total_with_gst
            print(f"Discount (5%): ₹{discount:.2f}")
        
        # Final bill
        final_amount = total_with_gst - discount
        print(f"Final Bill: ₹{final_amount:.2f}")


# Reading input
name = input()
room_charges = float(input())
doctor_fee = float(input())
medicine_cost = float(input())

# Create Patient object
patient = Patient(name, room_charges, doctor_fee, medicine_cost)

# Calculate and print final bill
patient.final_bill()
