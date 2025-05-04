# 5) Static Methods in Python

## 📌 What is a Static Method?

A **static method** is a method that:

* Does **not access** or **modify** class (`cls`) or instance (`self`) data.
* Belongs to the **class**, but doesn’t require `self` or `cls` as a parameter.
* Is used when the method’s logic is **independent** of class or object state.

---

## How It Works in Our Assignment

In the assignment:

* We created a class `MathUtils`.
* Inside the class, we defined a static method `add(a, b)` that returns the **sum** of two numbers.
* Since this method doesn’t depend on any class or object attributes, it is marked with the `@staticmethod` decorator.

---

## 🔍 Key Features

* ✅ **No object creation required** to use a static method.
* ✅ Ideal for **utility** or **helper functions** that logically belong to the class but don’t need to access its data.

---

Static methods improve code organization and encapsulation for operations that are logically related to a class but don't require class or instance context.
