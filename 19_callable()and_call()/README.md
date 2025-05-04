# `callable()` and `__call__()` in Python

In Python, objects are typically not callable by default. However, using the `__call__()` method, we can make an object behave like a function. Additionally, the built-in `callable()` function allows us to check if an object can be called like a function.

---

## ✅ Key Concepts

1. **`callable(object)`**:

   * This built-in function checks if an object can be called like a function.
   * It returns `True` if the object appears callable (i.e., has a `__call__()` method), and `False` otherwise.

2. **`__call__()`**:

   * The `__call__()` method is a special method that allows an instance of a class to be called as if it were a regular function.
   * By implementing this method in a class, objects of that class become callable.

---

## 💡 Example Summary

We created a class `Multiplier` with:

* A constructor (`__init__()`) to initialize the multiplying factor.
* A `__call__()` method that multiplies a given value by the factor, making the object callable like a function.

---

## 🚀 Benefits

* **Function-like Objects**: Making objects callable allows them to behave more flexibly and like functions.
* **Useful in Advanced Design Patterns**: The `__call__()` method is useful for scenarios such as decorators, callable configurations, and more advanced programming techniques.

---

With `callable()` and `__call__()`, Python enables greater flexibility in how you design your classes and interact with objects, making them more function-like and adaptable to different use cases.
