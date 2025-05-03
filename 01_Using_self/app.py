class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print("-" * 20)

# Creating multiple student objects
student1 = Student("Alice", 88)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 92)

# Display details for all students
student1.display()
student2.display()
student3.display()