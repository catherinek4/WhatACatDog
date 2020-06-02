import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import csv
# import numpy as np
# import matplotlib.pyplot as plt
# import tensorflow
# from tensorflow.python.keras.preprocessing import image
# import subprocess
# from tensorflow.keras.models import load_model

# classifier = load_model('resources/dogcat_model_bak.h5')
# classifier_cat = load_model('resources/cat_model_bak.h5')
# classifier_dog = load_model('resources/dog_model_bak.h5')
# cats = ["Abyssinian", "Bengal", "Birman", "Bombay", "British Shorthair", "Egyptian Mau",
# "Maine Coon", "Persian", "Ragdoll", "Russian Blue", "Siamese", "Sphynx"]
# dogs = ['Tibetan_terrier', 'Border_collie', 'dhole', 'clumber', 'Pembroke', 'Kerry_blue_terrier', 'Tibetan_mastiff', 'Bedlington_terrier', 'Walker_hound', 'black-and-tan_coonhound', 'malamute', 'Cardigan', 'schipperke', 'German_short-haired_pointer', 'golden_retriever', 'Afghan_hound', 'otterhound', 'African_hunting_dog', 'Italian_greyhound', 'Great_Dane', 'miniature_schnauzer', 'Pomeranian', 'Border_terrier', 'Airedale', 'Chihuahua', 'kuvasz', 'Chesapeake_Bay_retriever', 'miniature_pinscher', 'Norwich_terrier', 'French_bulldog', 'Ibizan_hound', 'Shih-Tzu', 'EntleBucher', 'Samoyed', 'vizsla', 'cocker_spaniel', 'Blenheim_spaniel', 'Rottweiler', 'whippet', 'groenendael', 'Bouvier_des_Flandres', 'Australian_terrier', 'redbone', 'Sussex_spaniel', 'basset', 'standard_poodle', 'flat-coated_retriever', 'chow', 'basenji', 'American_Staffordshire_terrier', 'Appenzeller', 'Staffordshire_bullterrier', 'soft-coated_wheaten_terrier', 'Irish_setter', 'silky_terrier', 'Rhodesian_ridgeback', 'Weimaraner', 'Eskimo_dog', 'briard', 'affenpinscher',
#  'Scottish_deerhound', 'Yorkshire_terrier', 'pug', 'Norwegian_elkhound', 'bloodhound', 'bull_mastiff', 'Old_English_sheepdog', 'Labrador_retriever', 'Saluki', 'giant_schnauzer', 'Japanese_spaniel', 'Lhasa', 'Norfolk_terrier', 'papillon', 'Irish_terrier', 'Brabancon_griffon', 'Irish_wolfhound', 'boxer', 'malinois', 'collie', 'standard_schnauzer', 'German_shepherd', 'beagle', 'English_setter', 'toy_poodle', 'Sealyham_terrier', 'West_Highland_white_terrier', 'Greater_Swiss_Mountain_dog', 'dingo', 'English_springer', 'Brittany_spaniel', 'Maltese_dog', 'curly-coated_retriever', 'Doberman', 'Shetland_sheepdog', 'Lakeland_terrier', 'Mexican_hairless', 'Saint_Bernard', 'English_foxhound', 'borzoi', 'Leonberg', 'Welsh_springer_spaniel', 'wire-haired_fox_terrier', 'miniature_poodle', 'Newfoundland', 'toy_terrier', 'Irish_water_spaniel', 'Gordon_setter', 'Great_Pyrenees', 'Scotch_terrier', 'Siberian_husky', 'komondor', 'bluetick', 'cairn', 'Pekinese', 'Boston_bull', 'Dandie_Dinmont', 'kelpie', 'Bernese_mountain_dog', 'keeshond']
import googleAuth
import signUp
import signIn
from user import User
from request import Request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
UPLOAD_FOLDER = 'user_images'

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_email):
    return User.getByEmail(user_email)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image_from_user = request.files["image"]
            image_from_user.save(os.path.join(
                app.config["IMAGE_UPLOADS"], str((image_from_user.filename).decode('utf-8'))))
            src = './user_images/' + str((image_from_user.filename).decode('utf-8'))
            ind = 3
            with open('data/csv/cats.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for i, row in enumerate(reader):
                    if i == 3:
                        name = row['name']
                        weight = row['weight']
                        life = row['life_exp']
                        country = row['country']
                        height = row['height']
                        colors = row['colors']
                        history = row['history']
                        img_breed1 = 'cats/'+str(i)+'.jpg'
                        break
                for i, row in enumerate(reader):
                    if i == 5:
                        name2 = row['name']
                        weight2 = row['weight']
                        life2 = row['life_exp']
                        country2 = row['country']
                        height2 = row['height']
                        colors2 = row['colors']
                        history2 = row['history']
                        img_breed2 = 'cats/'+str(i)+'.jpg'
                        break
    	    create_request(src, name, name2)                
    return render_template('result.html', name = name, weight = weight, life = life, country = country, height = height, colors = colors, history = history, name2 = name2, weight2 = weight2, life2 = life2, country2 = country2, height2 = height2, colors2 = colors2, history2 = history2, img_breed2 = img_breed2, img_breed1 = img_breed1)

def create_request(image, breed1, breed2):
    user_id = None
    if not current_user.is_authenticated:
	user_id = current_user.id
    return Request.create(user_id, image, breed1, breed2)
    
@app.route('/header/')
def show_header():
    return render_template('header.html')


@app.route('/signUp/', methods=["GET", "POST"])
def _signUp():
    name = request.form['fn']
    email = request.form['email']
    password = request.form['password']
    return signUp.login(name, email, password)


@app.route('/signIn/', methods=["GET", "POST"])
def _signIn():
    email = request.form['email']
    password = request.form['password']
    return signIn.login(email, password)

@app.route('/signGoogle')
def _signGoogle():
    return googleAuth.login()

@app.route("/signGoogle/callback")
def callback():
    return googleAuth.callback()

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=4826)
    app.run(ssl_context="adhoc")
