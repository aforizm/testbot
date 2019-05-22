# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types


TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup()
markup.row('this is buttomn')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	bot.send_message(message.chat.id, message.text)
	bot.send_message(message.chat.id, 'choose...', reply_markup=markup)


if __name__ == '__main__':
	bot.polling(none_stop = True)



