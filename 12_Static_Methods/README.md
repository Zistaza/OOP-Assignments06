# Static Methods in Python

---

A **static method** in Python belongs to the class but does not access any class-level (`cls`) or instance-level (`self`) variables. It functions like a regular function, but it is grouped inside the class for logical organization. Static methods are useful when you need a utility function that logically belongs to the class but does not rely on class or instance-specific data.

---

## ✅ Key Concepts

* **Declaration**:
  Static methods are declared using the `@staticmethod` decorator.

* **Calling**:
  A static method can be called directly on the class itself, without needing to create an instance of the class.
  Example: `TemperatureConverter.celsius_to_fahrenheit(25)`

* **No Instance or Class Dependency**:
  Static methods do not rely on instance data (`self`) or class-level data (`cls`). They act like standalone functions but are logically associated with the class.

* **Ideal for Utility Functions**:
  Static methods are best used for utility or helper functions that are related to the class but don't require access to class or instance attributes.

---

## 🧪 Example Use Case

In our example, we created a `TemperatureConverter` class with:

* A **static method** `celsius_to_fahrenheit(c)` that converts temperature from Celsius to Fahrenheit using the formula:
  `Fahrenheit = (Celsius × 9/5) + 32`

This allows us to convert temperatures without needing to create an object of the `TemperatureConverter` class, making the code more concise and logically organized.

---

Static methods provide a clean way to include utility functions within a class while avoiding the overhead of creating class instances when not needed.
