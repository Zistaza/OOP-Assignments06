class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Diamond inheritance
    pass

# Create object of class D
obj = D()
obj.show()

# Print the Method Resolution Order
print(D.__mro__)