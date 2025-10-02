class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        # Convert the string inputs to the float data type
        self.name = name
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = float(hours_worked)

    def calculate_salary(self):
        # The regular work week is 40 hours
        regular_hours = 40
        overtime_rate = 1.5

        if self.hours_worked > regular_hours:
            # Calculate regular pay for the first 40 hours
            regular_pay = regular_hours * self.hourly_rate
            # Calculate overtime pay for any hours worked over 40
            extra_hours = self.hours_worked - regular_hours
            overtime_pay = extra_hours * self.hourly_rate * overtime_rate
            return regular_pay + overtime_pay
        else:
            # If no overtime, salary is just hours worked multiplied by the rate
            return self.hours_worked * self.hourly_rate
    
    def show_details(self, salary):
        print(f"\nEmployee Name: {self.name}")
        print(f"Total Salary: ${salary:.2f}")

# Get employee data from the user
name = input('Enter the employee Name: ').strip()
rate = input('Enter the Rate of Pay: ').strip()
hours = input('Enter the No.of Working Hours: ').strip()

# Create an Employee object
emp = Employee(name, rate, hours)

# Calculate the salary using the method within the class
salary = emp.calculate_salary()

# Display the employee's details
emp.show_details(salary)
