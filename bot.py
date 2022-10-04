import telebot
import os

TOKEN_TELEBOT = os.environ["TOKEN_TELEBOT"]

# TOKEN_WEATHER_API = os.environ['TOKEN_WEATHER_API']

bot = telebot.TeleBot(TOKEN_TELEBOT)

HEROKU = os.environ.get('HEROKU', False)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    if  'Heroku':
        bot.reply_to(message, 'Я на сервере Heroku')
    else:
        bot.reply_to(message, 'Привет!')



bot.polling()