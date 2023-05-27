try:
    with open("test.txt", "w") as text:
        text.write("Hello, world!")
except Exception:
    print("Ошибка")
