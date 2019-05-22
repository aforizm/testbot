# -*- coding: utf-8 -*-
import config
import telebot
import parser

"""bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_meassages(message):
	bot.send_meassage(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop = True)  """
TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()