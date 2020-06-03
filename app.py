import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
import csv
import sqlite3

#Internal imports
import googleAuth
import signUp
import signIn
from user import User
from request import Request
from db import init_db_command

app = Flask(__name__)
UPLOAD_FOLDER = 'user_images'
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# Naive database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

@app.route('/')
def home():
    return render_template('main.html')

#################### ЕСЛИ ПОСМОТРЕТЬ КАК ОНО РАБОТАЕТ И ЗАПУСТИТЬ У СЕБЯ ########################
@app.route('/', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image_from_user = request.files["image"]
            image_from_user.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image_from_user.filename))
            src = './user_images/' + str(image_from_user.filename) 
            with open('data/csv/cats.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['breed'] == 'bombay':
                        name = row['name']
                        weight = row['weight']
                        life = row['life_exp']
                        country = row['country']
                        height = row['height']
                        colors = row['colors']
                        history = row['history']
                        img_breed1 = f"cats/bombay.jpg"
                        break
                for row in reader:
                    if row['breed'] == 'ragdoll':
                        name2 = row['name']
                        weight2 = row['weight']
                        life2 = row['life_exp']
                        country2 = row['country']
                        height2 = row['height']
                        colors2 = row['colors']
                        history2 = row['history']
                        img_breed2 = f"cats/ragdoll.jpg"
                        break
            create_request(src, name, name2)
    return render_template('result.html', name = name, weight = weight, life = life, country = country, height = height, colors = colors, history = history, name2 = name2, weight2 = weight2, life2 = life2, country2 = country2, height2 = height2, colors2 = colors2, history2 = history2, img_breed2 = img_breed2, img_breed1 = img_breed1)


######################### ТОЛЬКО ЕСЛИ ЕСТЬ TENSORFLOW + CUDA #############################
# import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow
# from tensorflow.python.keras.preprocessing import image
# import subprocess
# from tensorflow.keras.models import load_model

# classifier = load_model('resources/dogcat_model_bak.h5')
# classifier_cat = load_model('resources/cat_model_bak.h5')
# classifier_dog = load_model('resources/dog_model_bak.h5')
# cats = ["abyssinian", "bengal", "birman", "bombay", "british_shorthair", "egyptian_mau",
# "maine_coon", "persian", "ragdoll", "russian_blue", "siamese", "sphynx"]
# dogs = ['tibetan_terrier', 'border_collie', 'dhole', 'clumber', 'pembroke', 'kerry_blue_terrier', 'tibetan_mastiff', 'bedlington_terrier', 'walker_hound', 'black-and-tan_coonhound', 'malamute', 'cardigan', 'schipperke', 'german_short-haired_pointer', 'golden_retriever', 'afghan_hound', 'otterhound', 'african_hunting_dog', 'italian_greyhound', 'great_dane', 'miniature_schnauzer', 'pomeranian', 'border_terrier', 'airedale', 'chihuahua', 'kuvasz', 'chesapeake_bay_retriever', 'miniature_pinscher', 'norwich_terrier', 'french_bulldog', 'ibizan_hound', 'shih-tzu', 'entlebucher', 'samoyed', 'vizsla', 'cocker_spaniel', 'blenheim_spaniel', 'rottweiler', 'whippet', 'groenendael', 'bouvier_des_flandres', 'australian_terrier', 'redbone', 'sussex_spaniel', 'basset', 'standard_poodle', 'flat-coated_retriever', 'chow', 'basenji', 'american_Staffordshire_terrier', 'appenzeller', 'staffordshire_bullterrier', 'soft-coated_wheaten_terrier', 'irish_setter', 'silky_terrier', 'rhodesian_ridgeback', 'weimaraner', 'eskimo_dog', 'briard', 'affenpinscher',
#  'scottish_deerhound', 'yorkshire_terrier', 'pug', 'norwegian_elkhound', 'bloodhound', 'bull_mastiff', 'old_english_sheepdog', 'labrador_retriever', 'saluki', 'giant_schnauzer', 'japanese_spaniel', 'lhasa', 'norfolk_terrier', 'papillon', 'irish_terrier', 'brabancon_griffon', 'irish_wolfhound', 'boxer', 'malinois', 'collie', 'standard_schnauzer', 'german_shepherd', 'beagle', 'english_setter', 'toy_poodle', 'sealyham_terrier', 'west_Highland_white_terrier', 'greater_swiss_mountain_dog', 'dingo', 'english_springer', 'brittany_spaniel', 'maltese_dog', 'curly-coated_retriever', 'doberman', 'shetland_sheepdog', 'lakeland_terrier', 'mexican_hairless', 'saint_bernard', 'english_foxhound', 'borzoi', 'leonberg', 'welsh_springer_spaniel', 'wire-haired_fox_terrier', 'miniature_poodle', 'newfoundland', 'toy_terrier', 'irish_water_spaniel', 'gordon_setter', 'great_pyrenees', 'scotch_terrier', 'siberian_husky', 'komondor', 'bluetick', 'cairn', 'pekinese', 'boston_bull', 'dandie_dinmont', 'kelpie', 'bernese_mountain_dog', 'keeshond']

# @app.route('/', methods=["GET", "POST"])
# def upload_image():
#     if request.method == "POST":
#         if request.files:
#             image_from_user = request.files["image"]
#             image_from_user.save(os.path.join(
#                 app.config["IMAGE_UPLOADS"], image_from_user.filename))
#             src = './user_images/' + str(image_from_user.filename) 
#             img1 = image.load_img(src, target_size=(64, 64))
#             img = image.img_to_array(img1)
#             img = img/255
#             img = np.expand_dims(img, axis=0)
#             prediction = classifier.predict(img, batch_size=None, steps=1)
#             if(prediction[0][0] > 0.5):
#                 value = 'dogs'
#                 prediction_dog = prediction[0, 0]
#                 prediction = classifier_dog.predict(img, batch_size=None, steps=1)

#                 breed = dogs[np.argmax(prediction[0])]
#                 prediction_breed = prediction[0][np.argmax(prediction[0])] * 100
#                 prediction_breed = "{:5.3f}".format(prediction_breed)
#                 firts_breed_index = np.argmax(prediction[0])

#                 arr2 = np.delete(prediction[0], np.argmax(prediction[0]), axis=None)
#                 dogs2 = np.delete(dogs, np.argmax(prediction[0]), axis=None)

#                 breed2 = dogs2[np.argmax(arr2)]
#                 prediction_breed2 = arr2[np.argmax(arr2)] * 100
#                 prediction_breed2 = "{:5.3f}".format(prediction_breed2)
#                 second_breed_index = np.argmax(arr2)
#             else:
#                 value = 'cats'
#                 prediction_cat = 1.0-prediction[0, 0]
#                 prediction = classifier_cat.predict(img, batch_size=None, steps=1)
                
#                 breed = cats[np.argmax(prediction[0])]
#                 prediction_breed = prediction[0][np.argmax(prediction[0])] * 100
#                 prediction_breed = "{:5.3f}".format(prediction_breed)
#                 firts_breed_index = np.argmax(prediction[0])
                
#                 arr2 = np.delete(prediction[0], np.argmax(prediction[0]), axis=None)
#                 cats2 = np.delete(cats, np.argmax(prediction[0]), axis=None)

#                 breed2 = cats2[np.argmax(arr2)]
#                 prediction_breed2 = arr2[np.argmax(arr2)] * 100
#                 prediction_breed2 = "{:5.3f}".format(prediction_breed2)
#                 second_breed_index = np.argmax(arr2)
            
#             path_to_csv = 'data/csv/' + value + '.csv'
          
#             with open(path_to_csv, encoding='utf-8', errors='replace') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     if row['breed'] == breed:
#                         name = row['name']
#                         weight = row['weight']
#                         life = row['life_exp']
#                         country = row['country']
#                         height = row['height']
#                         colors = row['colors']
#                         history = row['history']
#                         img_breed1 = f"{value}/{breed}.jpg"
#                         break
#                 for row in reader:
#                     if row['breed'] == breed2:
#                         name2 = row['name']
#                         weight2 = row['weight']
#                         life2 = row['life_exp']
#                         country2 = row['country']
#                         height2 = row['height']
#                         colors2 = row['colors']
#                         history2 = row['history']
#                         img_breed2 = f"{value}/{breed2}.jpg"
#                         break           
#             return render_template('result.html',prediction_breed = prediction_breed, prediction_breed2 = prediction_breed2, name = name, weight = weight, life = life, country = country, height = height, colors = colors, history = history, name2 = name2, weight2 = weight2, life2 = life2, country2 = country2, height2 = height2, colors2 = colors2, history2 = history2, img_breed2 = img_breed2, img_breed1 = img_breed1)           
#                         #img_breed2 = 'cats/'+str(i)+'.jpg'
                        #break
    	    #create_request(src, name, name2)                
    #return render_template('result.html', name = name, weight = weight, life = life, country = country, height = height, colors = colors, history = history, name2 = name2, weight2 = weight2, life2 = life2, country2 = country2, height2 = height2, colors2 = colors2, history2 = history2, img_breed2 = img_breed2, img_breed1 = img_breed1)

def create_request(image, breed1, breed2):
    user_id = None
    if 'current_user' in session:
        user_id = session['current_user']
    return Request.create(user_id, image, breed1, breed2)
    
@app.route('/header')
def show_header():
    return render_template('header.html')

@app.route('/signUp', methods=["POST", "GET"])
def _signUp():
    if not 'current_user' in session:
        name = request.form['fn']
        email = request.form['email']
        password = request.form['password']
        user = signUp.login(name, email, password)
        session['current_user'] = user.id
    return render_template('main.html')

@app.route('/signIn', methods=["POST", "GET"])
def _signIn():
    if not 'current_user' in session:
        email = request.form['email']
        password = request.form['password']
        user = signIn.login(email, password)
        session['current_user'] = user.id
    return render_template('main.html')

@app.route('/signGoogle')
def _signGoogle():
    return googleAuth.login()

@app.route("/signGoogle/callback")
def callback():
    user = googleAuth.callback()
    session['current_user'] = user.id
    return render_template('main.html')

@app.route("/logout")
def logout():
    session.pop('current_user')
    return render_template('main.html')

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=4826)
    #app.run(ssl_context="adhoc")
    app.run(debug=True)