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


@bot.message_handler(commands=['number'])
def number(message: Message):
    bot.reply_to(message, str(random.randint(0, 100)))


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
