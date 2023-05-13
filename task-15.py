class Car:
    def __init__(self, brand, model, manufacture_year, price) -> None:
        self.brand = brand
        self.model = model
        self.manufacture_year = manufacture_year
        self.price = price

    def info(self):
        print(f"{self.brand} - {self.model}, {self.manufacture_year}, {self.price}")


car1 = Car("ВАЗ", "2109", 2000, 300_000)
car1.info()
