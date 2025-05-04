# Access Modifiers in Python (Public, Protected, Private)

In Python, **access modifiers** control the visibility and accessibility of class members (attributes and methods). Python uses naming conventions rather than enforced access restrictions, but they help guide proper usage.

---

## 🔓 1. Public Members

* **Syntax**: `self.name`
* **Access**: Can be accessed from anywhere — inside or outside the class.
* **Use Case**: Use when data should be easily accessible and modifiable.

---

## 🛡️ 2. Protected Members

* **Syntax**: `self._salary`
* **Access**: Intended to be accessed within the class and its subclasses.
* **Convention**: A single underscore `_` indicates the member is protected.
* **Note**: Still technically accessible from outside the class, but usage is discouraged to preserve encapsulation.

---

## 🔐 3. Private Members

* **Syntax**: `self.__ssn`
* **Access**: Only accessible within the class where it's defined.
* **Mechanism**: Python uses **name mangling**, renaming `__ssn` internally to `_ClassName__ssn`.
* **Access Outside the Class**: Possible via:

  * Getter and setter methods (e.g., `get_ssn()`)
  * Name mangling (e.g., `object._ClassName__ssn`) — **not recommended**
---

## Assignment Outcome

In the assignment example:

* A `Manager` class was created that inherits from `Employee`.
* The following members were used:

  * Public variable: `name`
  * Protected variable: `_salary`
  * Private variable: `__ssn`
* Demonstrated concepts:

  * Safe access to private data using **getter and setter** methods.
  * Use of **name mangling** to access private variables externally (not best practice).
  * **Protected members** are accessible in subclasses.
  * **Private members** raise an error when accessed directly outside the class.

Access modifiers in Python are a vital part of writing clean, maintainable, and secure object-oriented code.
