class Car:
    # Public variable
    brand1 = "Toyota"
    brand2 = "Mercedes"

    # Public method
    def start(self):
        print(f"The {self.brand1} car has started!")
        print(f"The {self.brand2} car has started!")

# Instantiate the class
my_car = Car()

# Access public variable
print(my_car.brand1)
print(my_car.brand2)

# Access public method
my_car.start()