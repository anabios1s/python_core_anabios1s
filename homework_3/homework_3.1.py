# Пользователь одной строкой вводит результаты запуска автотестов через пробел,
# например: PASS FAIL PASS SKIP PASS FAIL.
# Программа должна преобразовать введенную строку в список,
# подсчитать количество тестов каждого типа и вывести общую статистику.
# Логику подсчета необходимо вынести в отдельную функцию get_test_statistics(results),
# которая возвращает результат в виде словаря.
# Дополнительно программа должна вывести процент успешно пройденных тестов относительно общего количества тестов.
# Пример вывода:
# Всего тестов: 6 PASS: 3 FAIL: 2 SKIP: 1
# Успешно: 50.0%

result_test_from_user = input("Введите одной строкой результаты прохождения автотестов в формате - \"PASS FAIL SKIP\":")
results = result_test_from_user.split()
print(results)

def get_test_statistics(results):
    stats = {
        "FAIL": 0,
        "SKIP": 0,
        "PASS": 0
    }
    for status in results:
        if status in stats:
            stats[status] += 1
    return stats

stats = get_test_statistics(results)

total_tests = sum(stats.values())

if total_tests > 0:
    success_percent = stats["PASS"] / total_tests * 100
else:
    success_percent = 0

print(
    f"Всего тестов: {total_tests}\n"
    f"PASS: {stats['PASS']}\n"
    f"FAIL: {stats['FAIL']}\n"
    f"SKIP: {stats['SKIP']}"
)
print(f"Успешно: {success_percent:.1f}%")
