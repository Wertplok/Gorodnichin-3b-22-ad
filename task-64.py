import time


class BankClient:
    def __init__(self, info, bank) -> None:
        self.info = info
        self.bank = bank


class BankAccount:
    def __init__(self, owner, bank) -> None:
        self.owner = owner
        self.bank = bank


class Bank:
    def __init__(self) -> None:
        self.__clients = {}
        self.__accounts = {}
        self.__transactions = []

    def new_client(self, info):
        ncl = BankClient(info, self)
        self.__clients[ncl] = []
        return ncl

    def new_account(self, client, balance=0):
        try:
            if type(balance) in (int, float) and balance >= 0:
                new_acc = BankAccount(client, self)
                self.__clients[client].append(new_acc)
                self.__accounts[new_acc] = balance
                self.__transactions.append((time.time(), None, new_acc, balance, True))
                return new_acc
            else:
                print("Балланс должен быть положительным числом")
        except KeyError:
            print("В банке нет такого клиента")
        except Exception:
            print("Неизвестная ошибка")


    def transfer(self, from_account, to_account, amount):
        result = False
        try:
            if type(amount) in (int, float) and amount > 0:
                new_from_ballance = self.__accounts[from_account] - amount
                if new_from_ballance > 0:
                    self.__accounts[from_account] = new_from_ballance
                    self.__accounts[to_account] += amount
                    result = True
                else:
                    print("Недостаточно средств на счете")
            else:
                print("Сумма перевода должна быть положительным числом")
        except KeyError:
            print("Аккаунты не принадлежат банку")
        except Exception:
            print("Неизвестная ошибка")
        finally:
            self.__transactions.append((time.time(), from_account, to_account, amount, result))
        return result


