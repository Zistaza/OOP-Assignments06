# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

# Department class
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to existing Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()

# Create an Employee object (exists independently)
emp1 = Employee("Zawar")

# Create a Department object and associate the existing employee
dept1 = Department("HR", emp1)

# Display details
dept1.show_details()