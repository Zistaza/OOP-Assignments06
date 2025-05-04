# Function Decorators in Python

---

Function decorators are a powerful feature in Python that allow us to modify the behavior of a function without altering its actual code. Decorators are commonly used to add functionality to functions in a clean and reusable manner.

---

## ✅ Explanation

In this example, we define a `log_function_call` decorator:

* **`log_function_call` decorator**: This decorator is designed to log a message before executing the `say_hello()` function. Specifically, it prints "Function is being called" before the function’s actual behavior.

### How it Works:

* The decorator wraps the `say_hello` function, effectively adding new behavior (logging) before the original functionality executes.

---

By using decorators, we can enhance existing functions in a modular way without modifying their core logic.
