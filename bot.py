import telebot
import os
from bot_pogoda import weather_api
import redis

redis_db = redis.from_url.(os.environ.get(''))

TOKEN_TELEBOT = os.environ["TOKEN_TELEBOT"]

bot = telebot.TeleBot(TOKEN_TELEBOT)


@bot.message_handler(commands=['start'])
def start_cmd(message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        bot.reply_to(message, 'Привет ' + user_name + "\nЭто телеграм бот погоды\nВведите город на Английском Пример:'Moscow'")
        print(user_name, user_id,)
        print(message)
@bot.message_handler(func=lambda message: True)
def weather_call(message):
        Cyti = message.text.lower()
        bot.reply_to(message, weather_api(Cyti))

bot.polling()