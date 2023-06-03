import os


try:
    dirertory = input("Введите директорию для поиска (по умолчанию - текущая): ")
    file_type = "." + input("Введите расширение: .")
    files_in_dir = os.listdir(path=dirertory or '.')
    found_files = tuple(filter(lambda s: s.endswith(file_type), files_in_dir))
    print(f"Найдено файлов - {len(found_files)}:" if found_files else "Файлы не найдены")
    [print(i) for i in found_files]
except FileNotFoundError:
    print("Директория не найдена")
except NotADirectoryError:
    print("Указанный путь не является директорией")
