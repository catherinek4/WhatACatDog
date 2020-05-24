import telebot
from telebot import *
from telebot.types import InputMediaPhoto
import predict.py
bot = telebot.TeleBot('1216215465:AAFciPgQ-NSXY5e3N32PErhTeuDui91o1C0')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Recognize🔎')
    but2 = types.KeyboardButton('Statistics📊')
    but3 = types.KeyboardButton('Selection🖼')
    markup.add(but1, but2, but3)
    bot.send_message(
        message.chat.id, 'Hello, select the option you need :)', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id, 'To start recognition, enter the /start command.')


@bot.message_handler(content_types=['text'])
def text_message(message):
    text1 = 'Siberian Cat'
    img1 = 'https://imbt.ga/kZ3M2pN28o'
    pic1 = 'https://imbt.ga/kZ3M2pN28o'
    pic2 = 'https://imbt.ga/CVj4MLZHgD'
    pic3 = 'https://imbt.ga/RRuyJ1IBXp'
    pic4 = 'https://imbt.ga/4McNflhMer'
    pic5 = 'https://imbt.ga/mzqNOKJEbD'
    pic6 = 'https://imbt.ga/FHjDC7mNcv'
    pic7 = 'https://imbt.ga/qBNt0X3rLe'
    pic8 = 'https://imbt.ga/9ytmi8TXHr'
    pic9 = 'https://imbt.ga/nZ9WA1P0mU'
    pic10 = 'https://imbt.ga/f4YRgi68xV'
    if message.text == "/help":
        bot.send_message(message.from_user.id,
                         'To start recognition, enter the /start command.')
    elif message.text == "Recognize🔎":
        bot.send_message(
            message.from_user.id, 'Send me a picture of a cat/dog that you want to recognize :)')
    elif message.text == "Statistics📊":
        bot.send_message(message.from_user.id, 'tyt bydet statistika hehe')
    elif message.text == "Selection🖼":
        media = [InputMediaPhoto(pic1, caption="Siberian Cat"),
                 InputMediaPhoto(pic2, caption="British Shorthair Cat")]
        bot.send_media_group(message.chat.id, media)
    else:
        name = message.from_user.first_name
        bot.send_message(message.chat.id, 'Sorry, {0.first_name}... I dont understand you. Enter the /help command, please'.format(message.from_user, bot.get_me()))


@bot.message_handler(content_types=['photo'])
def photo_message(message):
    bot.send_message(message.chat.id, 'Wow, nice photo!' value)


bot.polling(none_stop=True)
