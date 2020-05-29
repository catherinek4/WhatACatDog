<h1>Краткое описание:</h1>
TODO:</br>
- вебсайт + соединение с питоном + с бд</br>
- телебот (загрузка на сервер)</br>
- загрузка на сервер сайта</br>
</br></br>
Фото должно быть формата .jpg. Сперва определяется вероятность того, собака это или кот, затем вызывается модель распознавания породы
кота или собаки.</br>
Все фотографии сжимаются, размер во время обработки становится 64*64 пикселя. Точность распознавания вида животного (кот или собака) = 97%,
точность распознавания породы животного = 60%.</br>
Модели имеют формат .h5 (бинарные файлы, в них НЕ записан код, лучше их не открывать). </br>
Основной файл, который следует запускать - predict.py. В нем не создаются модели, а уже используются ранее созданные. 

Всего 12 пород котов (ибо изображения переводятся в чб, породы котов смешиваются и тяжело распознать в отличии от собак), 120 пород собак.


<h3>Породы котов</h3>- ["Abyssinian", "Bengal", "Birman", "Bombay", "British Shorthair", "Egyptian Mau", "Maine Coon", "Persian", "Ragdoll", "Russian Blue", "Siamese", "Sphynx"] </br></br>
<h3>Породы собак</h3>-  ['Tibetan_terrier', 'Border_collie', 'dhole', 'clumber', 'Pembroke', 'Kerry_blue_terrier', 'Tibetan_mastiff', 'Bedlington_terrier', 'Walker_hound', 'black-and-tan_coonhound', 'malamute', 'Cardigan', 'schipperke', 'German_short-haired_pointer', 'golden_retriever', 'Afghan_hound', 'otterhound', 'African_hunting_dog', 'Italian_greyhound', 'Great_Dane', 'miniature_schnauzer', 'Pomeranian', 'Border_terrier', 'Airedale', 'Chihuahua', 'kuvasz', 'Chesapeake_Bay_retriever', 'miniature_pinscher', 'Norwich_terrier', 'French_bulldog', 'Ibizan_hound', 'Shih-Tzu', 'EntleBucher', 'Samoyed', 'vizsla', 'cocker_spaniel', 'Blenheim_spaniel', 'Rottweiler', 'whippet', 'groenendael', 'Bouvier_des_Flandres', 'Australian_terrier', 'redbone', 'Sussex_spaniel', 'basset', 'standard_poodle', 'flat-coated_retriever', 'chow', 'basenji', 'American_Staffordshire_terrier', 'Appenzeller', 'Staffordshire_bullterrier', 'soft-coated_wheaten_terrier', 'Irish_setter', 'silky_terrier', 'Rhodesian_ridgeback', 'Weimaraner', 'Eskimo_dog', 'briard', 'affenpinscher', 'Scottish_deerhound', 'Yorkshire_terrier', 'pug', 'Norwegian_elkhound', 'bloodhound', 'bull_mastiff', 'Old_English_sheepdog', 'Labrador_retriever', 'Saluki', 'giant_schnauzer', 'Japanese_spaniel', 'Lhasa', 'Norfolk_terrier', 'papillon', 'Irish_terrier', 'Brabancon_griffon', 'Irish_wolfhound', 'boxer', 'malinois', 'collie', 'standard_schnauzer', 'German_shepherd', 'beagle', 'English_setter', 'toy_poodle', 'Sealyham_terrier', 'West_Highland_white_terrier', 'Greater_Swiss_Mountain_dog', 'dingo', 'English_springer', 'Brittany_spaniel', 'Maltese_dog', 'curly-coated_retriever', 'Doberman', 'Shetland_sheepdog', 'Lakeland_terrier', 'Mexican_hairless', 'Saint_Bernard', 'English_foxhound', 'borzoi', 'Leonberg', 'Welsh_springer_spaniel', 'wire-haired_fox_terrier', 'miniature_poodle', 'Newfoundland', 'toy_terrier', 'Irish_water_spaniel', 'Gordon_setter', 'Great_Pyrenees', 'Scotch_terrier', 'Siberian_husky', 'komondor', 'bluetick', 'cairn', 'Pekinese', 'Boston_bull', 'Dandie_Dinmont', 'kelpie', 'Bernese_mountain_dog', 'keeshond'] 


