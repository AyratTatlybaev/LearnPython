#Функция Как дела?
def ask_user():
	input_user = ''
	#Ловим исключения
	try:
		while input_user != 'Хорошо':
			print('Как дела?')
			input_user = input()
		exit()
	#Исключение 1 - ввод с клавиатуры Ctrl+C
	except KeyboardInterrupt:
		return 'Принудительное завершение работы Ctrl+C. Пока!'
	#Исключение 2 - конец файла
	except EOFError:
		return 'Прерывание - Конец файла '
#Вывод результата выполнения функции
print(ask_user())