# Online Course Enrollment

# Course fees dictionary
course_fees = {
    "Python": 5000,
    "Java": 6000,
    "AI": 10000
}

class Course:
    def __init__(self, name, course_name, early_flag):
        self.name = name
        self.course_name = course_name
        self.early_flag = early_flag

    def enroll(self):
        # Get course fee
        fee = course_fees.get(self.course_name, 0)
        print(f"Course: {self.course_name}")
        print(f"Fee before discount: ₹{fee:.2f}")
        
        # Apply early-bird discount if applicable
        discount = 0
        if self.early_flag.lower() == "yes":
            discount = 0.15 * fee
            print(f"Early-bird Discount (15%): ₹{discount:.2f}")
        
        final_fee = fee - discount
        print(f"Final Fee: ₹{final_fee:.2f}")


# Reading input
name = input()
course_name = input()
early_flag = input()