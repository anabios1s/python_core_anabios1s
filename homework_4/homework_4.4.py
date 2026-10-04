# Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа

with open("file_1.txt", "r", encoding="utf-8") as file_1, \
     open("file_2.txt", "r", encoding="utf-8") as file_2:

    data_1 = file_1.read()
    data_2 = file_2.read()

with open("file_1.txt", "w", encoding="utf-8") as file_1, \
     open("file_2.txt", "w", encoding="utf-8") as file_2:

    file_1.write(data_2)
    file_2.write(data_1)
