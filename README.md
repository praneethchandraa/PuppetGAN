CS 585 Final Project: PuppetGAN

## Introduction:
**PuppetGAN is** model that extends the CycleGAN idea and is **capable of extracting and manipulating features from a domain using examples from a different domain**. On top of that, one amazing aspect of PuppetGAN is that it **does not require a great amount of data**; (Giorgos Karantonis)
In addition to the MNIST dataset that the original repository used, we implemented the PuppetGAN algorithm on the SynAction and Weizamann datasets.

## Data Preparation
Training data:
- 1200 real images obtained by sampling every fourth frame in the Weizman dataset videos
- 1200 synthetic pose images from the SynAction dataset
Validation data:
- 100 images sampled from the SynAction dataset
- *20* images sampled from the Weizman video frames

## Experiments
We run a couple of experiments to get the PuppetGAN algorithm to correctly manipulate the poses from the SynAction images to the Weizmann images.

### Experiment 0:
In this experiment we trained the model on resized images (64x64) from the Weizmann real images without any masking

### Experiment 1: 
We used a mask on the real images to get the person, we then and made a 128x128 image crop to allow the 'person' to take up more of the frame.

### Experiment 2: 
 We also explored using a much larger dimension in the bottleneck layer and scaling the images to 256x256
 
### Experiment 3: 
Introduced a sigmoid activation for the activation function in the discriminator. 

### Experiment 4: 
Exp 4 still needs a better explanation

### Experiment 5: 
In this experiment we reduced the learning rate because we were implementing the training with a smaller batch size of 16 

### Experiment 6: 
Ongoing. We are using a mask over the real images to center the 'person'. We are then cropping around the mask to magnify the  person in the frame. We are resizing the cropped image to *dim*
