class students:
    roll = ""
    gpa = ""
    def __init__(self,Roll,Gpa):
        self.roll = Roll
        self.gpa = Gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = students(102,3.33)
rahim.display()

karim = students(105,3.67)
karim.display()