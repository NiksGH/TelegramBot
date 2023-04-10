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
        btn5 = types.KeyboardButton("Куртки")
        btn6 = types.KeyboardButton("Меню")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.chat.id, "Выберите категорию товара", reply_markup=markup)

    elif message.text == '🗑 Корзина':
        bot.send_message(message.chat.id, "Ваша корзина пуста")

    if message.text == 'Худи':

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Меню', callback_data='qwerty')
        btn2 = types.InlineKeyboardButton('В корзину', callback_data='jjfj')

        markup.add(btn1, btn2)

        bot.send_photo(message.chat.id, photo=open("black.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный \nЦена: 3800₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("emerald.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-зеленый \nЦена: 3500₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("light blue.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-синий \nЦена: 3500₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("red.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: красный \nЦена: 3500₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("spruce.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: еловый \nЦена: 3500₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("white.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: белый \nЦена: 3800₽',
                       reply_markup=markup)

    elif message.text == 'Спортивные штаны':

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Меню', callback_data='qwert1')
        btn2 = types.InlineKeyboardButton('В корзину', callback_data='jjf1')

        markup.add(btn1, btn2)


        bot.send_photo(message.chat.id, photo=open("black_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный \nЦена: 3300₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("emerald_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-зеленый \nЦена: 3000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("light blue_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-синий \nЦена: 3000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("red_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: красный \nЦена: 3000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("spruce_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: еловый \nЦена: 3000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("white_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: белый \nЦена: 3300₽',
                       reply_markup=markup)

    elif message.text == 'Шорты':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Меню', callback_data='qwert12')
        btn2 = types.InlineKeyboardButton('В корзину', callback_data='jjf12')

        markup.add(btn1, btn2)

        bot.send_photo(message.chat.id, photo=open("black_shorts.jpg", 'rb'),
                       caption='Шорты \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный \nЦена: 1300₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("gray_shorts.jpg", 'rb'),
                       caption='Шорты \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: серый \nЦена: 1200₽',
                       reply_markup=markup)

    elif message.text == 'Кросовки':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Меню', callback_data='qwert13')
        btn2 = types.InlineKeyboardButton('В корзину', callback_data='jjf13')

        markup.add(btn1, btn2)

        bot.send_photo(message.chat.id, photo=open("nike_dunks.jpg", 'rb'),
                       caption='Кроссовки Nike Dunk Low \n \nМатериал: 100% кожа \nРазмер: 40-45 \nЦвет: белый, серый \nЦена: 5800₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("nike_air_force.jpg", 'rb'),
                       caption='Кроссовки Nike Air Force \n \nМатериал: 100% кожа \nРазмер: 41-45 \nЦвет: белый \nЦена: 6000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("nike_air_monarh.jpg", 'rb'),
                       caption='Кроссовки Nike Air Monarch \n \nМатериал: 100% кожа \nРазмер: 40-45 \nЦвет: черно-белый \nЦена: 8000₽',
                       reply_markup=markup)

    elif message.text == 'Куртки':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Меню', callback_data='qwert12')
        btn2 = types.InlineKeyboardButton('В корзину', callback_data='jjf12')

        markup.add(btn1, btn2)

        bot.send_photo(message.chat.id, photo=open("black_TNF.jpg", 'rb'),
                       caption='Куртка The North Face \n \nСостав: 100% пух \nРазмер: S, M, L \nЦвет: черный \nЦена: 10000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("gray_shorts.jpg", 'rb'),
                       caption='Куртка The North Face \n \nСостав: 100% пух \nРазмер: S, M, L \nЦвет: белый \nЦена: 10000₽',
                       reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open("black_nike.jpg", 'rb'),
                       caption='Олимпийка Nike \n \nСостав: 100% шерсть \nРазмер: S, M, L \nЦвет: черный \nЦена: 5200₽',
                       reply_markup=markup)

    elif message.text == 'Меню':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🗑 Корзина")
        item2 = types.KeyboardButton("😊 Каталог")

        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Возвращаемся в меню', reply_markup=markup)

bot.infinity_polling()
