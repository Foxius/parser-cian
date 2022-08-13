# parser-cian
[![GitHub issues](https://img.shields.io/github/issues/Foxius/parser-cian?style=plastic)](https://github.com/Foxius/parser-cian/issues) [![GitHub stars](https://img.shields.io/github/stars/Foxius/parser-cian)](https://github.com/Foxius/parser-cian/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Foxius/parser-cian)](https://github.com/Foxius/parser-cian/network) 

**Описание проекта:** Бот парсит квартиры по фильтру, выводит данные в телеграмм бота и проверяет изменения цены

## Алгоритм работы с репозиторием для разработчика

1 - Открываем файл `parser.py`

2 - В 10 строке (выделенной рамкой из комментариев) меняем значение токена на свое, полученое в BotFather. Получится нечто: `bot = telebot.TeleBot('цифарки:оченьмногослучайныхбуквнаанглийском')`

## Алгоритм работы с репозиторием для юзера

1 - Заходим на https://www.cian.ru 

2 - В меню выставляем нужные значения

![photorepo1](https://media.discordapp.net/attachments/927545383612203018/1007967440212349010/unknown.png?width=1006&height=473)

3 - Получаем ссылку фильтра, которую копируем к себе в буфер обмена

![photorepo2](https://media.discordapp.net/attachments/927545383612203018/1007968004493025292/unknown.png?width=1025&height=259)

4 - Переходим в бота Телеграмм, начинаем диалог и нажимаем на кнопку "Спарсить"

![photorepo3](https://media.discordapp.net/attachments/927545383612203018/1007969190176641066/unknown.png)
