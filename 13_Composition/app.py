class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine is part of Car

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Access Engine's method via Car

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car class
my_car = Car(my_engine)

# Use Car to start the engine
my_car.start_car()