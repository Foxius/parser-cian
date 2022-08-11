from bs4 import BeautifulSoup as bs
import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputMediaDocument
import dbw as db
from apscheduler.schedulers.background import BackgroundScheduler
from telebot import types

site = "https://www.cian.ru/cat.php?bbox=55.56107802789372%2C36.63006417453285%2C55.926717332084785%2C38.387876674532855&center=55.74432778739276%2C37.50897042453286&deal_type=sale&engine_version=2&in_polygon[0]=37.6282425_55.9039673%2C37.5939102_55.9039673%2C37.5595779_55.9070683%2C37.5252456_55.9024168%2C37.4936599_55.8954396%2C37.4675674_55.8838108%2C37.4359817_55.8752831%2C37.4126358_55.8613285%2C37.3920364_55.8450483%2C37.3934097_55.825667%2C37.3961563_55.8055105%2C37.3961563_55.7853539%2C37.3810501_55.7682984%2C37.3865432_55.7489172%2C37.3879165_55.7303111%2C37.3975296_55.7109299%2C37.4140091_55.6938743%2C37.4291153_55.6760436%2C37.427742_55.6574376%2C37.4524612_55.6450335%2C37.470314_55.6256523%2C37.4936599_55.6116977%2C37.5156326_55.5961927%2C37.5499649_55.5884402%2C37.5856704_55.5884402%2C37.6200027_55.5837887%2C37.5746841_55.578362%2C37.5417&offer_type=flat&origin=map&polygon_name[0]=default_name_0&zoom=10"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.56'}
page = requests.get(site, headers=headers)
soup = bs(page.content, 'html.parser')
res = soup.find_all("span", {"data-mark": "OfferTitle"})
res1 = soup.find_all("span", {"data-mark": "MainPrice"})
res2 = soup.find_all('a', {"class": "_93444fe79c--link--eoxce"})
pars = [res]
pars1 = [res1]
pars2 = [res2]
# print(res2[1].text)
_l = zip(res, res2)
for i in _l:
    print(f"{i[1].get('href')}")
# _l = zip(res, res1, res2)
# for i in _l:
    # markuup = types.InlineKeyboardMarkup()
    # button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
    # markuup.add(button1)
    # bot.send_message(message.chat.id,f"**Название**: `{i[0].text}`\n**Цена:** `{i[1].text}`\n**Ссылка:** `{i[2].text}`", reply_markup=markup, parse_mode='Markdown')
    # db.add_url(message.chat.id, site, i[1].text)
    # print(f"""Название: {i[0].text}`\nЦена: {i[1].text}\nСсылка:{i[2].text}""")
# for link in soup.find_all('a', {"class": "_93444fe79c--link--eoxce"}):
#     print(link.get('href'))