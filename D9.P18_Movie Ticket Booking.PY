# Movie Ticket Booking

class MovieTicket:
    def __init__(self, tickets_count, seat_type, base_price):
        self.tickets_count = tickets_count
        self.seat_type = seat_type
        self.base_price = base_price

    def calculate_total(self):
        # Determine per-ticket price
        if self.seat_type.lower() == "premium":
            per_ticket_price = self.base_price * 1.5
        else:
            per_ticket_price = self.base_price
        
        print(f"Per-ticket price ({self.seat_type}): ₹{per_ticket_price:.2f}")
        
        # Total before discount
        total_before_discount = per_ticket_price * self.tickets_count
        print(f"Total before discount: ₹{total_before_discount:.2f}")
        
        # Apply group discount if
