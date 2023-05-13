class BankAccount:
    def __init__(self, acc_name, acc_number, acc_balance=0) -> None:
        self.__acc_name = acc_name
        self.__acc_number = acc_number
        self.__acc_balance = acc_balance

    def deposit(self, amount):
        self.__acc_balance+=amount
        print(f"Пополнено на: {amount}, доступно: {self.__acc_balance}")

    def withdraw(self, amount):
        self.__acc_balance-=amount
        print(f"Снято: {amount}, остаток: {self.__acc_balance}")


wallet=BankAccount("Иван", 12345, 1_000_000)
wallet.deposit(1000)
wallet.withdraw(100_000)
