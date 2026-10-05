from dataclasses import dataclass

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
