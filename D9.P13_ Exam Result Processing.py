#Exam Result Processing
class Result:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_result(self):
        total = sum(self.marks)
        average = total / len(self.marks)

        # Grading system (same as Problem 2)
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")


# -------- Higher-order function --------
def process_students(process_fn, students):
    for student in students:
        process_fn(student)


# -------- Input Section --------
name = input().strip()
marks = list(map(int, input().split()))

student = Result(name, marks)

# Using higher-order function (process one student here)
process_students(lambda s: s.display_result(), [student])
