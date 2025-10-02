#Method overriding
class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer Work---------")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Software Engineer Worxk-------------")
class CivilEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Civil Engineer Work-------------")
e=Engineer
se=SoftwareEngineer
c= CivilEngineer
e.work()
se.work()
c.work()