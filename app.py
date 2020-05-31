import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
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


UPLOAD_FOLDER = 'user_images'

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image_from_user = request.files["image"]
            image_from_user.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image_from_user.filename))
            src = './user_images/' + str(image_from_user.filename)
            '''
            img1 = image.load_img(src, target_size=(64, 64))
            img = image.img_to_array(img1)
            img = img/255
            img = np.expand_dims(img, axis=0)
            prediction = classifier.predict(img, batch_size=None, steps=1)
            if prediction[0][0] > 0.5:
                value = 'Dog'
            else:
                value = 'Cat'
            return value
            '''
    return render_template('main.html')


@app.route('/header/')
def show_header():
    return render_template('header.html')


@app.route('/signUp/')
def show_signUp():
    return render_template('signUp.html')


@app.route('/signIn/')
def show_signIn():
    return render_template('signIn.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4567)
