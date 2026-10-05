import json
from nested_data import Student

with open("data/students.json", "r") as file:
    students = json.load(file)

def validate_records(students):
    if not isinstance(students, list):
        return False
    if not students:
        return False
    for student_data in students:
        if not isinstance(student_data, dict):
            return False
        if "name" not in student_data:
            return False
        if type(student_data["name"]) != str:
            return False
        if "age" not in student_data:
            return False
        if type(student_data["age"]) != int or student_data["age"] <= 0:
            return False
        if "contact" not in student_data:
            return False
        if type(student_data["contact"]) != str:
            return False
        if "@" not in student_data["contact"] or ".com" not in student_data["contact"]:
            return False
    return True
                    
def find_student(student_objects, name):
    for student in student_objects:
        if student.name == name:
            return student
    return None

def filter_students(student_objects, attribute, value):
    matching_students = []
    for student in student_objects:
        if getattr(student, attribute) == value:
            matching_students.append(student)
    return matching_students

def report_students(student_objects):
    for student in student_objects:
        print(f"{student.name} - {student.age} - {student.contact}")

is_valid = validate_records(students)
if is_valid:
    student_objects = []
    for student_data in students:
        student = Student(student_data["name"], student_data["age"], student_data["contact"])
        student_objects.append(student)

    found_student = find_student(student_objects, "David")
    print(found_student)

    results = filter_students(student_objects, "age", 21)
    print(results)

    report_students(student_objects)
else:
    print("Invalid student data")


