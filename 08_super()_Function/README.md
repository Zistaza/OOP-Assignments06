# The `super()` Function in Python
The `super()` function in Python is used to call methods from a **parent class**, typically the constructor (`__init__`). It is especially useful in **inheritance** when a child class wants to **reuse or extend** functionality from its parent class without rewriting code.

## ✅ Why Use `super()`?

* Promotes **cleaner and more maintainable code**.
* Prevents **code duplication** in child classes.
* Ensures **proper initialization** of attributes defined in the parent class.

## 🔍 Key Takeaways

* `super()` guarantees that the **parent class is properly initialized**.
* It allows access to **any method** in the parent class, not just `__init__`.
* Works effectively in both **single and multiple inheritance** scenarios.
---
Using `super()` is a best practice when working with inheritance, ensuring better code organization and reducing redundancy.
