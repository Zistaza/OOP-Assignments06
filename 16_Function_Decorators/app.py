# Simple decorator to log function calls
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Apply the decorator to say_hello function
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()