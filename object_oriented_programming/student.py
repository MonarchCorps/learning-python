from datetime import datetime

class Student:
    
    class_year = datetime.now().year
    num_students = 0
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.num_students += 1
        
    def study(self):
        print(f"{self.name} is studying")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
