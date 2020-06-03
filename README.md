<h1>WhatACat?Dog project</h1></br>
<div>
<h3>Introduction</h3>
Our task was to recognize a breed of a cat or a dog. We used 2 datasets for distinguishing these breeds. The first one is called The Oxford-IIIT PET dataset. There is a collection of 2371 images of cats and 12 cat breeds in general. The second dataset is the Stanford Dogs Dataset with 120 breeds. For each breed class there are ~150 images. So the content of the dataset is quite huge as the number of total images is 20,580. 
</div>

<div>
  <h3>Recognition Model</h3>
  Our Neural Network receives an input (one single vector with 64*64 values) and transforms it using a series of hidden layers. The last layer is a fully-connected layer and is called the output layer. For making a Recongnition Model we took into account Convolutional Neural Networks because of the fact it has a sensible architecture and each neuron is arranged in 3 dimensions: width, height, and depth. <br/>
  For initializing the model we applied the Sequential method:</br>
  classifier = Sequential()
  </br>
We used 4 main types of layers to build a model: Convolutional, Pooling, Flattening and Fully-Connected Layer Layers.
</br>
<h4>Convolutional Layer</h4>
This is the main layer because it is used to reduce the size of an image and make the process of breeds recognition easier and faster.
If an image is too big, some of the main features are lost because the image is compressed to the shape of (64, 64) pixels. But for preventing such loss of image information we used feature maps. As a result, each cat or dog has a unique map feature location for identifying it.</br>
classifier.add(Convolution2D(32, 3, 3, input_shape = (256, 256, 3), activation='relu'))</br>
<h4>Pooling Layer</h4>
Pooling enables us to classify breeds irrespective of the difference in lighting and the number of edges. Max pooling works to preserve the main features while also reducing the size of the image. </br>
classifier.add(MaxPooling2D(pool_size=(2,2)))</br>
<h4>Flattening Layer</h4>
Once the pooled featured map is obtained, the next step is to flatten it. Flattening involves transforming the entire pooled feature map matrix into a single column which is then fed to the neural network for processing.</br>
classifier.add(Flatten())</br>
<h4> Fully-Connected Layer</h4>
The output layer the Fully-Connected Layer and here we get the predicted classes. The information is passed through the network and the error of prediction is calculated. The error is then back propagated through the system to improve the prediction.</br>
classifier.add(Dense(output_dim = 128, activation='relu'))</br>
classifier.add(Dense(output_dim=1, activation='sigmoid'))</br>
 </div>
 
 <div>
  <h3>Telegram Bot</h3>
  Our Telegram Bot is able to receive user images and send messages with a result of breed recognition. The process of detection of a breed takes at least 3 seconds. A user can press one of three main buttons - Recognize, Statistics and Selection. Also, there is a list of commands that can help a user solve specific tasks or problems if he has some questions. The WhatACat?Dog Bot is able to send a message to your 'Hello' or 'Thanks' response as well as to some unknown words. The size of an input image should be more than 300*300 pixels, or it will not be processed otherwise. The information about users (user name, date, and time) is automatically saved in logs.txt file.
  </div>
 




