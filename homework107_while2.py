#Создаем список имён
new_list = ['Вася','Маша','Петя','Валера','Саша','Даша']
#Функция поиска имени в листе
def find_person(name,list):
	try:
		while list[0] != name:
			list.pop(0)	
		return str(name) + ' нашёлся'	
	#Исключение - индекс не в диапазоне
	except IndexError:
		return str(name) + ' нет в списке'
	
#Кого будем искать
search_name = input('Кого будем искать: ')
#Поиск имени в списке и печать результата
print(find_person(search_name,new_list))