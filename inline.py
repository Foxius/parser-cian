import telebot
from telebot import types # для указание типов


bot = telebot.TeleBot('5327867700:AAFTaMS5oatwdxXIfB6AVNuDX3x9ZWxwGyQ') # токен лежит в файле config.py

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
bot.polling(none_stop=True)