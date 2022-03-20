import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Start', 'Hello'])
def start(message):
    bot.send_message(message.chat.id, "Hello select the signal!")



bot.polling()
