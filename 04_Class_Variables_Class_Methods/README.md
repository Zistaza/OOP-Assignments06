# Class Variables and Class Methods in Python

## 📘 Objective

Understand how to use **class variables** and **class methods** in Python to **share and update values** across all instances of a class.

---

## ✅ Explanation

In Python:

* A **class variable** is a variable that is shared among **all instances** of a class. It belongs to the **class itself**, not any one object.
* A **class method** is defined using the `@classmethod` decorator and takes `cls` (referring to the class) as its first parameter. It is used to **access or modify** class-level data.

---

## 🛠️ Key Concepts

### 🔹 Class Variable

A variable defined **inside the class**, but **outside of any instance method**.
✅ Shared by **all objects** of that class.

### 🔹 Class Method

A method defined using the `@classmethod` decorator.
✅ Takes `cls` as the first parameter and can **access or update** class variables.

### 🔹 Effect on Instances

When a class variable is updated via a class method:
✅ The change is **reflected across all instances**, existing or new.

---

## 📌 Summary

| **Term**        | **Description**                                                     |
| --------------- | ------------------------------------------------------------------- |
| Class Variable  | A variable shared across all instances of a class.                  |
| Class Method    | A method that modifies or accesses class-level data using `cls`.    |
| Shared Behavior | Changing the class variable affects **all instances** of the class. |

---
