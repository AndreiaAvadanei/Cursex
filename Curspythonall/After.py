'''class Dog:
    def __init__(self,name):
        self.name = name
        print(name)
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Rex")
d2 = Dog("Tasha") '''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        pass

s1 = Student("Dia", 20, 90)
s2 = Student("Inna", 20, 80)
s2 = Student("Jim", 20, 95)

course = Course("Management", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0.name)



