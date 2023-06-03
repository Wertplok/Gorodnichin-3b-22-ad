from collections import Counter


try:
    with open(input("Введите имя файла: ")) as file:
        print(Counter(file.read().replace("\n", "").split()).most_common(1)[0][0])
except FileNotFoundError:
    print("Ошибка: файл не найден")
