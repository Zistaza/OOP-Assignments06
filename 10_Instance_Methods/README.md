# Instance Methods in Python

---
In Python, **instance methods** are functions defined within a class that operate on instances (objects) of that class. These methods can **access and modify instance variables**, making them essential for most object-oriented programming use cases.

---

## ✅ Key Concepts

* **`self` Parameter**:
  Every instance method must take `self` as its first parameter. It refers to the specific object calling the method, allowing access to the object’s attributes and other methods.

* **Instance Variables**:
  These are defined inside the `__init__()` constructor and represent the **data unique to each object**. Instance methods often modify or retrieve these variables.

* **Functionality**:
  Instance methods typically perform tasks such as updating object attributes, computing values based on current object state, or printing relevant information.

---
##  Example Summary

* A class named `Dog` is created with two instance variables: `name` and `breed`, representing the dog's details.
* An instance method called `bark()` is defined to **print a message** including the dog’s name.
* When an object like `my_dog` calls `my_dog.bark()`, the method uses `self.name` to generate a personalized message.
---
Instance methods are the core of object behavior in Python, enabling dynamic interaction with each object’s data and providing encapsulated functionality.
