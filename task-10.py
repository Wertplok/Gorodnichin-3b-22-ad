class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}')


man = Person("Alex", 25)
man.info()
