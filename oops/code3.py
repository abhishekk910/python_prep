class Student:

    counter = 0

    def __init__(self, name):
        self.name = name 
        Student.counter += 1 

    @classmethod 
    def get_total_students(cls):
        return cls.counter 
    

    def display_info(self):
        print(f"Name is {self.name}")


student1 = Student("A")
student2 = Student("B")     

print(Student.get_total_students())
Student.display_info(student1)
student2.display_info()