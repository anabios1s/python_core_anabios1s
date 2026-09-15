#Заменить символ "#" на символ "/" в строке: www.my_site.com#about
string_for_change= "www.my_site.com#about"
string_for_change_after_change = string_for_change.replace("#", "/")
correct_url = "До замены символа: {}, после замены: {}". format(string_for_change, string_for_change_after_change)
print(correct_url)
# print(string_for_change)
# print("После замены символа")
# print(string_for_change_after_change)
# комментарирование всех строк - ctrl+/