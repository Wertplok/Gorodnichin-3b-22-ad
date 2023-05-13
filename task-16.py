class Cat:
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color


    def info(self):
        print(f"кошка по имени {self.name}, {self.age} лет, цвет {self.color}")


Cat1 = Cat("Мурка", 5, "черный")
Cat1.info()
