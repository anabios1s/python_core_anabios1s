# Дан список тестов: tests = \
# [ "test_login", "test_logout", "test_registration", "test_profi le", "test_payment", "test_search" ]
# Пользователь вводит количество тестов, которые необходимо запустить.
# Программа должна случайным образом выбрать указанное количество уникальных тестов из списка
# и каждому выбранному тесту случайно назначить статус PASS, FAIL или SKIP.
# Результаты необходимо объединить и вывести в виде отчёта.
# Если пользователь запросил больше тестов, чем существует в списке, программа должна вывести сообщение об ошибке.

import random

statuses = ["PASS", "FAIL", "SKIP"]
tests = [ "test_login", "test_logout", "test_registration", "test_profi le", "test_payment", "test_search" ]
test_to_call = int(input("Введите количество тестов, необходимых к запуску:   "))

if test_to_call > len(tests):
    print("Ошибка: запрошено больше тестов, чем есть в списке.")
elif test_to_call < 0:
    print("Ошибка: количество тестов не может быть отрицательным.")
else:
    to_chose_the_tests = random.sample(tests, test_to_call)
    print("\nОтчёт о запуске:")
    for test in to_chose_the_tests:
        status = random.choice(statuses)
        print(f"{test} — {status}")
