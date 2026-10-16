# Создайте класс CreditCard, описывающий кредитную карту. При
# создании объекта необходимо передавать номер счёта и начальный
# баланс карты. Реализуйте метод deposit(amount), который пополняет
# баланс на указанную сумму, метод withdraw(amount), который снимает
# указанную сумму, и метод show_info(), который выводит номер счёта и
# текущий баланс.
# Создайте три объекта класса CreditCard с разными номерами счетов и
# начальными балансами. Пополните баланс первой и второй карты, а с
# третьей карты снимите некоторую сумму. После выполнения операций
# выведите информацию о состоянии всех трёх карт.

class CreditCard:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_info(self):
        print(f"Номер счета: {self.__account_number}"
              f"\nБаланс: {self.__balance}")


first_acc = CreditCard(account_number="4-8-15-16-23-42", balance=1000)
second_acc = CreditCard(account_number="42-42", balance=2000)
third_acc = CreditCard(account_number=88002000600, balance=3000)

first_acc.deposit(10)
second_acc.deposit(505)
third_acc.withdraw(3)

first_acc.show_info()
second_acc.show_info()
third_acc.show_info()
