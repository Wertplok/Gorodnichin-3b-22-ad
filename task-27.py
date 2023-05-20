from random import randint


my_list = [randint(1, 100) for _ in range(15)]
# print(f"Массив {my_list = }")
for i in my_list:
    if not i % 2:
        print(i)

# print(*filter(lambda x: x % 2 == 0, my_list))
