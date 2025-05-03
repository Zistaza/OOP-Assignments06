# Class Decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the class decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of the Person class
person1 = Person("Sarah")

# Access the greet method added by the decorator
print(person1.greet()) 