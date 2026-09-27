#Секретное число. В программе хранится секретное число 37.
# Пользователь должен вводить числа до тех пор, пока не угадает его.
# После каждой неправильной попытки программа должна сообщать, больше или меньше введенное число относительно секретного.
# После правильного ответа необходимо вывести сообщение об успехе и количество совершенных попыток.

hidden_number = 37
is_success = False
attempt = 0
while is_success is False:
    input_number = int(input("Введите число: "))
    attempt += 1
    if input_number > hidden_number:
        print(f"{input_number} БОЛЬШЕ секретного числа, попробуйте еще раз!")
    elif input_number < hidden_number:
        print(f"{input_number} МЕНЬШЕ секретного числа, попробуйте еще раз!")
    else:
        print(f"Успех! {input_number} - секретное число!!")
        print(f"Угадано с {attempt} попытки")
        is_success = True
