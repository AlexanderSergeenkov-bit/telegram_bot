import telebot
import random
from telebot import types
from telebot.types import Message

TOKEN = '749206105:AAFOfzQhTDQxU8XPQehkXmilGVGIGIVIp24'
bot = telebot.TeleBot(TOKEN)


with open('phrases.txt', 'r') as f:
    phrases = f.readlines()

phrase = ['Подтверди', 'подтверди', 'повдверди', 'да?']
prase_reply = [
    'угу',
    'ага',
    'подтверждаю',
    'согласен',
]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
               55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
               81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


phrase_number = [
    'зарандомь число',
    'любое число',
    'рандомное число'
]

bad_phrases = [
    'пошел нах',
    'эй ты',
    'живо',
    'иди в жопу',
    'заткнись',
    'ебало офни',
    'додик',
    'даун',
    'мудак',
    'тварь',
    'гад',
    'пидор',
    'дебил',
]

error_phrases = [
    'спиши часики',
    'как успехи',
    'как оно',
    'как дела',
]

keyword = "бот"
keyword2 = "Бот"

bad_phrases_reply = [
    'А повежлевее нельзя!?',
    'Ты чё бык?',
    'Я хоть и бот, но оскорблять меня нельзя',
    'Мне вообще-то обидно',
    'Ты меня оскорбил',
    'Я любил тебя, а ты...',
    'Эх, опять издеваешься',
]


@bot.message_handler(commands=['start', 'help'])
def markup_bot(message: Message):
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=keyboard())


@bot.message_handler(commands=['phrase'])
def send_phrase(message: Message):
    bot.reply_to(message, random.choice(phrases))


@bot.message_handler(commands=['number'])
def number_fun(message: Message):
    bot.reply_to(message, random.choice(number_list))


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    chat_id = message.chat.id
    for c in phrase:
        if (c in message.text):
            bot.reply_to(message, random.choice(prase_reply))
    # elif bad_phrases in message.text:
    #     bot.reply_to(message, "А повежлевее нельзя!?")
    #
    # elif bad_phrases in message.text:
    #     bot.reply_to(message, "Ты чё бык?")
    #
    # elif bad_phrases in message.text:
    #     bot.reply_to(message, "Я хоть и бот, но оскорблять меня нельзя")

    # elif phrase_number[0] in message.text:
    #     bot.reply_to(message, random.choice(number_list))
    #
    # elif phrase_number[1] in message.text:
    #     bot.reply_to(message, random.choice(number_list))
    #
    # elif phrase_number[2] in message.text:
    #     bot.reply_to(message, random.choice(number_list))

    for b in error_phrases:
        if (b in message.text and (keyword in message.text or keyword2 in message.text)):
            bot.reply_to(message, "Лёня, иди нахуй")

    # elif error_phrases[0] in message.text:
    #     bot.reply_to(message, "Пошел нахуй")
    #
    # elif [1] in message.text:
    #     bot.reply_to(message, "Пошел нахуй")
    #
    # elif bad_phrases[2] in message.text:
    #     bot.reply_to(message, "Пошел нахуй")
    #
    # elif bad_phrases[3] in message.text:
    #     bot.reply_to(message, "Пошел нахуй")

    for a in phrase_number:
        if (a in message.text and (keyword in message.text or keyword2 in message.text)):
            bot.reply_to(message, random.choice(number_list))

    for i in bad_phrases:
        if (i in message.text):
            bot.reply_to(message, random.choice(bad_phrases_reply))


@bot.message_handler(content_types=['text'])
def send_anytext(message):
    chat_id = message.chat.id
    if message.text == 'phrase':
        bot.send_message(chat_id, random.choice(phrases), reply_markup=keyboard())


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('/phrase')
    btn2 = types.KeyboardButton('/number')
    markup.add(btn1, btn2)
    return markup



bot.polling()