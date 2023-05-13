class Dog:
    def __init__(self, name, breed, age) -> None:
        self.name = name
        self.breed = breed
        self.age = age

    def info(self):
        print(f'Имя: {self.name}, порода: {self.breed}, возраст: {self.age}')


dog1 = Dog("Шарик", "овчарка", 5)
dog1.info()
