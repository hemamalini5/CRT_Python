# School Attendance System

class Attendance:
    def __init__(self, name, attendance_percent):
        self.name = name
        self.attendance_percent = attendance_percent

    def check_eligibility(self):
        # Lambda to determine eligibility
        is_eligible = lambda percent: "Eligible" if percent >= 75 else "Not Eligible"
        status = is_eligible(self.attendance_percent)
        print(f"{self.name} is {status} for Exam")


# Reading input
name = input()
attendance_percent = float(input())

# Create Attendance object
student = Attendance(name, attendance_percent)

# Check and print eligibility
student.check_eligibility()
