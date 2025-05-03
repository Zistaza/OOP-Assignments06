class Logger:
    def __init__(self):
        print("🟢 Logger object created. (Constructor)")

    def __del__(self):
        print("🔴 Logger object destroyed. (Destructor)")

# Create an object
log = Logger()

# Optionally delete the object manually
del log