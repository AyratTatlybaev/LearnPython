from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
	updater = Updater('345548542:AAH9dJDqihmalKUtbbtnya4lL_-aLPOFTpo')
	
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',green_user))
	#добавим много новый handler 
	dp.add_handler(MessageHandler([Filters.text],talk_to_me))

	#добавим обработку ошибок
	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()

def green_user(bot, update):
	print('Вызван /start')
	bot.sendMessage(update.message.chat_id, text= 'Давай общаться!')

def show_error(bot,update,error):
	print(error)

#обработчик сообщений
def talk_to_me(bot, update):
	print(update.message.text)
	bot.sendMessage(update.message.chat_id, update.message.text)

main()