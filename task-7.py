def sum_(a, b):
    return a + b

print("Сумма чисел равна", sum_(*map(int, input("Введите два числа через пробел: ").split())))
