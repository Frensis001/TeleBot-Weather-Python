import telebot

token = '5719352624:AAE91fHqkvC_tT9fnKmAQIZyy_9jc07u6_k'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_cmd(message):
        bot.reply_to(message, 'Я на сервере Heroku')




bot.polling()