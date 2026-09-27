# Создайте собственный модуль test_data.py. В нём реализуйте функции generate_login(),
# generate_age(), generate_status() и generate_user().
# generate_user() должна использовать остальные функции и возвращать готового тестового пользователя в виде словаря.
# Создайте второй файл main.py. Импортируйте в него созданный модуль,
# запросите у пользователя количество необходимых тестовых пользователей и сформируйте их список.
# После генерации выведите пользователей и статистику по статусам ACTIVE, BLOCKED и INACTIVE.
import random

def generate_login():
    login = (f"username_" + str(random.randint(0, 100)))
    return login

def generate_age():
    return random.randint(18, 95)

def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]
    return random.choice(statuses)

def generate_user():
    user = {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }
    return user
