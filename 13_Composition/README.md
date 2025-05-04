# Composition in Python

---
**Composition** is a design principle in object-oriented programming where one class contains an object of another class. Unlike inheritance, which represents an "is-a" relationship, composition represents a "has-a" relationship, where one class "owns" another class and utilizes its functionality. Composition allows you to build more complex functionality by combining simpler classes, providing flexibility and modularity.

---

## ✅ Key Concepts

* **Has-a Relationship**:
  Composition models the relationship between classes where one class contains objects of another. For example, a `Car` has an `Engine`. This allows for more flexible and modular designs.

* **Combination of Simpler Classes**:
  Instead of relying on inheritance to extend behavior, composition enables you to combine multiple classes to create complex functionality.

* **Class Containment**:
  A class can contain an object of another class as an attribute. This allows you to use the contained class's methods and properties without using inheritance.

---

## 🧪 Example Use Case

In this assignment, we demonstrated composition through the following:

* **Engine class**:
  Contains a method `start()` that prints a message indicating the engine is starting.

* **Car class**:
  Accepts an `Engine` object through its constructor and stores it as an instance variable. The `Car` class uses the `Engine` class's `start()` method to simulate starting the car's engine.

---

### 📌 Summary of the Composition Example:

* The **Car** class **has-a** **Engine**.
* The **Engine** class has a `start()` method.
* The **Car** class uses the **Engine** class's `start()` method to start the engine, demonstrating the power of composition.

This example highlights how one class can utilize the functionality of another by including it as an attribute, rather than inheriting from it.

---

Composition promotes code reuse and flexibility, allowing for the creation of more complex behaviors by combining simpler, independent classes.
