def is_prime(num):
    return num >= 2 and all(num % i for i in range(2, int(num**0.5) + 1))

number = int(input("Введите целое число: "))
print(f"{number} - {('не ','')[is_prime(number)]}простое число")
