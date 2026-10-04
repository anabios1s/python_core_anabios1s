# Замыкание для проверки времени выполнения.
# Напишите функцию create_time_checker(max_time), которая возвращает вложенную функцию для проверки времени выполнения теста.
# Вложенная функция принимает фактическое время выполнения и сообщает, превышен установленный лимит или нет.
# Создайте два независимых замыкания с разными значениями max_time и продемонстрируйте их работу.

def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            print(
                f"Лимит превышен: тест выполнялся {actual_time} сек., допустимо не более {max_time} сек."
            )
        else:
            print(
                f"Лимит не превышен: тест выполнялся {actual_time} сек., лимит — {max_time} сек"
            )

    return check_time


test_checker_first = create_time_checker(1)
test_checker_second = create_time_checker(5)

test_checker_first(0.7)
test_checker_first(1.5)

test_checker_second(3)
test_checker_second(7)
