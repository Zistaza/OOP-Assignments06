class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be positive.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# Example usage
item = Product(150)
print("Initial Price:", item.price)

item.price = 200
print("Updated Price:", item.price)

del item.price