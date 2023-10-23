''''
def student(x):
    print(x)

name = input("Enter the students name")
student(name)
'''



'''
def student(student_id, student_name, student_class):
    print(student_id)
    print(student_name) 
    print(student_class) 

id = int(input("Enter the student's id number "))
name = input("Enter the students name ")
studentClass = input("Enter the students class ")

student(id, name, studentClass)
'''
'''
class Student:
    pass
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)
'''
'''
class Student:
    pass

class Marks:
    pass

student1 = Student()
mark1 = Marks()

print(isinstance(student1, Student))
print(isinstance(student1, Marks))
print(isinstance(mark1, Marks))
print(isinstance(mark1, Student))

print(issubclass(Student, object))
print(issubclass(Marks, object ))
'''

'''
class Student:
    student_name = "John Brooke"
    marks = 96
print(f"Student name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Barry Ballon')
setattr(Student, 'marks', 100)
print(f"Student name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
'''

'''
class Student:
    student_id = "01"
    student_name = "John Cole"
print("Orginal Values: ")
print(f"Student ID: {getattr(Student, 'student_id')}")
print(f"Student name: {getattr(Student, 'student_name')}")
print("After adding student class: ")
Student.student_class = "Class B"
print(f"Student ID: {getattr(Student, 'student_id')}")
print(f"Student name: {getattr(Student, 'student_name')}")
print(f"Student class: {getattr(Student, 'student_class')}")
print("After removing student name: ")
del Student.student_name
print(f"Student ID: {getattr(Student, 'student_id')}")
print(f"Student class: {getattr(Student, 'student_class')}")
'''

'''
class Student:
    student_id = "01"
    student_name = "Harry Wilson"

    def displayAll():
        print(f"Student ID: {Student.student_id}, Student Name: {Student.student_name}")
print("Displaying all attributes and their values: ")
Student.displayAll()
'''

class Student:
    student_name = "John Brooke"
    marks = 96

m2201995 = Student()

print(f"Student name: {m2201995.student_name}")
print(f"Marks: {m2201995.marks}")

m2201995.student_name = "Barry Ballon"
m2201995.marks = 100


print(f"Student name: {m2201995.student_name}")
print(f"Marks: {m2201995.marks}")