class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f"{self.name} has an average grade of {self.average()}"
    
    def __repr__(self):
        return f"Student(name={self.name}, grades={self.grades})"

student = Student()
#print(Student.average(student))

# print(student.average())
# print(Student.average(student))

print(student)