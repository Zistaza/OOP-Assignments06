class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of Person
        self.subject = subject
        print(f"Teacher created. Subject: {self.subject}")

# Create an instance of Teacher
t = Teacher("Miss Sarah", "International Relations")