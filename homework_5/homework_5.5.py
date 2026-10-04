# 5. Создайте программу для формирования отчёта по результатам автоматизированного тестирования.
# Исходные данные программа должна получать из JSON-файла,
# в котором для каждого теста указаны название, статус и время выполнения.
# Программа должна определить общее количество тестов, количество тестов со статусами PASS, FAIL и SKIP,
# сформировать список упавших тестов, определить самый длительный тест
# и рассчитать суммарное время выполнения. При обработке данных необходимо использовать минимум
# один генератор списка, lambda, filter() и reduce().
# Работу с файлом и входными данными необходимо защитить с помощью try/except:
#     программа должна корректно обрабатывать отсутствие файла,
#     некорректный JSON и неправильную структуру тестовых данных.
# Сформированный итоговый отчёт необходимо сохранить в отдельный JSON-файл.

import json
from functools import reduce

try:
    with open("AT_results_for_hw_5.5.json", "r") as file:
        all_tests = json.load(file)

    for test in all_tests:
        try:
            name = test["name"]
            status = test["status"]
            time = test["time"]

            print(f"Название теста: {name}")
            print(f"Статус выполнения: {status}")
            print(f"Время выполнения: {time}\n")

        except KeyError as e:
            print(f"Ошибка: отсутствует обязательное поле  {e} \n")

except FileNotFoundError as e:
    print(f"Ошибка: json файл не найден \n")

except json.JSONDecodeError as e:
    print("Ошибка: нарушен синтаксис файла json \n")

statuses = ["PASS", "FAIL", "SKIP"]

pass_quantity = len(list(filter(lambda test: test["status"] == "PASS", all_tests)))
fail_quantity = len(list(filter(lambda test: test["status"] == "FAIL", all_tests)))
skip_quantity = len(list(filter(lambda test: test["status"] == "SKIP", all_tests)))
quantity_of_tests = len(all_tests)

failed_tests = list(filter(lambda test: test["status"] == "FAIL", all_tests))

failed_test_names = list(map(lambda test: test["name"], failed_tests))

passed_test_names = [
    test["name"]
    for test in all_tests
    if test["status"] == "PASS"
]

full_execution_time = reduce(lambda total, test: total + test["time"], all_tests, 0)
longest_test = max(all_tests, key=lambda test: test["time"], default=None)

print(f"PASS: {pass_quantity}")
print(f"FAIL: {fail_quantity}")
print(f"SKIP: {skip_quantity}")
print(f"Всего тестов - {quantity_of_tests}")

print(f"Упавшие тесты: {failed_test_names}")
print(f"Успешно пройденные тесты: {passed_test_names}")
print(f"Общее время выполнения: {full_execution_time:.2f} сек.")

report = {
    "quantity_of_tests": quantity_of_tests,
    "pass_quantity": pass_quantity,
    "fail_quantity": fail_quantity,
    "skip_quantity": skip_quantity,
    "failed_test_names": failed_test_names,
    "passed_test_names": passed_test_names,
    "full_execution_time": full_execution_time,
    "longest_test": longest_test
}

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)