from tensorflow.keras.models import load_model
classifier = load_model('resources/dogcat_model_bak.h5')
classifier_cat = load_model('resources/cat_model_bak.h5')
classifier_dog = load_model('resources/dog_model_bak.h5')
cats = ["Abyssinian", "Bengal", "Birman", "Bombay", "British Shorthair", "Egyptian Mau", "Maine Coon", "Persian", "Ragdoll", "Russian Blue", "Siamese", "Sphynx"]
dogs = ['Tibetan_terrier', 'Border_collie', 'dhole', 'clumber', 'Pembroke', 'Kerry_blue_terrier', 'Tibetan_mastiff', 'Bedlington_terrier', 'Walker_hound', 'black-and-tan_coonhound', 'malamute', 'Cardigan', 'schipperke', 'German_short-haired_pointer', 'golden_retriever', 'Afghan_hound', 'otterhound', 'African_hunting_dog', 'Italian_greyhound', 'Great_Dane', 'miniature_schnauzer', 'Pomeranian', 'Border_terrier', 'Airedale', 'Chihuahua', 'kuvasz', 'Chesapeake_Bay_retriever', 'miniature_pinscher', 'Norwich_terrier', 'French_bulldog', 'Ibizan_hound', 'Shih-Tzu', 'EntleBucher', 'Samoyed', 'vizsla', 'cocker_spaniel', 'Blenheim_spaniel', 'Rottweiler', 'whippet', 'groenendael', 'Bouvier_des_Flandres', 'Australian_terrier', 'redbone', 'Sussex_spaniel', 'basset', 'standard_poodle', 'flat-coated_retriever', 'chow', 'basenji', 'American_Staffordshire_terrier', 'Appenzeller', 'Staffordshire_bullterrier', 'soft-coated_wheaten_terrier', 'Irish_setter', 'silky_terrier', 'Rhodesian_ridgeback', 'Weimaraner', 'Eskimo_dog', 'briard', 'affenpinscher', 'Scottish_deerhound', 'Yorkshire_terrier', 'pug', 'Norwegian_elkhound', 'bloodhound', 'bull_mastiff', 'Old_English_sheepdog', 'Labrador_retriever', 'Saluki', 'giant_schnauzer', 'Japanese_spaniel', 'Lhasa', 'Norfolk_terrier', 'papillon', 'Irish_terrier', 'Brabancon_griffon', 'Irish_wolfhound', 'boxer', 'malinois', 'collie', 'standard_schnauzer', 'German_shepherd', 'beagle', 'English_setter', 'toy_poodle', 'Sealyham_terrier', 'West_Highland_white_terrier', 'Greater_Swiss_Mountain_dog', 'dingo', 'English_springer', 'Brittany_spaniel', 'Maltese_dog', 'curly-coated_retriever', 'Doberman', 'Shetland_sheepdog', 'Lakeland_terrier', 'Mexican_hairless', 'Saint_Bernard', 'English_foxhound', 'borzoi', 'Leonberg', 'Welsh_springer_spaniel', 'wire-haired_fox_terrier', 'miniature_poodle', 'Newfoundland', 'toy_terrier', 'Irish_water_spaniel', 'Gordon_setter', 'Great_Pyrenees', 'Scotch_terrier', 'Siberian_husky', 'komondor', 'bluetick', 'cairn', 'Pekinese', 'Boston_bull', 'Dandie_Dinmont', 'kelpie', 'Bernese_mountain_dog', 'keeshond'] 
import tensorflow
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
img1 = image.load_img('br.jpg', target_size=(64, 64))
img = image.img_to_array(img1)
img = img/255
# create a batch of size 1 [N,H,W,C]
img = np.expand_dims(img, axis=0)
prediction = classifier.predict(img, batch_size=None,steps=1) #gives all class prob.
print(prediction)
if(prediction[0][0]>0.5):
    value ='Dog :%1.2f'%(prediction[0,0])
    plt.text(0, 62,value,color='red',fontsize=10,bbox=dict(facecolor='white',alpha=0.8))
    prediction = classifier_dog.predict(img, batch_size=None,steps=1)
    print(prediction[0])
    print(np.argmax(prediction[0]))
    value =dogs[np.argmax(prediction[0])] + ' :%1.10f'%(prediction[0][np.argmax(prediction[0])])
    plt.text(40, 62,value,color='red',fontsize=10,bbox=dict(facecolor='white',alpha=0.8))
else:
    value ='Cat :%1.2f'%(1.0-prediction[0,0])
    plt.text(0, 62,value,color='red',fontsize=10,bbox=dict(facecolor='white',alpha=0.8))
    prediction = classifier_cat.predict(img, batch_size=None,steps=1)
    print(prediction[0])
    print(np.argmax(prediction[0]))
    value =cats[np.argmax(prediction[0])] + ' :%1.10f'%(prediction[0][np.argmax(prediction[0])])
    plt.text(40, 62,value,color='red',fontsize=10,bbox=dict(facecolor='white',alpha=0.8))

plt.imshow(img1)
plt.show()
