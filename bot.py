import telebot
import os

TOKEN_TELEBOT = os.environ("TOKEN_TELEBOT")

bot = telebot.TeleBot(TOKEN_TELEBOT)


@bot.message_handler(commands=['start'])
def start_cmd(message):
        bot.reply_to(message, 'Я на сервере Heroku')




bot.polling()