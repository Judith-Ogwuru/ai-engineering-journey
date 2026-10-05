from dataclasses import dataclass
students = {"Python": [{"name": "Mary", "age": 20}, {"name": "Martha", "age": 22}],
"SQL": [{"name": "Agnes", "age": 21},{"name": "David", "age": 20}],
"Math": [{"name": "Emmanuel", "age": 25}, {"name": "Kyle", "age": 24}, {"name": "Dora", "age": 23}]}
students["Python"][0]["age"]
students["SQL"][1]["name"]
for course in students:
    for student in students[course]:
        print(student["name"])

print()

student_records = [{"name": "Mary", "age": 20, "course": "Python", "contact": {"email": "mary@example.com", "phone": "555-1234"}},
{"name": "Martha", "age": 22, "course": "Python"},
{"name": "Agnes", "age": 21, "course": "SQL"},
{"name": "David", "age": 20, "course": "SQL"}]
count = 0
for student in student_records:
    if student["course"] == "Python":
        count += 1
        print(student["name"])
print(count)
for student in student_records:
    if student["name"] == "Mary":
        print(student["contact"]["email"])

@dataclass
class Student:
    #def __init__(self, name, age, contact):
        #self.name = name
        #self.age = age
        #self.contact = contact
    name: str
    age: int
    contact: str
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.contact)


if __name__ == "__main__":
    student1 = Student("Mary", 20, "mary@example.com")
    student2 = Student("Martha", 22, "martha@example.com")
    student3 = Student("David", 20, "david@example.com")
    student1.name = "Maria"
    student1.age = 21
    print(student1.name)
    print(student2.name)
    print(student1.age)
    print(student1.contact)
    print(student3.name)
    print(student3.age)
    print(student3.contact)
    student1.display_info()
    student2.display_info()
    student3.display_info()

