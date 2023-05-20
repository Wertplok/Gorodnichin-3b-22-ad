class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def viev(self):
        print(f"Сотрудник по имени {self.name}, {self.age} лет, получает {self.salary}")


man1 = Employee("Иван", 30, 150000)
man1.viev()
