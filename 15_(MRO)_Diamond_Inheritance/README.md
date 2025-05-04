# Method Resolution Order (MRO) and Diamond Inheritance in Python

---
### Method Resolution Order (MRO)

* **MRO** determines the order in which methods are searched in a class hierarchy, particularly in multiple inheritance scenarios. It ensures that the correct method is called when multiple classes inherit from the same base class.

### Diamond Inheritance

* **Diamond Inheritance** occurs when a class inherits from two classes, both of which inherit from a common base class, forming a diamond-shaped structure. MRO resolves potential method conflicts in this structure by providing a well-defined method lookup order.

---

## ✅ Assignment Explanation

In this assignment, we created four classes:

* **Class A**: Defines the method `show()`.
* **Class B** and **Class C**: Inherit from `A` and override the `show()` method.
* **Class D**: Inherits from both `B` and `C`.

### MRO in Action:

* When an object of `D` calls the `show()` method, Python uses the **Method Resolution Order** (MRO) to determine which method to invoke.
* In our example, since `D` inherits from `B` first, the `show()` method from class `B` will be called.

---

## 🔍 Key Points

* **The `__mro__` attribute**:
  The `__mro__` attribute of a class provides the MRO, showing the order in which Python looks for methods in the class hierarchy.

* **Predictable Order**:
  MRO ensures that methods are called in a predictable order, avoiding conflicts that arise in cases of diamond inheritance.

* **MRO in Multiple Inheritance**:
  In cases of multiple inheritance, MRO helps avoid ambiguity, ensuring that the correct method is called from the appropriate class.

---

## 📌 Conclusion

* **MRO** is a vital mechanism in multiple inheritance, ensuring that method resolution is unambiguous and predictable.
* **Diamond inheritance** is resolved by MRO, ensuring that methods are executed from the correct class according to the class hierarchy.

---

By understanding MRO, we can confidently work with complex inheritance structures and avoid method conflicts in multiple inheritance scenarios.
