class School_student:
    def __init__(self, name, school_class) -> None:
        self.name = name
        self.school_class = school_class

    def learn(self):
        print(f"Школьник {self.name} учится")


child1 = School_student("Иван", 5)
child1.learn()
