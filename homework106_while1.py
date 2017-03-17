#Создаем список имён
new_list = ['Вася','Маша','Петя','Валера','Саша','Даша']
#Кого будем искать
search_name = input('Кого будем искать: ')
try:
	while new_list[0] != search_name:
		new_list.pop(0)
		#список пуст
		if not new_list:
			print(search_name + ' нет в списке')
			break
	else:
		print(search_name + ' нашёлся')
#Исключение - индекс не в диапазоне
except IndexError:
	print(search_name + ' нет в списке - исключение')
