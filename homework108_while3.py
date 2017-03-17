#Функция Как дела?
def ask_user():
	input_user = ''
	while input_user != 'Хорошо':
		print('Как дела?\n')
		input_user = input()
	exit()
#Вывод результата выполнения функции
print(ask_user())