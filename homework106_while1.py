#Создаем список имён
new_list = ['Вася','Маша','Петя','Валера','Саша','Даша']
#Кого будем искать
search_name = input('Кого будем искать: ')
while new_list[0] != search_name:
	new_list.pop(0)
print('Валера нашелся')