# Декоратор для логирования автотестов. Напишите декоратор log_test,
# который перед запуском тестовой функции выводит её имя, после выполнения сообщает о завершении и выводит полученный результат.
# Декоратор должен поддерживать функции с произвольным количеством позиционных и именованных аргументов с помощью *args и **kwargs.
# Используйте functools.wraps(), чтобы сохранить метаданные исходной функции.

from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Тест {func.__name__} завершён.")
        print(f"Результат: {result} \n")

        return result
    return wrapper

@log_test
def test_sum(number_1, number_2):
    return number_1 + number_2

test_sum(10, 5)
