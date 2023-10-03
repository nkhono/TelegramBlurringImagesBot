import telebot, utility, os
from config import *
from language import translate as trn

bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start'])
def start(message):
	language = message.from_user.language_code
	chat_id = message.chat.id

	if message.chat.type == 'private':
		bot.send_message(chat_id, trn(language, 'WELCOME_MESSAGE'), parse_mode='html')

	else:
		bot.send_message(chat_id, trn(language, 'NOT_SUPPORTED_CHAT'), parse_mode='html')
		bot.leave_chat(chat_id)

@bot.message_handler(content_types=['document'])
def document(message):
	language = message.from_user.language_code
	chat_id = message.chat.id
	if message.chat.type == 'private':
		sent = bot.send_message(message.chat.id, '⌛️')
		file_id = message.document.file_id
		file_name = message.document.file_name

		file_id_info = bot.get_file(file_id)
		downloadedDocument = bot.download_file(file_id_info.file_path)

		open(file_name, 'wb').write(downloadedDocument)
		new_file = utility.blur(file_name)

		bot.delete_message(chat_id, sent.id)
		bot.send_document(chat_id, open(new_file, 'rb'), caption=f'<b>{telegram_username}</b>', parse_mode='html')
		try:
			os.remove(file_name)
			os.remove(new_file)
		except:
			pass
	
	else:
		bot.send_message(chat_id, trn(language, 'NOT_SUPPORTED_CHAT'), parse_mode='html')
		bot.leave_chat(chat_id)
bot.polling(none_stop=True)