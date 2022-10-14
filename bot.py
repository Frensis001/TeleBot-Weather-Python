import telebot
import os
from bot_pogoda import weather_api



TOKEN_TELEBOT = os.environ["TOKEN_TELEBOT"]

bot = telebot.TeleBot(TOKEN_TELEBOT)


@bot.message_handler(commands=['start'])
def start_cmd(message):
        user_name = message.from_user.first_name
        bot.send_message(message.from_user.id, 'Привет ' + user_name + "\nЭто телеграм бот погоды\nВведите город ")


@bot.message_handler(func=lambda message: True)
def weather_call(message):
        Cyti = message.text.lower()
        bot.reply_to(message, weather_api(Cyti))
        print(message.text)

bot.polling()