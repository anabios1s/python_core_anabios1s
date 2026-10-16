# Создайте класс ATM, описывающий работу банкомата. Банкомат должен
# хранить количество купюр номиналом 20, 50 и 100. Начальное количество
# купюр каждого номинала передается при создании объекта через
# __init__().
# Реализуйте метод add_money(), позволяющий добавить в банкомат
# купюры каждого номинала. Также реализуйте метод withdraw(amount)
# для снятия указанной суммы. Метод должен определить, может ли
# банкомат выдать запрошенную сумму имеющимися купюрами. Если
# операция возможна, необходимо уменьшить количество купюр в
# банкомате, вывести, сколько купюр каждого номинала было выдано, и
# вернуть True. Если указанную сумму выдать невозможно — вернуть False
# и оставить содержимое банкомата без изменений.
# Создайте объект ATM, добавьте в него несколько купюр и выполните
# несколько операций снятия денег.


class ATM:
    def __init__(self, banknote_20, banknote_50, banknote_100):
        self.banknote_20 = banknote_20
        self.banknote_50 = banknote_50
        self.banknote_100 = banknote_100

    def add_money(self, banknote_20, banknote_50, banknote_100):
        self.banknote_20 += banknote_20
        self.banknote_50 += banknote_50
        self.banknote_100 += banknote_100

    def withdraw(self, amount):

        banknote_100 = min(amount // 100, self.banknote_100)
        amount -= banknote_100 * 100

        banknote_50 = min(amount // 50, self.banknote_50)
        amount -= banknote_50 * 50

        banknote_20 = min(amount // 20, self.banknote_20)
        amount -= banknote_20 * 20

        if amount != 0:
            print("Указанную сумму выдать невозможно!")
            return False

        self.banknote_100 -= banknote_100
        self.banknote_50 -= banknote_50
        self.banknote_20 -= banknote_20

        print(f"Выдано купюр номиналом 100: {banknote_100}")
        print(f"Выдано купюр номиналом 50: {banknote_50}")
        print(f"Выдано купюр номиналом 20: {banknote_20}")

        return True

atm = ATM(10, 10, 10)

atm.add_money(5, 5, 5)

print("Попытка снять 40:")
result = atm.withdraw(40)
print(f"Результат: {result}\n")

print("Попытка снять 80:")
result = atm.withdraw(80)
print(f"Результат: {result}\n")

print("Попытка снять 4:")
result = atm.withdraw(4)
print(f"Результат: {result}\n")
