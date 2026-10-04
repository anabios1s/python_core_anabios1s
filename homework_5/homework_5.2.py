# 2. Создайте JSON-файл с тестовыми пользователями для проверки авторизации.
# Для каждого пользователя должны храниться логин, пароль и ожидаемый результат авторизации.
# Напишите программу, которая открывает JSON-файл,
# загружает данные и выводит информацию о каждом тестовом пользователе.
# Программа должна корректно обрабатывать ситуации, когда файл не существует,
# содержимое файла невозможно прочитать как JSON или у пользователя отсутствует обязательное поле.
# Для обработки ошибок используйте try/except,
# соответствующие типы исключений и получение информации об ошибке через as e.

import json


try:
    with open("users_for_hw_5.2.json", "r") as file:
        users = json.load(file)

    for user in users:
        try:
            login = user["login"]
            password = user["password"]
            expected_result = user["expected_result"]

            print(f"Логин: {login}")
            print(f"Пароль: {password}")
            print(f"Ожидаемый результат: {expected_result} \n")

        except KeyError as e:
            print(f"Ошибка: отсутствует обязательное поле  {e} \n")

except FileNotFoundError as e:
    print(f"Ошибка: json файл не найден.")

except json.JSONDecodeError as e:
    print("Ошибка: нарушен синтаксис файла json.")
