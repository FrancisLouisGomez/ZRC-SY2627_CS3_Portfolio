# Write a short Python code snippet showing a Course adding a Student object to a list. 
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


course = Course("Computer Science")

student1 = Student("Francis", "2026-001")
student2 = Student("Alex", "2026-002")

course.add_student(student1)
course.add_student(student2)

print("Course:", course.name)

for student in course.students:
    print("Student:", student.name, "| ID:", student.student_id)