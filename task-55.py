try:
    num_list = tuple(map(int, input("Введите список целых чисел через запятую: ").split(",")))
    print(f"Минимальное число: {min(num_list)}")
except ValueError:
    print("Неверный формат числа")
