try:
    a, b = map(float, [input(f"Введите {i}: ") for i in ("делимое", "делитель")])
    print(f"Результат: {a / b}")
except Exception:
    print("Ошибка")
