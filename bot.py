from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ephem import * 
import datetime, bot_config

def main():

	#определяем текущую дату и время
	date = datetime.datetime.now()

	updater = Updater(bot_config.token)
	
	dp = updater.dispatcher
	#По команде planet отвечаем в каком она созвездии в данный момент
	dp.add_handler(CommandHandler('planet',planet_constellation))

	dp.add_handler(CommandHandler('start',greet_user))
	#добавим много новый handler 
	dp.add_handler(MessageHandler([Filters.text],talk_to_me))

	#добавим обработку ошибок
	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()

def greet_user(bot, update):
	print('Вызван /start')
	bot.sendMessage(update.message.chat_id, text= 'Давай общаться!')

def show_error(bot,update,error):
	print(error)

#обработчик сообщений
def talk_to_me(bot, update):
	print(update.message.text)
	bot.sendMessage(update.message.chat_id, update.message.text)

#функция возвращающая созвездие, в котором находится планета
def planet_constellation(bot,update):
	print('Вызван /planet')
	ask_planet = message.text
	bot.sendMessage(update.message.chat_id, text= constellation(ask_planet(date.strftime('%d.%m.%Y'))))

main()