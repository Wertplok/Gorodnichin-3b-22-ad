from random import randint


my_list = [randint(1, 10) for _ in range(5)]
# print(f"Массив {my_list = }")
number = int(input("Введите целое число: "))
print(f"Число {number} {('не ', '')[number in my_list]}найдено в массиве")
