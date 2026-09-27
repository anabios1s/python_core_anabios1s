import test_data

quantity_of_users = int(input("Введите количество тестовых пользователей: "))

users = []

for number in range(quantity_of_users):
    user = test_data.generate_user()
    users.append(user)

print("\nСписок тестовых пользователей:")

for user in users:
    print(
        f"Логин: {user['login']}, "
        f"возраст: {user['age']}, "
        f"статус: {user['status']}"
    )

statistics = {
    "ACTIVE": 0,
    "BLOCKED": 0,
    "INACTIVE": 0
}

for user in users:
    status = user["status"]
    statistics[status] += 1

print("\nСтатистика по статусам:")

for status, count in statistics.items():
    print(f"{status}: {count}")
