from random import randint


my_list = [randint(1, 10) for _ in range(5)]
print(f"Сумма чисел массива {my_list} равна {sum(my_list)}")
