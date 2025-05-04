# Aggregation in Python

**Aggregation** is a type of relationship in object-oriented programming where one class holds a reference to another class, but both classes can exist independently. Unlike composition, where the contained object cannot exist without the container, aggregation represents a "has-a" relationship with **loose coupling**.

---

## ✅ Key Concepts

* **Loose Coupling**:
  Aggregation allows the contained object to exist independently of the containing class, ensuring that changes to the container do not force changes to the contained object.

* **Has-a Relationship**:
  Similar to composition, aggregation shows a "has-a" relationship between classes. However, in aggregation, the contained object (the referenced object) can exist before and after the containing object.

* **Independence of Objects**:
  The contained object does not depend on the container class for its existence. The container class only holds a reference to the object.

---

## 🧪 Example Use Case

In this example, we demonstrate aggregation using two classes: **Employee** and **Department**.

### Example Breakdown:

* **Employee class**:
  Defines an employee with a `name` attribute.

* **Department class**:
  Uses an `Employee` object, but does not create it. The `Employee` object exists independently and can be shared by multiple departments, showing the **loose coupling** nature of aggregation.

### 📌 Summary of Aggregation Example:

* The **Department** class **has-a** **Employee**, but the **Employee** object is created and managed independently.
* The **Employee** object can exist outside of the **Department** class, demonstrating that they are loosely coupled.
* The **Department** class simply holds a reference to the **Employee** object, without owning or controlling it.

---

Aggregation is useful when you want to establish relationships between classes, but maintain the independence and reusability of the contained objects.
