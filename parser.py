from bs4 import BeautifulSoup as bs
import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
import dbw as db
from apscheduler.schedulers.background import BackgroundScheduler
from telebot import types

########################################################################
bot = telebot.TeleBot('5774853485:HJGBJHVBjkvjkghVJKVjkvjhVJHvjkvigud')#
########################################################################
markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
markup.add('Спарсить')


@bot.message_handler(commands=['start'])
def start(message):
    db.add_user(message.chat.id)
    bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=markup)

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    if message.text == "Спарсить":
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Введите ссылку: '), parser)

def parser(message):
    site = message.text
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.56'}
    page = requests.get(site, headers=headers)
    soup = bs(page.content, 'html.parser')
    res = soup.find_all("span", {"data-mark": "OfferTitle"})
    res1 = soup.find_all("span", {"data-mark": "MainPrice"})
    res2 = soup.find_all("a", {"class": "_93444fe79c--link--eoxce"})
    _l = zip(res, res1, res2)
    for i in _l:
        # markuup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
        # markuup.add(button1)
        bot.send_message(message.chat.id,f"**Название**: [{i[0].text}]({i[2].get('href')})\n**Цена:** `{i[1].text}`", reply_markup=markup, parse_mode='Markdown')
        # db.add_url(message.chat.id, site, i[1].text)



# def parse(url):
#     site = message.text
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.56'}
#     page = requests.get(site, headers=headers)
#     soup = bs(page.content, 'html.parser')
#     res = soup.find_all("span", {"data-mark": "OfferTitle"})
#     res1 = soup.find_all("span", {"data-mark": "MainPrice"})
#     
#     _l = zip(res, res1)
#     for i in _l:
#         return (i[0].text, i[1].text)
#         print (i[0].text, i[1].text)

def parse_and_report():
    alls = dbw.get_all()
    for e in alls:
        name, amount = parse(e[0])
        if amount != e[2]: #<<< вот здесь установить цену в формате "150000"
            bot.send_message(e[1], f'Обновление!\nНазвание: {name}\nСтарая цена: {e[2]}\nНовая цена: {amount}')






if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(parse_and_report, 'interval', hours=6)
    scheduler.start()
    bot.infinity_polling()
