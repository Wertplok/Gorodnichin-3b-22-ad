operations = {"+":lambda x, y: x + y,
              "-":lambda x, y: x - y,
              "*":lambda x, y: x * y,
              "/":lambda x, y: x / y,}

cont = '0'

while cont != "Y":
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Введите операцию ('+', '-', '*', '/'): ")
        print(f"{a} {op} {b} = {operations[op](a, b)}")
    except ValueError:
        print("Неверный числовой формат")
        continue
    except ZeroDivisionError:
        print("Деление на ноль запрещено")
    except KeyError:
        print("Неверная операция")
    finally:
        cont = input("Для завершения работы введите 'Y': ")
