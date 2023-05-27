try:
    with open("test.txt") as text:
        print(text.read())
except FileNotFoundError:
    print("Файл не найден")
