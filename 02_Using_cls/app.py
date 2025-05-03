class Counter:
    # Class variable to keep track of the count
    count = 0

    def __init__(self):
        # Increment the count each time an object is created
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        # Class method to display the current count of objects created
        print(f"Total objects created: {cls.count}")


# Creating multiple objects of the Counter class
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
counter5 = Counter()
counter6 = Counter()

# Display the count using the class method
Counter.display_counter()