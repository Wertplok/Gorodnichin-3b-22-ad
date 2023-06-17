# Задание:
# Написать программу, которая принимает на вход строку
# и выводит на экран количество различных подстрок строки,
# начинающихся и заканчивающихся одним и тем же символом.


input_str = input("Введите строку: ") # запрашиваем ввод строки

substrings = set() # создаем пустое множество подстрок

for l in set(input_str): # выполняем цикл для каждого из множества уникальных символов в строке
    start = input_str.index(l) # устанавливаем индекс начала подстроки на индекс первого вхождения символа в строку
    end = input_str.rindex(l) # устанавливаем индекс конца подстроки на индекс последнего вхождения символа в строку

    while start < end: # выполняем цикл пока индекс начала подстроки не превышает индекса конца подстроки

        while start < end:
            # добавляем подстроку между индексами в множество подстрок
            substrings.add(input_str[start:end + 1])

            # устанавливаем индекс конца подстроки на последнее вхождение символа в подстроку
            end = input_str.rindex(l, start, end)

        # возвращаем индекс конца подстроки на индекс последнего вхождения символа в строку
        end = input_str.rindex(l)
        try:
            # пытаемся установить индекс начала подстроки на индекс второго но не последнего вхождения символа в строку
            start = input_str.index(l, start + 1, end)
        except ValueError:
            # в случае если второе вхождение символа в строку является последним - прерываем цикл,
            # переходим к следующему символу из множества уникальных символов
            break

print(len(substrings)) # выводим на экран количество элементов в множестве подстрок
