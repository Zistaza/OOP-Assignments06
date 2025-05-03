class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public
        self._salary = salary      # Protected (convention)
        self.__ssn = ssn           # Private

#now 
# Working with Employee directly
emp = Employee("Ayesha", 60000, "123-45-6789")

# Public variable
print("Public Name:", emp.name)

# Protected variable (accessible, but discouraged)
print("Protected Salary:", emp._salary)

# Private variable (direct access will fail)
try:
    print("Private SSN:", emp.__ssn)
except AttributeError:
    print("Private SSN: ❌ Cannot access directly!")

# Accessing private variable using name mangling
print("Private SSN via Mangling (Employee):", emp._Employee__ssn)