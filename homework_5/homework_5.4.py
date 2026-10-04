# 4. Создайте собственное исключение InvalidTestStatusError, наследуемое от Exception.
# Напишите функцию, которая принимает статус теста и проверяет его значение.
# Допустимыми считаются только PASS, FAIL и SKIP.
# Если передан любой другой статус, функция должна с помощью raise создать InvalidTestStatusError
# и передать в него сообщение с некорректным значением.
# В основной программе обработайте это исключение через try/except
# и выведите понятное сообщение пользователю.
# Проверьте программу как с корректными, так и с некорректными статусами.

class InvalidTestStatusError(Exception):
    pass

def test(status):
    statuses = ["PASS", "FAIL", "SKIP"]
    if status not in statuses:
        raise InvalidTestStatusError(f"Статус {status} не предусмотрен в статусной модели.")
    print(f"Статус {status} корректный.")

params_for_example = [
        "PASS", "10",  "FAIL" , "SKIP"
    ]
for status in params_for_example:
    try:
        test(status)
    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")
