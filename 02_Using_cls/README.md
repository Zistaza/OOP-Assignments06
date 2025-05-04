# Understanding Class Methods and `cls` in Python

In Python, **class methods** are methods that are bound to the class, not the instance. These methods use the `cls` parameter to refer to the class itself, much like `self` is used in instance methods.

---

## 🔑 Key Points about Class Methods

* Defined using the `@classmethod` decorator.
* The first parameter is `cls`, which refers to the class.
* Can access or modify class-level data (class variables).
* Can be called on the class or on any instance of it.
* Useful when working with data shared across all instances.

---

## 🤔 Why Use `cls`?

* `cls` allows access to **class-level data** and methods.
* It is essential when defining **class-level behavior** that is the same for every object.
* Similar to how `self` refers to the instance, `cls` refers to the class.

---

## 🔍 Key Differences: Instance Methods vs. Class Methods

| **Instance Method**                           | **Class Method**                                  |
| --------------------------------------------- | ------------------------------------------------- |
| Defined without the `@classmethod` decorator. | Defined with the `@classmethod` decorator.        |
| Takes `self` as the first parameter.          | Takes `cls` as the first parameter.               |
| Works with instance data (unique per object). | Works with class data (shared among all objects). |
| Called on an instance of the class.           | Called on the class itself or any instance.       |

---
