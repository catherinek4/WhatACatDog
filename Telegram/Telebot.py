
import numpy as np
import matplotlib.pyplot as plt
import tensorflow
from tensorflow.python.keras.preprocessing import image
import telebot
import requests
from telebot import *
from telebot.types import InputMediaPhoto
import urllib.request
import subprocess
import datetime
import os
from os import environ
from tensorflow.keras.models import load_model
classifier = load_model('resources/dogcat_model_bak.h5')
classifier_cat = load_model('resources/cat_model_bak.h5')
classifier_dog = load_model('resources/dog_model_bak.h5')
cats = ["Abyssinian", "Bengal", "Birman", "Bombay", "British Shorthair", "Egyptian Mau",
        "Maine Coon", "Persian", "Ragdoll", "Russian Blue", "Siamese", "Sphynx"]
dogs = ['Tibetan_terrier', 'Border_collie', 'dhole', 'clumber', 'Pembroke', 'Kerry_blue_terrier', 'Tibetan_mastiff', 'Bedlington_terrier', 'Walker_hound', 'black-and-tan_coonhound', 'malamute', 'Cardigan', 'schipperke', 'German_short-haired_pointer', 'golden_retriever', 'Afghan_hound', 'otterhound', 'African_hunting_dog', 'Italian_greyhound', 'Great_Dane', 'miniature_schnauzer', 'Pomeranian', 'Border_terrier', 'Airedale', 'Chihuahua', 'kuvasz', 'Chesapeake_Bay_retriever', 'miniature_pinscher', 'Norwich_terrier', 'French_bulldog', 'Ibizan_hound', 'Shih-Tzu', 'EntleBucher', 'Samoyed', 'vizsla', 'cocker_spaniel', 'Blenheim_spaniel', 'Rottweiler', 'whippet', 'groenendael', 'Bouvier_des_Flandres', 'Australian_terrier', 'redbone', 'Sussex_spaniel', 'basset', 'standard_poodle', 'flat-coated_retriever', 'chow', 'basenji', 'American_Staffordshire_terrier', 'Appenzeller', 'Staffordshire_bullterrier', 'soft-coated_wheaten_terrier', 'Irish_setter', 'silky_terrier', 'Rhodesian_ridgeback', 'Weimaraner', 'Eskimo_dog', 'briard', 'affenpinscher',
        'Scottish_deerhound', 'Yorkshire_terrier', 'pug', 'Norwegian_elkhound', 'bloodhound', 'bull_mastiff', 'Old_English_sheepdog', 'Labrador_retriever', 'Saluki', 'giant_schnauzer', 'Japanese_spaniel', 'Lhasa', 'Norfolk_terrier', 'papillon', 'Irish_terrier', 'Brabancon_griffon', 'Irish_wolfhound', 'boxer', 'malinois', 'collie', 'standard_schnauzer', 'German_shepherd', 'beagle', 'English_setter', 'toy_poodle', 'Sealyham_terrier', 'West_Highland_white_terrier', 'Greater_Swiss_Mountain_dog', 'dingo', 'English_springer', 'Brittany_spaniel', 'Maltese_dog', 'curly-coated_retriever', 'Doberman', 'Shetland_sheepdog', 'Lakeland_terrier', 'Mexican_hairless', 'Saint_Bernard', 'English_foxhound', 'borzoi', 'Leonberg', 'Welsh_springer_spaniel', 'wire-haired_fox_terrier', 'miniature_poodle', 'Newfoundland', 'toy_terrier', 'Irish_water_spaniel', 'Gordon_setter', 'Great_Pyrenees', 'Scotch_terrier', 'Siberian_husky', 'komondor', 'bluetick', 'cairn', 'Pekinese', 'Boston_bull', 'Dandie_Dinmont', 'kelpie', 'Bernese_mountain_dog', 'keeshond']

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
        bot.send_message(
            bot.send_message(message.chat.id, 'Sorry, {0.first_name}... I dont understand you. Enter the /help command, please'.format(message.from_user, bot.get_me()))


@bot.message_handler(content_types=['photo'])



@bot.message_handler(content_types=['photo'])
def handle(message):
    log_request(message)

    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = './user_images/' + message.photo[1].file_id + ".jpg"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, '🔥 Analyzing image, be patient ! 🔥')
    image_name = save_image_from_message(message)
    img1 = image.load_img(src, target_size=(64, 64))
    img = image.img_to_array(img1)
    img = img/255
    img = np.expand_dims(img, axis=0)
    prediction = classifier.predict(img, batch_size=None, steps=1)
    if(prediction[0][0] > 0.5):
        value = 'Dog'
        prediction_dog = prediction[0, 0]
        prediction = classifier_dog.predict(img, batch_size=None, steps=1)
        breed = dogs[np.argmax(prediction[0])]
        prediction_breed = prediction[0][np.argmax(prediction[0])]
        bot.send_message(message.chat.id, f'This is a {value}')
        bot.send_message(
            message.chat.id, f'The probability is {prediction_dog*100}%')

        arr2 = np.delete(prediction[0], np.argmax(prediction[0]), axis=None)

        breed2 = dogs[np.argmax(arr2)]
        prediction_breed2 = arr2[np.argmax(arr2)]

        if prediction_breed == 0.0:
            prediction_breed = 0.01
        if prediction_breed2 == 0.0:
            prediction_breed2 = 0.01

        bot.send_message(
            message.chat.id, f'It can be:\n\n1.{breed}, the probability: {prediction_breed*100}%\n\n2.{breed2}, the probability: {prediction_breed2*100}%')
    else:
        value = 'Cat'
        prediction_cat = 1.0-prediction[0, 0]
        prediction = classifier_cat.predict(img, batch_size=None, steps=1)
        breed = cats[np.argmax(prediction[0])]
        prediction_breed = prediction[0][np.argmax(prediction[0])]
        bot.send_message(message.chat.id, f'This is a {value}')
        bot.send_message(
            message.chat.id, f'The probability is {prediction_cat*100}%')
        arr2 = np.delete(prediction[0], np.argmax(prediction[0]), axis=None)
        breed2 = cats[np.argmax(arr2)]
        prediction_breed2 = arr2[np.argmax(arr2)]

        if prediction_breed == 0.0:
            prediction_breed = 0.01
        if prediction_breed2 == 0.0:
            prediction_breed2 = 0.01

        bot.send_message(
            message.chat.id, f'It can be:\n\n1.{breed}, the probability: {prediction_breed*100}%\n\n2.{breed2}, the probability: {prediction_breed2*100}%')


def log_request(message):
    file = open('logs.txt', 'a')
    file.write("{0} - {1} {2} [{3}]\n".format(datetime.datetime.now(),
                                              message.from_user.first_name, message.from_user.last_name, message.from_user.id))
    print("{0} - {1} {2} [{3}]".format(datetime.datetime.now(),
                                       message.from_user.first_name, message.from_user.last_name, message.from_user.id))
    file.close()


def save_image_from_message(message):
    cid = message.chat.id
    image_id = get_image_id_from_message(message)
    file_path = bot.get_file(image_id).file_path
    image_name = "{0}.jpg".format(image_id)
    return image_name


def get_image_id_from_message(message):
    return message.photo[len(message.photo)-1].file_id


@bot.message_handler(content_types=['document', 'audio'])
def document_message(message):
    bot.send_message(message.from_user.id,
                     'Please send the image for recognition as a photo, not as a file☺️')


bot.polling(none_stop=True)
