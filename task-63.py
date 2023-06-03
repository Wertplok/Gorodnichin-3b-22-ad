class NonnegativeProperty:
    def __set_name__(self, owner, name):
        self.name = name
        self.type = owner.__init__.__annotations__[name]

    def __get__(self, instance, owner):
        return getattr(instance, f"_{self.name}")

    def __set__(self, instance, value):
        if type(value) is not self.type and not(type(value) is int and self.type is float):
            raise TypeError(f"{self.name} must be {self.type.__name__}")
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        setattr(instance, f"_{self.name}", value)


class ProductCard:
    price = NonnegativeProperty()
    quantity = NonnegativeProperty()

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_quantity(self, decrease_value: int) -> None:
        self.quantity -= decrease_value

    def price_change(self, new_price: float) -> None:
        self.price = new_price


# test
def test():
    try:
        pc = ProductCard("product", -100, 10)
        print("Fail! An instance of a ProductCard can be created with negative price.")
    except ValueError:
        print("Success! An instance of a ProductCard can't be created with negative price.")

    try:
        pc = ProductCard("product", 100, -10)
        print("Fail! An instance of a ProductCard can be created with negative quantity.")
    except ValueError:
        print("Success! An instance of a ProductCard can't be created with negative quantity.")

    pc = ProductCard("product", 100, 10)

    try:
        pc.price_change(-1000)
        print("Fail! Price changed to a negative value.")
    except ValueError:
        print("Success! Price can't be changed to a negative value.")

    try:
        pc.decrease_quantity(11)
        print("Fail! Quantity changed to a negative value.")
    except ValueError:
        print("Success! Quantity can't be changed to a negative value.")

    try:
        pc.price_change("one million dollars")
        print("Fail! Price changed to a string value.")
    except TypeError:
        print("Success! Price can't be changed to a string value.")

    try:
        pc.decrease_quantity(0.5)
        print("Fail! Quantity changed to a fractional value.")
    except TypeError:
        print("Success! Quantity can't be changed to a fractional value.")

    pc.price_change(1000)
    if pc.price == 1000:
        print("Success! Price change to a positive value is working properly")
    else:
        print("Fail! Price change to a positive value is't working properly")

    pc = ProductCard("product", 100, 10)
    pc.decrease_quantity(6)
    if pc.quantity == 4:
        print("Success! Quantity decrease to a positive value is working properly")
    else:
        print("Fail! Quantity decrease to a positive value is't working properly")

test()
