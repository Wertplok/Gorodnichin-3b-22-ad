from random import randint


my_list = [randint(0, 100) for _ in range(10)]

print(f"Массив {my_list = }")
print(f"Max = {max(my_list)}")
print(f"Min = {min(my_list)}")
