from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # Abstract method (no implementation here)

# Subclass that inherits and implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating an instance of Rectangle and using it
rect = Rectangle(5, 15)
print("Area of rectangle:", rect.area())