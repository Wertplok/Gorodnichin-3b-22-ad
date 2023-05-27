try:
    with open(input("Введите имя файла: ")) as file:
        print(file.read())
except Exception:
    print("Ошибка")
