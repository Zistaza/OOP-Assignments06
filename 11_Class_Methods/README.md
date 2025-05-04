# Class Methods in Python

In Python, **class methods** are methods that are bound to the **class** itself rather than to instances (objects) of the class. These methods are defined with the `@classmethod` decorator and can access or modify **class-level variables**.

---

## 🧠 Key Concepts

* **`cls` Parameter**:
  The first parameter of a class method is `cls`, which refers to the class itself (similar to how `self` refers to an instance).

* **Class-Level Variables**:
  Class methods are ideal for manipulating class variables, which are shared across all instances of the class.

* **Usage**:
  Class methods can be called on both the **class** itself or any **object instance** of the class. However, they always interact with class-level data, not instance-specific data.

---

## 🧪 Example Use Case

In our example, we created a `Book` class with:

* A **class variable** `total_books` to track how many books have been created.
* A **class method** `increment_book_count()` that increases the `total_books` count each time a new book is instantiated.
* Another **class method** `show_total_books()` to display the current count of books.

This setup helps in scenarios where we want to keep track of the number of class instances without relying on each individual object to do so.
---
Class methods are powerful tools for managing class-level state and ensuring that the behavior of the class is consistent across all instances.
