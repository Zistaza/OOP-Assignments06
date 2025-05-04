# Custom Class Iterable in Python

---
In Python, to make a custom class iterable, you need to implement two special methods:

* **`__iter__()`**: This method returns the iterator object itself, usually `self`.
* **`__next__()`**: This method returns the next value in the iteration and moves the iterator forward. It raises a `StopIteration` exception when the iteration is complete.

### **Class**: `Countdown(start)`

The purpose of the `Countdown` class is to allow counting down from a given start number down to 0 using a loop.

### **How It Works**:

1. **Initialization (`__init__`)**:

   * The class is initialized with a starting number.

2. **Iterator Method (`__iter__`)**:

   * The method returns the object itself as the iterator.

3. **Next Method (`__next__`)**:

   * The method returns the current number and decrements it for the next iteration. When the countdown finishes, the method raises a `StopIteration` exception.

---

## 💡 Key Benefits of Custom Iterables

* **Control Over Iteration**: Custom iterables give you control over how an object is iterated, allowing for specialized iteration logic.

* **Seamless Integration**: By defining `__iter__()` and `__next__()`, your custom class can be used directly in Python's iteration-based constructs like `for` loops.

---

Creating a custom iterable class lets you define exactly how an object should be iterated over, which can enhance the flexibility and functionality of your code.
