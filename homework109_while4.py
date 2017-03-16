#Функция Как дела?
def ask_user():
	#Переменная - ввод пользователя
	input_user = ''
	while input_user != 'Хорошо':
		print('Как дела?')
		#Ответ пользователя 
		input_user = input()	
	while input_user.lower() != 'пока': 	
		#Вопрос пользователя
		input_user = input()
		#Вывод ответа по вопросу
		print(get_answer(input_user))
	exit()
#Функция Отвечаю на вопросы
def get_answer(question):
	try:
		answers = {'привет':'И тебе привет!','как дела?':'Лучше всех', 'пока':'Увидимся'}
		return answers[question.lower()]
	except KeyError:
		return 'Не знаю что тебе сказать'
#Вывод результата выполнения функции
print(ask_user())