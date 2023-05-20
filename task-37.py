# from random import randint


# print(numb_list := [randint(1, 100) for _ in range(15)])

numb_list = list(map(int, input("Введите список целых чисел через пробел: ").split()))
print("Два наименьших значения: ", ', '.join(map(str, sorted(numb_list)[:2])))
