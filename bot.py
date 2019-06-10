# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

'''
Список переменных которе нужны
count       - счетчик дней, с момента последнего обнуления
lastDateRes - дата последнего сброса
today		- сегодняшняя дата
maxCount 	- Рекорд дней без сборса счетчика

потом надо бужет сделать переменную  ID пользователя
'''


TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["start"])
def start_messages(message):
	bot.send_message(message.chat.id, message.text)
	print("Hello bla bla bla")
	print("/count - Uznat count\n/reset - reset count")
	

if __name__ == '__main__':
	bot.polling(none_stop = True)



