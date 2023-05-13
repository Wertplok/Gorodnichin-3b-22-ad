class Book:
    def __init__(self, title, author, publication_year, genre) -> None:
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def info(self):
        print(f"{self.title}, {self.author} ({self.publication_year}), {self.genre}")


Book1 = Book("Война и мир", "Л.Н. Толстой", 1867, "роман")
Book1.info()
