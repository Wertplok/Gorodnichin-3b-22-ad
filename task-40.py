import os


files = os.listdir('.')
print(f"Файл {('не найден', 'существует')['test.txt' in files]}")
