# 1. Дан список результатов автотестов.
# Для каждого теста известны его название, статус выполнения (PASS, FAIL или SKIP) и время выполнения.
# Напишите программу, которая с помощью filter() получает все упавшие тесты,
# с помощью map() формирует список их названий,
# а с помощью reduce() рассчитывает общее время выполнения всех тестов.
# Дополнительно с помощью генератор списка сформируйте список названий успешно пройденных тестов.
# В результате программа должна вывести количество тестов каждого статуса,
# список названий упавших тестов,
# список успешно пройденных тестов и общее время выполнения всех тестов.

from functools import reduce

all_tests = [
    {"name": "test_1", "status": "PASS", "time": 1.25},
    {"name": "test_2", "status": "PASS", "time": 0.80},
    {"name": "test_3", "status": "FAIL", "time": 2.10},
    {"name": "test_4", "status": "SKIP", "time": 0.00},
    {"name": "test_5", "status": "FAIL", "time": 1.45}
]

pass_quantity = len(list(filter(lambda test: test["status"] == "PASS", all_tests)))
fail_quantity = len(list(filter(lambda test: test["status"] == "FAIL", all_tests)))
skip_quantity = len(list(filter(lambda test: test["status"] == "SKIP", all_tests)))

failed_tests = list(filter(lambda test: test["status"] == "FAIL", all_tests))

failed_test_names = list(map(lambda test: test["name"], failed_tests))

passed_test_names = [
    test["name"]
    for test in all_tests
    if test["status"] == "PASS"
]

full_time = reduce(lambda a, b: a + b ["time"], all_tests, 0)

print(f"PASS: {pass_quantity}")
print(f"FAIL: {fail_quantity}")
print(f"SKIP: {skip_quantity}")

print(f"Упавшие тесты: {failed_test_names}")
print(f"Успешно пройденные тесты: {passed_test_names}")
print(f"Общее время выполнения: {full_time:.2f} сек.")
