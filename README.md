# Better Cross-Domain Feature Disentanglement and Manipulation with Improved PuppetGAN

<p align="center">
  <img src="https://github.com/praneethchandraa/PuppetGAN/blob/585/6.gif" width="100%">
  <em>Quite cool... Right?</em>
</p>

CS 585 Final Project: PuppetGAN

## Introduction:
**PuppetGAN is** model that extends the CycleGAN idea and is **capable of extracting and manipulating features from a domain using examples from a different domain**. On top of that, one amazing aspect of PuppetGAN is that it **does not require a great amount of data**; (Giorgos Karantonis)
In addition to the MNIST dataset that the original repository used, we implemented the PuppetGAN algorithm on the SynAction and Weizamann datasets.

## Data Preparation
Training data:
- 1200 real images obtained by sampling every fourth frame in the Weizmann dataset videos
- 1200 synthetic pose images from the SynAction dataset
Validation data:
- 1000 synthetic images randomly sampled from the SynAction dataset
- 10 real images sampled from the Weizman dataset frames

In order to prepare your data for these experiments, download the SynAction and Weizmann datasets and store them in a folder. The data preparation script is syn_weiz_data.py. In this file edit the lines 49,50 to the correct paths to the folder where your data is located. You may proceed to run the script to prepare your dataset. 


## Experiments and Results
We run a couple of experiments to get the PuppetGAN algorithm to correctly manipulate the poses from the SynAction images to the Weizmann images.

