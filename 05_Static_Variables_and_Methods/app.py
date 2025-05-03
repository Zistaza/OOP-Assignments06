class MathUtils:
    @staticmethod
    def add(a, b):
        print(f"Adding numbers: {a} + {b}") #a and b are local parameters
        return a + b

# Call the static method directly
result = MathUtils.add(10, 5)
print("Sum:", result)