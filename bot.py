from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inlinekeyboardmarkup import InlineKeyboardMarkup
import ephem 
import datetime, bot_config

def main():

	updater = Updater(bot_config.token)

	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler('start',greet_user))
	#По команде planet отвечаем в каком она созвездии в данный момент
	dp.add_handler(CommandHandler('planet',planet_constellation,pass_args=True))
	#команда посчитать количество слов в ""
	dp.add_handler(CommandHandler('wordcount',wordcount,pass_args=True))
	#команда посчитать выражение
	dp.add_handler(CommandHandler('calculate',calculate,pass_args=True))
	#добавим много новый handler 
	dp.add_handler(MessageHandler([Filters.text],talk_to_me))

	#добавим обработку ошибок
	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()

#приветствуем пользователя
def greet_user(bot, update):
	print('Вызван /start')
	bot.sendMessage(update.message.chat_id, text= 'Давай общаться!')

#функция ошибок
def show_error(bot,update,error):
	print(error)

#обработчик сообщений
def talk_to_me(bot, update):

	if update.message.text.find('сколько будет') != -1:
		calculate_words(bot,update)
	else:
		print(update.message.text)
		bot.sendMessage(update.message.chat_id, update.message.text)

#определяем в каком созвездии планета в данный момент. 
#считываем название планеты по команде /planet
def planet_constellation(bot,update,args):
	#определяем текущую дату и время
	date = datetime.datetime.now().strftime('%Y/%m/%d')
	#input_text = ' '.join(args)
	#Меркурий
	if str(args[0]) == 'Mercury':
		p = ephem.Mercury(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 	#Венера
	if str(args[0]) == 'Venus':
		p = ephem.Venus(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
	#Марс
	if str(args[0]) == 'Mars':
		p = ephem.Mars(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 	#Юпитер
	if str(args[0]) == 'Jupiter':
		p = ephem.Jupiter(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 	#Сатурн
	if str(args[0]) == 'Saturn':
		p = ephem.Saturn(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 	#Уран
	if str(args[0]) == 'Uranus':
		p = ephem.Uranus(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 	#Нептун
	if str(args[0]) == 'Neptune':
		p = ephem.Neptune(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 	#Плутон
	if str(args[0]) == 'Pluto':
		p = ephem.Pluto(date)
		bot.sendMessage(update.message.chat_id,text=str(args[0]) + ' в созвездии '+ ephem.constellation(p)[1])
 		 		 
#подсчёт количества слов в предложении
def wordcount(bot,update,args):
 	#ответ
 	if args:		
 		bot.sendMessage(update.message.chat_id,text='в предложении ' + str(len(args)) + word)
 	else:
 		bot.sendMessage(update.message.chat_id,text='в предложении нет слов')
#функция калькулятор
def calculate(bot,update,args):
	#преобразовываем args в строку
	input_text = ' '.join(update.message.text)
	#если строка не пуста
	operand_1, operand_2  = '',''
	operation = ''
	result = -1.0
	if args:
		#анализируем строку
		for symbol in input_text:
			#операнд №1
			if symbol in [str(i) for i in range(10)] and not operation:
				operand_1 += symbol
			#операция
			if symbol in ['+','-','*','/',' ']:
				operation = symbol
			#операнд №2
			if symbol in [str(i) for i in range(10)] and operation:
				operand_2 += symbol
		print('Введена строка: ' + input_text)
		print('Операнд 1: ' + str(operand_1))
		print('Операнд 2: ' + str(operand_2))
		print('Операция: '  + operation)
		#ошибка - делить на ноль нельзя
		if operand_2 == 0 and operation == '/':
			print('Ошибка: деление на ноль ')
			bot.sendMessage(update.message.chat_id,text='Ошибка! Делить на ноль нельзя!')
		#ошибка - не введён первый операнд	
		if not operand_1:
			print('Ошибка: не введён первый операнд')
			bot.sendMessage(update.message.chat_id,text='Ошибка! первый операнд не введён')
		#ошибка - не введён второй операнд	
		if not operand_2:
			print('Ошибка: не введён второй операнд')
			bot.sendMessage(update.message.chat_id,text='Ошибка! второй операнд не введён')
		#ошибка - не введена операция или пробел	
		if not operation or operation == ' ':
			print('Ошибка: не введена операция')
			bot.sendMessage(update.message.chat_id,text='Ошибка! не введена операция')
		#если введены все операнды и операция
		if operand_1 and operand_2 and operation and not operation == ' ':
			print('Выполняем вычисление выражения')
			#операция сложения
			if operation == '+':
				result = float(operand_1) + float(operand_2)
			#операция вычитания
			if operation == '-':
				result = float(operand_1) - float(operand_2)
			#операция умножения
			if operation == '*':
				result = float(operand_1) * float(operand_2)
			#операция деления
			if operation == '/':
				result = float(operand_1) / float(operand_2)
			#вывод результата в чвт
			bot.sendMessage(update.message.chat_id,text=result)
	#если строка пуста, то невозможно посчитать выражение
	else:
		bot.sendMessage(update.message.chat_id,text='нет введенных чисел!')

#кнопки
def build_menu(buttons: list,
               n_cols: int,
               header_buttons: list = None,
               footer_buttons: list = None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

#функция калькулятор со словами на входе
def calculate_words(bot,update):
	print('Вызов функции calculate_words')
	#словарь слово-число
	dict_number = {	'ноль'	 : '0',
					'один'	 : '1',
					'два'	 : '2',
					'три'	 : '3',
					'четыре' : '4',
					'пять'	 : '5',
					'шесть'  : '6',
					'семь' 	 : '7',
					'восемь' : '8',
					'девять' : '9'}
	#словарь число-слово
	dict_number_rev = {	'0' : 'ноль',
						'1' : 'один',
						'2' : 'два',
						'3' : 'три',
						'4' : 'четыре',
						'5' : 'пять',
						'6' : 'шесть',
						'7' : 'семь',
						'8' : 'восемь',
						'9' : 'девять'}
	#словарь слово-операция
	dict_operation = {'плюс':'+','минус':'-','умножить':'*','разделить':'/'}
	#преобразовываем update в список
	input_text = update.message.text.split()
	print('Введена строка: ' + input_text[0])
	#если строка не пуста
	operand_1, operand_2  = '',''
	operation = ''
	result = 0
	
	if input_text:
		#анализируем строку
		for symbol in input_text:
			#операнд №1
			if symbol in dict_number and not operation:
				operand_1 = dict_number[symbol]
			#операция
			if symbol in dict_operation:
				operation = dict_operation[symbol]
			#операнд №2
			if symbol in dict_number and operation:
				operand_2 = dict_number[symbol]
		
		print('Операнд 1: ' + str(operand_1))
		print('Операнд 2: ' + str(operand_2))
		print('Операция: '  + operation)

		#ошибка - делить на ноль нельзя
		if operand_2 == 0 and operation == '/':
			print('Ошибка: деление на ноль ')
			bot.sendMessage(update.message.chat_id,text='Ошибка! Делить на ноль нельзя!')
		#ошибка - не введён первый операнд	
		if not operand_1:
			print('Ошибка: не введён первый операнд')
			bot.sendMessage(update.message.chat_id,text='Ошибка! первый операнд не введён')
		#ошибка - не введён второй операнд	
		if not operand_2:
			print('Ошибка: не введён второй операнд')
			bot.sendMessage(update.message.chat_id,text='Ошибка! второй операнд не введён')
		#ошибка - не введена операция или пробел	
		if not operation or operation == ' ':
			print('Ошибка: не введена операция')
			bot.sendMessage(update.message.chat_id,text='Ошибка! не введена операция')
		#если введены все операнды и операция
		if operand_1 and operand_2 and operation and not operation == ' ':
			print('Выполняем вычисление выражения')
			#операция сложения
			if operation == '+':
				result = int(operand_1) + int(operand_2)
			#операция вычитания
			if operation == '-':
				result = int(operand_1) - int(operand_2)
			#операция умножения
			if operation == '*':
				result = int(operand_1) * int(operand_2)
			#операция деления
			if operation == '/':
				result = int(operand_1) / int(operand_2)
			#Вывод результата	
			print('result = ', result)
			#вывод результата в чат
			bot.sendMessage(update.message.chat_id,text=dict_number_rev[str(result)])

	else:
		bot.sendMessage(update.message.chat_id,text='нет введенных слов-чисел!')
		
main()