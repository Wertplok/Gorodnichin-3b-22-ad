try:
    n = int(input("Введите целое число: "))
    print(f"Сумма целых чисел от 1 до {n}: {(sum(range(abs(n) + 1)) - (n < 0)) * (1, -1)[n < 0]}")
except ValueError:
    print("Неверный формат числа")
