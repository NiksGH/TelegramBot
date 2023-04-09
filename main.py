import telebot
from telebot import types

token = '5949952362:AAGaIIqKRz8Hit2paQGViQPoZ9trVME6duw'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🗑 Корзина")
    item2 = types.KeyboardButton("😊 Каталог")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет ✌ \nЯ бот который поможет тебе выбрать одежду на любой вкус)", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu(message):

    if message.text == '😊 Каталог':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Худи")
        btn2 = types.KeyboardButton("Спортивные штаны")
        btn3 = types.KeyboardButton("Шорты")
        btn4 = types.KeyboardButton("Кросовки")
        btn5 = types.KeyboardButton("Носки")
        btn6 = types.KeyboardButton("Куртки")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.chat.id, "Выберите категорию товара", reply_markup=markup)

    elif message.text == '🗑 Корзина':
        bot.send_message(message.chat.id, "Ваша корзина пуста")


@bot.message_handler(content_types=['text'])
def shoe(message):

    if message.text == 'Худи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Меню")
        btn2 = types.KeyboardButton("В корзину")

        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, "Выберите категорию товара", reply_markup=markup)

        bot.send_photo_file(message.chat.id, photo=open("img/black.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный',
                       reply_markup=markup)
        bot.send_photo_file(message.chat.id, photo=open("img/emerald.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-зеленый',
                       reply_markup=markup)
        bot.send_photo_file(message.chat.id, photo=open("img/light blue.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-синий',
                       reply_markup=markup)
        bot.send_photo_file(message.chat.id, photo=open("img/red.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: красный',
                       reply_markup=markup)
        bot.send_photo_file(message.chat.id, photo=open("img/spruce.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: еловый',
                       reply_markup=markup)
        bot.send_photo_file(message.chat.id, photo=open("img/white.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: белый',
                       reply_markup=markup)

    elif message.text == 'Спортивные штаны':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Меню")
        btn2 = types.KeyboardButton("В корзину")

        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, "Выберите категорию товара", reply_markup=markup)

        bot.send_photo(message.chat.id, photo=open("img/black_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("img/emerald_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-зеленый',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("img/light blue_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-синий',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("img/red_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: красный',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("img/spruce_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: еловый',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("img/white_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: белый',
                       reply_markup=markup)

bot.infinity_polling()