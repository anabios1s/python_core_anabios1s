# Есть два списка:
# (test_cases) = ["Login", "Registration", "Checkout", "Logout"]
# statuses = ["PASS", "FAIL", "PASS", "SKIP"]
# Необходимо с помощью zip() объединить название каждого тест-кейса с его статусом.
# Создайте функцию statuses = ["PASS", "FAIL", "PASS", "SKIP"],
# которая принимает два списка и выводит отчёт в формате Login — PASS.
# После формирования отчета программа должна определить количество успешных и неуспешных тестов и сообщить,
# можно ли считать тестовый запуск успешным: если есть хотя бы один FAIL, запуск считается неуспешным.


def statuses ():
    test_cases = ["Login", "Registration", "Checkout", "Logout"]
    statuses = ["PASS", "FAIL", "PASS", "SKIP"]
    zip_list = dict(zip(test_cases, statuses))
    for key, value in zip_list.items():
        print(f"{key}: {value}")

    pass_count = statuses.count("PASS")
    fail_count = statuses.count("FAIL")

    print(f"Успешных тестов: {pass_count}")
    print(f"Неуспешных тестов: {fail_count}")

    if fail_count > 0:
        print("Тестовый запуск неуспешный: есть упавшие тесты.")
    else:
        print("Тестовый запуск успешный: упавших тестов нет.")

statuses ()
