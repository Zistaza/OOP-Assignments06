# Abstract Classes and Methods in Python

In Python, **abstract classes** are classes that cannot be instantiated directly. They are designed to be **inherited** by other classes and often contain **abstract methods**—methods that are declared but lack implementation. Abstract classes help enforce a **structure or contract** for subclasses.

---

##  Key Concepts

* Abstract classes are created using Python’s built-in **`abc` module**, specifically using `ABC` and the `@abstractmethod` decorator.
* They act as **blueprints** for future derived classes.
* If a class contains at least **one abstract method**, it becomes abstract and **cannot be instantiated**.
* All **subclasses must implement** the abstract methods, or they too will be treated as abstract classes.

---

##  Example Summary

* An abstract class `Shape` defines an abstract method `area()` without any implementation.
* A subclass `Rectangle` inherits from `Shape` and provides its own implementation of the `area()` method.
* This structure ensures **every subclass of `Shape` will have a working `area()` method**, enforcing a consistent interface across all shape types.

---
Abstract classes are especially useful in large-scale applications where you want to define a standard interface across multiple derived classes.
