# Декоратор повторного запуска. Напишите декоратор с параметром retry(count),
# который повторно запускает декорируемую функцию указанное количество раз, пока функция не вернет True.
# Перед каждой попыткой необходимо выводить её номер. Если функция вернула True, дальнейшие попытки выполнять не нужно.
# Декоратор должен поддерживать передачу позиционных и именованных аргументов через *args и **kwargs.
from functools import wraps

def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt}...")
                result = func(*args, **kwargs)
                if result is True:
                    return True
            return False
        return wrapper
    return decorator

@retry(3)
def check():
    if not hasattr(check, 'counter'):
        check.counter = 0
    check.counter += 1
    return check.counter >= 3

result = check()
print(f"Результат: {result}\n")
