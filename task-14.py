class Student:
    def __init__(self, name, surname, age, speciality) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.speciality = speciality

    def info(self):
        print(f"{self.name} - {self.surname}, {self.age} лет, {self.speciality}")


man = Student("Иван", "Иванов", 20, "программист")
man.info()
