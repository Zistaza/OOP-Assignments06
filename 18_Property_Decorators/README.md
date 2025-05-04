# Property Decorators in Python (@property, @setter, @deleter)

Property decorators in Python provide a way to control access to instance variables. With `@property`, `@<property>.setter`, and `@<property>.deleter`, you can define custom behavior when getting, setting, or deleting an attribute, while making it appear as though you’re interacting with regular attributes.

---

## ✅ Explanation

In this example, we create a `Product` class with a private attribute `_price`. We use property decorators to manage access to this attribute.

### Key Details:

1. **@property**:

   * Allows you to access `_price` like a normal attribute (`item.price`), rather than calling a method (`item.get_price()`).
   * This enhances readability and maintains a clean interface.

2. **@price.setter**:

   * This decorator allows you to control the modification of `_price` by adding validation logic (e.g., ensuring that the price is positive).
   * It ensures that the data is only modified in an acceptable way.

3. **@price.deleter**:

   * Provides a way to delete the `_price` attribute.
   * When the attribute is deleted, you can also display a custom message or perform additional cleanup.

---

## 📌 Why Use Property Decorators?

* **Data Protection**: Protects sensitive data inside a class by controlling how attributes are accessed or modified.
* **Controlled Access**: Ensures that reading, writing, and deletion of an attribute follows certain rules or logic.
* **Cleaner Code**: Provides a Pythonic approach, making the code cleaner and more intuitive by allowing attribute-like access, while still having the benefits of method functionality.

---

By using property decorators, you can enhance the flexibility and security of your classes while keeping them easy to use and maintain.
