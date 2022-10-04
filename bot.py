import telebot
import os

TOKEN_TELEBOT = os.environ["TOKEN_TELEBOT"]


bot = telebot.TeleBot(TOKEN_TELEBOT)

IS_HEROKU = os.environ.get('IS_HEROKU', False)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    if 'IS_HEROKU':
        bot.reply_to(message, 'Я на сервере Heroku')
    else:
        bot.reply_to(message, 'Привет!')



bot.polling()