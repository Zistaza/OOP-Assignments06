class Book:
    # Class variable to count total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment count each time a new book is added
        Book.increment_book_count()

    # Class method to increment the book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    # Method to show total books
    @classmethod
    def show_total_books(cls):
        print(f"Total books: {cls.total_books}")


# Create multiple book objects
book1 = Book("Python Basics")
book2 = Book("OOP in Python")
book3 = Book("Advanced Python")

# Show total books
Book.show_total_books()