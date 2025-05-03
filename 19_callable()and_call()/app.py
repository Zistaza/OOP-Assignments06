class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an object of Multiplier
times_three = Multiplier(3)

# Check if the object is callable
print("Is object callable?", callable(times_three))  # True

# Call the object like a function
result = times_three(10)  # Multiplies 10 by 3
print("Result:", result)