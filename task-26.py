def lcm(a, b):
    m = a * b
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


a = int(input("a = "))
b = int(input("b = "))
print(f"Наименьший общий множитель: {lcm(a, b)}")


# import math

# print(math.lcm(a, b))
