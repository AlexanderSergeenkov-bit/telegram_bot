import telebot
import random
from telebot import types
from telebot.types import Message

TOKEN = '749206105:AAFOfzQhTDQxU8XPQehkXmilGVGIGIVIp24'
bot = telebot.TeleBot(TOKEN)

with open('phrases.txt', 'r') as f:
    phrases = f.readlines()

with open('sql/phrases/love.txt', 'r') as f:
    phrases_love = f.readlines()

with open('sql/phrases/friendship.txt', 'r') as f:
    phrases_friendship = f.readlines()

with open('sql/phrases/life.txt', 'r') as f:
    phrases_life = f.readlines()

phrase = ['Подтверди', 'подтверди', 'повдверди', 'да?', 'согласен?']
prase_reply = [
    'угу',
    'ага',
    'подтверждаю',
    'согласен',
]

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
    'лох',
    'педик',
    'гомосек',
]

error_phrases = [
    'спиши часики',
    'как успехи',
    'как оно',
    'как дела',
]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
               55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
               81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
               106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
               127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147,
               148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
               169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189,
               190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210,
               211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231,
               232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252,
               253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273,
               274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294,
               295, 296, 297, 298, 299, 300]

keyword = "бот"
keyword2 = "Бот"

phrase_love_key = 'Любовь'
phrases_friendship_key = 'Дружба'
phrases_life_key = 'Жизнь'

bad_phrases_reply = [
    'А повежлевее нельзя!?',
    'Ты чё бык?',
    'Я хоть и бот, но оскорблять меня нельзя',
    'Мне вообще-то обидно',
    'Ты меня оскорбил',
    'Я любил тебя, а ты...',
    'Эх, опять издеваешься',
    'Ты офигел?',
    'Чё ещё скажешь?',
    'Что-то не нравится?',
    'Ну и чё',
]


@bot.message_handler(commands=['start', 'help'])
def markup_bot(message: Message):
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=keyboard())


@bot.message_handler(commands=['phrase'])
def send_phrase(message: Message):
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=phrase_keyboard())


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    if phrase_love_key in message.text:
        bot.reply_to(message, random.choice(phrases_love))

    elif phrases_friendship_key in message.text:
        bot.reply_to(message, random.choice(phrases_friendship))

    elif phrases_life_key in message.text:
        bot.reply_to(message, random.choice(phrases_life))


@bot.message_handler(commands=['number'])
def number_fun(message: Message):
    bot.reply_to(message, random.choice(number_list))



@bot.message_handler(content_types=['document', 'audio', 'photo', 'sticker', 'video'])
def reply_to_doc(message: Message):
    bot.reply_to(message, "Ну блин, давай текст, я такое не умею")


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
            bot.reply_to(message, "Лёня, Саша работает, иди нахуй")

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


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('/phrase')
    btn2 = types.KeyboardButton('/number')
    markup.add(btn1, btn2)
    return markup


def phrase_keyboard():
    markkup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Любовь')
    btn2 = types.KeyboardButton('Жизнь')
    btn3 = types.KeyboardButton('Дружба')
    markkup.add(btn1, btn2, btn3)
    return markkup


bot.polling()