### Experiment 0:
In this experiment we trained the model on resized images (64x64) from the Weizmann real images without any masking. 
In most of the generated images the pose is doesn’t look like it's related to the one in the corresponding synthetic image.
![6](https://user-images.githubusercontent.com/50864401/116167227-6c428900-a6c5-11eb-93eb-2ecabe2750b6.gif)

### Experiment 1: 
We used a mask on the real images to get the person, we then and made a 128x128 image crop to create a region of interest around the person.The pose is a match to the synthetic image in some of the generated images where the camera perspective in both the input images is similar.
![6](https://user-images.githubusercontent.com/50864401/116167301-8da37500-a6c5-11eb-934f-6698e0404b6c.gif)


### Experiment 2: 
 We increased the bottleneck dimension size of the generator to 256  to see the effects it has on the generated pose. It was an improvement over having the dimension size as 128.
 ![6](https://user-images.githubusercontent.com/50864401/116167418-c7747b80-a6c5-11eb-93f7-1b71a96febde.gif)

 
### Experiment 3: 
We increased the bottleneck dimension size of the generator to 512  to see the effects it has on the generated pose. The apparent generated pose has significantly improved although the generated images are blurry. 
![6](https://user-images.githubusercontent.com/50864401/116167490-f0950c00-a6c5-11eb-8701-3ca631c64e34.gif)


### Experiment 4: 
We found no activation function is being used by default in the repository. We added sigmoid activation to the discriminator. The bottleneck dimension being used is 512. The generated poses are better than the ones generated when there is no activation function.

![6](https://user-images.githubusercontent.com/50864401/116167615-30f48a00-a6c6-11eb-826b-328beea8330f.gif)

### Experiment 5:
We tightened the crop around the people in the weizman dataset to (86, 86) and resized the resulting image to (64, 64). The poses in the generated images are far richer in information than the previous versions.

![6 (1)](https://user-images.githubusercontent.com/50864401/116341712-02021500-a7a7-11eb-9db2-a1aa5d9fb4c3.gif)



### Training a Model 
To start a new training, simply run:

```bash
python3 main.py
```

This will automatically look first for any existing checkpoints and will restore the latest one. If you want to continue the training from a specific checkpoint just run:

```bash
python3 main.py -c [checkpoint number]
```
or
```bash
python3 main.py --ckpt=[checkpoint number]
```

To help you keep better track of your work, every time you start a new training, a configuration report is created in [`./PuppetGAN/results/config.txt`](https://github.com/GiorgosKarantonis/PuppetGAN/blob/master/PuppetGAN/results/config.txt) which stores a detailed report of your current configuration. This report contains all your hyper-parameters and their respective values as well as the whole architecture of the model you are using, including every single layer, its parameters and how it is connected to the rest of the model.

Also, to help you keep better track of your process, every a certain number of epochs my model creates in `./PuppetGAN/results` a sample of [evaluation rows of generated images](https://github.com/GiorgosKarantonis/images/blob/master/PuppetGAN/mouth_baseline.png) along with [`gif` animations for these rows](https://github.com/GiorgosKarantonis/images/blob/master/PuppetGAN/mouth_baseline.gif) to visualize better the performance of your model. 

On top of that, in `./PuppetGAN/results` are also stored plots of both the supervised and the adversarial losses as well as the images that are produced during the training. This allows you to have in a single folder everything you need to evaluate an experiment, keep track of its progress and reproduce its results!

Unless you want to experiment with different architectures, [`PuppetGAN/config.json`](https://github.com/GiorgosKarantonis/PuppetGAN/blob/master/PuppetGAN/config.json) is the only file you'll need. This file allows you to control all the hyper-parameters of the model without having to look at any of code! More specifically, the parameters you can control are: 

* `dataset` : The dataset to use. You can choose between *"mnist"*, *"mouth"* and *"light"*.

* `epochs` : The number of epochs that the model will be trained for.

* `noise std` : The standard deviation of the noise that will be applied to the translated images. The mean of the noise is 0.

* `bottleneck noise` : The standard deviation of the noise that will be applied to the bottleneck. The mean of the noise is 0.

* `on roids` : Whether or not to use the proposed Roids.

* `learning rates`-`real generator` : The learning rate of the real generator.

* `learning rates`-`real discriminator` : The learning rate of the real discriminator

* `learning rates`-`synthetic generator` : The learning rate of the synthetic generator.

* `learning rate`-`synthetic discriminator` : The learning rate of the synthetic discriminator.

* `losses weights`-`reconstruction` : The weight of the reconstruction loss.

* `losses weights`-`disentanglement` : The weight of the disentanglement loss.

* `losses weights`-`cycle` : The weight of the cycle loss.

* `losses weights`-`attribute cycle b3` : The weight of part of the attribute cycle loss that is a function of the synthetic image that has both the Attribute of Interest and all the rest of the attributes.

* `losses weights`-`attribute cycle a` : The weight of part of the attribute cycle loss that is a function of the real image.

* `batch size` : The batch size. Depending on the kind of the dataset different values can be given.

* `image size` : At what size to resize the images of the dataset.

* `save images every` : Every how many epochs to save the training images and the sample of the evaluation images.

* `save model every` : Every how many epochs to create a checkpoint. Keep in mind that the 5 latest checkpoints are always kept during training.

### Evaluation of a Model
You can start an evaluation just by running:

```bash
python3 main.py -t
```
or
```bash
python3 main.py --test
```

Just like with training, this will look for the latest checkpoint; if you want to evaluate the performance of a different checkpoint you can simply use the `-c` and `--ckpt` options the same way as before.

During the evaluation process, the model creates all the [rows of the generated images](https://github.com/GiorgosKarantonis/images/blob/master/PuppetGAN/mouth_baseline.png), where each cell corresponds to the generated image for the respective synthetic and a real input. Additionally, for each of the evaluation images, [their corresponding `gif` file](https://github.com/GiorgosKarantonis/images/blob/master/PuppetGAN/mouth_baseline.gif) is also created to help you get a better idea of your results!

If you want to calculate the scores of your model in the `MNIST` dataset you can use my [`./PuppetGAN/eval_rotation.py`](https://github.com/GiorgosKarantonis/PuppetGAN/blob/master/PuppetGAN/eval_rotation.py) script, by running:

```bash
python3 eval_rotation.py -p [path to the directory of your evaluation images]
```
or
```bash
python3 eval_rotation.py -path=[path to the directory of your evaluation images]
```

You can also specify a path to save the evaluation report file using the option `-t` or `--target-path`. For example, let's say you have just trained and produced the evaluation images for a model and you want to get the evaluation scores for epoch 100 and save the report in the folder of this epoch. Then you should just run:

```bash
# make sure you are in ./PuppetGAN
python3 eval_rotation.py -p results/test/100/images -t results/test/100
```


