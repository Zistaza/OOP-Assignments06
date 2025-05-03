class Dog:
    def __init__(self, name, breed):
        self.name = name   # Instance variable
        self.breed = breed # Instance variable

    def bark(self):
        print(f"{self.name} says Woof! Woof!")

# Create an instance of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Call the bark method
my_dog.bark()  # Outputs: Buddy says Woof! Woof!