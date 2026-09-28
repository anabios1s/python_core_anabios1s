# Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

with open("for_hw4.3.txt","r") as f:
    for_new_file = f.readlines()
with open("for_hw4.3.txt","w") as f:
    for i in for_new_file:
        i = int(i.strip())
        f.write(str(i ** 2) + "\n")
