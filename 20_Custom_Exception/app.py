# Define a custom exception
class InvalidAgeError(Exception):
    pass

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Access granted. Age is valid.")

# Test the function with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid number.")