<h1>WhatACat?Dog project</h1></br>
<div>
<h3>Introduction</h3>
Our task was to recognize a breed of a cat or a dog. We used 2 datasets for distinguishing these breeds. The first one is called The Oxford-IIIT PET dataset. There is a collection of 2371 images of cats and 12 cat breeds in general. The second dataset is the Stanford Dogs Dataset with 120 breeds. For each breed class there are ~150 images. So the content of the dataset is quite huge as the number of total images is 20,580. 
</div>

<div>
  <h3>Recognition Model</h3>
  Our Neural Network receives an input (one single vector with 64*64 values) and transforms it using a series of hidden layers. The last layer is a fully-connected layer and is called the output layer. For making a Recongnition Model we took into account Convolutional Neural Networks because of the fact it has a sensible architecture and each neuron is arranged in 3 dimensions: width, height, and depth.
We used 4 main types of layers to build a model: Convolutional, Pooling, Fully-Connected Layer, and Flattening Layers.
</br></br>
<h4>Convolutional Layer and ReLU function</h4>
This is the main layer because it is used to reduce the size of an image and make the process of breeds recognition easier and faster.
If an image is too big, some of the main features are lost because the image is compressed to the shape of (64, 64) pixels. But for preventing such loss of image information we used feature maps. As a result, each cat or dog has a unique map feature location for identifying it. 
</div>




