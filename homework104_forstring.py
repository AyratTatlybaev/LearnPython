#Создаём пустой список
new_list = []
#Считываем введенную строку
new_string = input('Введите новую строку: ')
for i in range(len(new_string)):
	new_list.append(new_string[i])
#Выводим символы
for i in range(len(new_list)):
	print(new_list[i])
