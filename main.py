import telebot
from telebot import types

token = '5949952362:AAGaIIqKRz8Hit2paQGViQPoZ9trVME6duw'
bot = telebot.TeleBot(token)

CALLBACK = ['black', 'emerald', 'light blue', 'red', 'spruce', 'white', 'black_pants', 'emerald_pants', 'light blue_pants', 'red_pants', 'spruce_pants', 'white_pants', 'black_shorts', 'gray_shorts', 'nike_dunks', 'nike_air_force', 'nike_air_monarh', 'black_TNF', 'white_TNF', 'black_nike']
cal = {
    'black':'Худи черный',
    'emerald':'Худи светло-зеленый',
    'light blue':'Худи светло-синий',
    'red':'Худи красный',
    'spruce':'Худи еловый',
    'white':'Худи белый',
    'black_pants':'Спортивные штаны черные',
    'emerald_pants':'Спортивные штаны светло-зеленые',
    'light blue_pants':'Спортивные штаны светло-синие',
    'red_pants':'Спортивные штаны красные',
    'spruce_pants':'Спортивные штаны еловые',
    'white_pants':'Спортивные штаны белые',
    'black_shorts':'Шорты черные',
    'gray_shorts':'Шорты серые',
    'nike_dunks':'Кроссовки Nike Dunk Low',
    'nike_air_force':'Кроссовки Nike Air Force',
    'nike_air_monarh':'Кроссовки Nike Air Monarch',
    'black_TNF':'Куртка The North Face черная',
    'white_TNF':'Куртка The North Face белая',
    'black_nike':'Олимпийка Nike черная'
}


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

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='black')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("black.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный \nЦена: 3800₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='emerald')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("emerald.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-зеленый \nЦена: 3500₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='light blue')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("light blue.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-синий \nЦена: 3500₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='red')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("red.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: красный \nЦена: 3500₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='spruce')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("spruce.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: еловый \nЦена: 3500₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='"white')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("white.jpg", 'rb'),
                       caption='Худи \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: белый \nЦена: 3800₽',
                       reply_markup=markup)

    elif message.text == 'Спортивные штаны':

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='black_pants')

        markup.add(btn2)


        bot.send_photo(message.chat.id, photo=open("black_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный \nЦена: 3300₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='emerald_pants')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("emerald_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-зеленый \nЦена: 3000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='light blue_pants')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("light blue_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: светло-синий \nЦена: 3000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='red_pants')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("red_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: красный \nЦена: 3000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='spruce_pants')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("spruce_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: еловый \nЦена: 3000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='white_pants')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("white_pants.jpg", 'rb'),
                       caption='Спортивные штаны \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: белый \nЦена: 3300₽',
                       reply_markup=markup)

    elif message.text == 'Шорты':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='black_shorts')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("black_shorts.jpg", 'rb'),
                       caption='Шорты \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: черный \nЦена: 1300₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='gray_shorts')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("gray_shorts.jpg", 'rb'),
                       caption='Шорты \n \nМатериал: 100% хлопок \nРазмер: S, M, L \nЦвет: серый \nЦена: 1200₽',
                       reply_markup=markup)

    elif message.text == 'Кросовки':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='nike_dunks')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("nike_dunks.jpg", 'rb'),
                       caption='Кроссовки Nike Dunk Low \n \nМатериал: 100% кожа \nРазмер: 40-45 \nЦвет: белый, серый \nЦена: 5800₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='nike_air_force')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("nike_air_force.jpg", 'rb'),
                       caption='Кроссовки Nike Air Force \n \nМатериал: 100% кожа \nРазмер: 41-45 \nЦвет: белый \nЦена: 6000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='nike_air_monarh')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("nike_air_monarh.jpg", 'rb'),
                       caption='Кроссовки Nike Air Monarch \n \nМатериал: 100% кожа \nРазмер: 40-45 \nЦвет: черно-белый \nЦена: 8000₽',
                       reply_markup=markup)

    elif message.text == 'Куртки':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='black_TNF')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("black_TNF.jpg", 'rb'),
                       caption='Куртка The North Face \n \nСостав: 100% пух \nРазмер: S, M, L \nЦвет: черный \nЦена: 10000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='white_TNF')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("white_TNF.jpg", 'rb'),
                       caption='Куртка The North Face \n \nСостав: 100% пух \nРазмер: S, M, L \nЦвет: белый \nЦена: 10000₽',
                       reply_markup=markup)

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('Купить', callback_data='black_nike')

        markup.add(btn2)

        bot.send_photo(message.chat.id, photo=open("black_nike.jpg", 'rb'),
                       caption='Олимпийка Nike \n \nСостав: 100% шерсть \nРазмер: S, M, L \nЦвет: черный \nЦена: 5200₽',
                       reply_markup=markup)

    elif message.text == 'Меню':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🗑 Корзина")
        item2 = types.KeyboardButton("😊 Каталог")

        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Возвращаемся в меню', reply_markup=markup)

    elif message.text == 'Перейти к оформлению заказа' or message.text == 'Указать другой':
        bot.send_message(message.chat.id, 'Укажите адрес доставки')
        bot.register_next_step_handler(message, test)

    elif message.text == "Да верный":
        bot.send_message(message.chat.id, 'Вы можете оплатить заказ удобным для вас способом: \nКарта: 2202 2061 7890 3410 \nQIWI: +79619398580 \n⚠После оплаты с вами свяжется администратор')

def test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да верный")
    item2 = types.KeyboardButton("Указать другой")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"Адрес доставки {message.text}, верно?", reply_markup=markup)


@bot.callback_query_handler(func=lambda c:True)
def call_back(c):
    cid = c.message.chat.id
    if cal[c.data]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Перейти к оформлению заказа")
        item2 = types.KeyboardButton("Меню")

        markup.add(item1, item2)
        bot.send_message(cid, f"Отличный выбор😊 {cal[c.data]}", reply_markup=markup)


bot.infinity_polling()
