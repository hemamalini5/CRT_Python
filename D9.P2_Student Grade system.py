#Student Grade Management
class Student:
    def init(self,name,m1,m2,m3,m4,m5):
        self.name = name
        self.sub1,self.sub2, self.sub3,self.sub4,self.sub5= m1,m2,m3,m4,m5
        self.avg = self.Average()
        self.grade = self.Grade()
    def Average(self):
        return (self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)/5
    def Grade(self):
        #lambda function to determine grade
        grade = lambda avg: 'A' if avg >= 90 else ('B' if 75 <= avg < 90 else ('C' if 50 <= avg < 75 else 'Fail'))
        return grade(self.avg)
        
        
    def display(self):
        print(f"Student : {self.name}")
        print(f"Average Marks : {self.avg}")
        print(f"Grade : {self.grade}")
Name = input("Enter Student Name: ")
marks = list(map(int,input("Enter marks of 5 subjects: ").split()))
S2 = Student(Name,marks[0],marks[1],marks[2],marks[3],marks[4])
S2.display()