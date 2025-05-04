# Custom Exception in Python

In Python, custom exceptions allow you to define specific error types that can provide clearer and more controlled error handling in your applications. By creating your own exceptions, you can tailor the error messages to suit the needs of your program.

---

## ✅ Key Concepts

* **Custom Exception Class**:

  * A custom exception is created by extending the built-in `Exception` class.
  * Example: `class InvalidAgeError(Exception):` defines a custom exception called `InvalidAgeError`.

* **`raise`**:

  * The `raise` keyword is used to trigger or throw the custom exception when a specific condition is met.

* **`try...except` Block**:

  * The `try...except` structure is used to catch and handle exceptions gracefully, preventing the program from crashing.

---

## 💡 Example Summary

* **User Age Input**:

  * The program prompts the user to input their age.
* **Custom Exception**:

  * If the age entered is less than 18, it raises a custom exception, `InvalidAgeError`, with a relevant error message.
* **Valid Age**:

  * If the input age is valid and greater than or equal to 18, the program prints a success message.
* **Handling Non-integer Inputs**:

  * The program handles invalid input types, such as non-integer values, using a `ValueError`.

---

## 🚀 Benefits

* **Clear Error Handling**: Custom exceptions provide a way to define and manage specific errors in your program, making it easier to debug and maintain.

* **Improved User Experience**: By defining custom error messages, users can receive more meaningful feedback when an error occurs.

---

Creating and using custom exceptions helps in building more robust and maintainable error-handling strategies tailored to the specific needs of your Python applications.