def test():
    sber = Bank()
    assert type(sber) is Bank, "Не создается объект класса Bank"

    ivan_sber = sber.new_client("Иванов Иван Иванович")
    assert type(ivan_sber) is BankClient, "Не создается объект класса BankClient"
    assert ivan_sber in sber._Bank__clients, "Клиент не добавляется в список клиентов"
    assert len(sber._Bank__clients) == 1, "Создается несколько объектов класса BankClient вместо одного"

    petr_sber = sber.new_client("Иванов Иван Иванович")
    assert type(petr_sber) is BankClient, "Не создается второй объект класса BankClient"
    assert petr_sber in sber._Bank__clients, "Второй клиент не добавляется в список клиентов"
    assert ivan_sber in sber._Bank__clients, "Первый клиент удаляется из списка после создания второго клиента"

    ivan_sber10k = sber.new_account(ivan_sber, 10000)
    assert type(ivan_sber10k) is BankAccount, "Не создается объект класса BankAccount"
    assert ivan_sber10k in sber._Bank__accounts, "Счет не добавляется в список счетов"
    assert len(sber._Bank__accounts) == 1, "Создается несколько объектов класса BankAccount вместо одного"
    assert sber._Bank__accounts[ivan_sber10k] == 10000, "Счет создается с неверным баллансом"
    assert len(sber._Bank__transactions) != 0, "Создание счета не учитывается в списке транзакций"
    assert len(sber._Bank__transactions) == 1, "Создается несколько записей в списке транзакций плосле создания счета"
    assert sber._Bank__transactions[0][2] == ivan_sber10k, "В списке транзакций указывается неверный счет получателя при создании счета"
    assert sber._Bank__transactions[0][3] == 10000, "В списке транзакций указывается неверная сумма перевода при создании счета"

    print("Ожидаемая ошибка: ", end ="")
    ivan_sber_negative = sber.new_account(ivan_sber, -10000)
    assert ivan_sber_negative not in sber._Bank__accounts, "Можно создать счет с отрицательным баллансом"

    print("Ожидаемая ошибка: ", end ="")
    ivan_sber_nondidgit = sber.new_account(ivan_sber, "сто сысяч")
    assert ivan_sber_nondidgit not in sber._Bank__accounts, "Можно создать счет с нечисловым баллансом"

    ivan_sber20k = sber.new_account(ivan_sber, 20000)
    assert type(ivan_sber20k) is BankAccount, "Не создается второй объект класса BankAccount"
    assert ivan_sber20k in sber._Bank__accounts, "Второй счет не добавляется в список счетов"
    assert ivan_sber10k in sber._Bank__accounts, "Первый счет удаляется из списка счетов после создания второго счета"
    assert len(sber._Bank__transactions) == 2, "Создание второго счета неверно учитывается в списке транзакций"
    assert sber._Bank__transactions[1][2] == ivan_sber20k, "В списке транзакций указывается неверный счет получателя при создании второго счета"
    assert sber._Bank__transactions[1][3] == 20000, "В списке транзакций указывается неверная сумма перевода при создании счета"

    petr_sber15k = sber.new_account(petr_sber, 15000)
    assert type(petr_sber15k) is BankAccount, "Не создается объект класса BankAccount для второго клиента"
    assert petr_sber15k in sber._Bank__accounts, "Счет для второго клиента не добавляется в список счетов"
    assert ivan_sber10k in sber._Bank__accounts and ivan_sber20k in sber._Bank__accounts, "Счета первого клиента удаляются из списка счетов после создания счета для второго клиента"
    assert len(sber._Bank__transactions) == 3, "Создание счета второго клиента неверно учитывается в списке транзакций"
    assert sber._Bank__transactions[2][2] == petr_sber15k, "В списке транзакций указывается неверный счет получателя при создании счета второго клиента"
    assert sber._Bank__transactions[2][3] == 15000, "В списке транзакций указывается неверная сумма перевода при создании счета второго клиента"

    assert sber.transfer(ivan_sber10k, ivan_sber20k, 9000), "Невозможно выполнить перевод между счетами одного клиента"
    assert sber._Bank__accounts[ivan_sber10k] == 1000, "После перевода между счетами одного клиента на счете отправителя неверный балланс"
    assert sber._Bank__accounts[ivan_sber20k] == 29000, "После перевода между счетами одного клиента на счете получателя неверный балланс"
    assert len(sber._Bank__transactions) >= 4, "Перевод между счетами одного клиента не учитывается в списке транзакций"
    assert len(sber._Bank__transactions) == 4, "Создается несколько записей в списке транзакций на один перевод между счетами одного клиента"
    assert sber._Bank__transactions[3][1] == ivan_sber10k, "В списке транзакций указывается неверный счет отправителя при переводе между счетами одного клиента"
    assert sber._Bank__transactions[3][2] == ivan_sber20k, "В списке транзакций указывается неверный счет получателя при переводе между счетами одного клиента"
    assert sber._Bank__transactions[3][3] == 9000, "В списке транзакций указывается неверная сумма перевода при переводе между счетами одного клиента"
    assert sber._Bank__transactions[3][4], "Успешный перевод при переводе между счетами одного клиента в списке транзакций указывается как неуспешный"

    assert sber.transfer(petr_sber15k, ivan_sber10k, 10000), "Невозможно выполнить перевод между счетами разных клиентов"
    assert sber._Bank__accounts[petr_sber15k] == 5000, "После перевода между счетами разных клиентов на счете отправителя неверный балланс"
    assert sber._Bank__accounts[ivan_sber10k] == 11000, "После перевода между счетами разных клиентов на счете получателя неверный балланс"
    assert len(sber._Bank__transactions) >= 5, "Перевод между счетами разных клиентов не учитывается в списке транзакций"
    assert len(sber._Bank__transactions) == 5, "Создается несколько записей в списке транзакций на один перевод между счетами разных клиентов"
    assert sber._Bank__transactions[4][1] == petr_sber15k, "В списке транзакций указывается неверный счет отправителя при переводе между счетами разных клиентов"
    assert sber._Bank__transactions[4][2] == ivan_sber10k, "В списке транзакций указывается неверный счет получателя при переводе между счетами разных клиентов"
    assert sber._Bank__transactions[4][3] == 10000, "В списке транзакций указывается неверная сумма перевода при переводе между счетами разных клиентов"
    assert sber._Bank__transactions[4][4], "Успешный перевод при переводе между счетами разных клиентов в списке транзакций указывается как неуспешный"

    print("Ожидаемая ошибка: ", end ="")
    assert not sber.transfer(petr_sber15k, ivan_sber10k, 100000), "Возможно выполнить перевод на сумму превышающую баланс на счете отправителя"
    assert sber._Bank__accounts[petr_sber15k] == 5000, "После попытки перевода на сумму превышающую баланс на счете отправителя на счете отправителя неверный балланс"
    assert sber._Bank__accounts[ivan_sber10k] == 11000, "После попытки перевода между на сумму превышающую баланс на счете отправителя на счете получателя неверный балланс"
    assert len(sber._Bank__transactions) >= 6, "Попытка перевода на сумму превышающую баланс на счете отправителя не учитывается в списке транзакций"
    assert len(sber._Bank__transactions) == 6, "Создается несколько записей в списке транзакций при попытке перевода на сумму превышающую баланс на счете отправителя"
    assert not sber._Bank__transactions[5][4], "Неудачная попытка перевода на сумму превышающую баланс на счете отправителя в списке транзакций указывается как успешная"

    print("Ожидаемая ошибка: ", end ="")
    assert not sber.transfer(petr_sber15k, ivan_sber10k, -100), "Возможно выполнить перевод с отрицательной суммой"
    assert sber._Bank__accounts[petr_sber15k] == 5000, "После попытки перевода с отрицательной суммой на счете отправителя неверный балланс"
    assert sber._Bank__accounts[ivan_sber10k] == 11000, "После попытки перевода с отрицательной суммой на счете получателя неверный балланс"
    assert len(sber._Bank__transactions) >= 7, "Попытка перевода с отрицательной суммой не учитывается в списке транзакций"
    assert len(sber._Bank__transactions) == 7, "Создается несколько записей в списке транзакций при попытке перевода с отрицательной суммой"
    assert not sber._Bank__transactions[6][4], "Неудачная попытка перевода с отрицательной суммой в списке транзакций указывается как успешная"

    print("Все тесты успешно пройдены")


test()
