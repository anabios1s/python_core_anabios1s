# Рекурсивный подсчет результатов тестов.
# Дан список результатов автотестов со статусами PASS, FAIL и SKIP.
# Напишите рекурсивную функцию, которая подсчитывает количество тестов со статусом PASS.
# Функция должна обрабатывать список с помощью рекурсии. Использовать циклы for и while нельзя.

def all_passed_tests(tests):
    # Базовый случай: список закончился
    if not tests:
        return 0

    # Первый тест списка
    first_test = tests[0]

    # Все тесты, кроме первого
    remaining_tests = tests[1:]

    # Если первый тест пройден — прибавляем 1
    if first_test["status"] == "PASS":
        return 1 + all_passed_tests(remaining_tests)
    else:
        return all_passed_tests(remaining_tests)

all_tests = [
    {"name": "test_1", "status": "PASS"},
    {"name": "test_2", "status": "FAIL"},
    {"name": "test_3", "status": "PASS"},
    {"name": "test_4", "status": "SKIP"},
    {"name": "test_5", "status": "PASS"},
    {"name": "test_6", "status": "pass"}
]

pass_count = all_passed_tests(all_tests)

print(f"Количество успешно пройденных тестов: {pass_count}")
