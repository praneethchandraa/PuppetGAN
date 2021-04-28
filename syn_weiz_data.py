from glob import glob
from random import shuffle

import cv2
import numpy as np
import subprocess as sp


SIZE = 64 # Size of the real images

def synthPrep(pth):
    """
        Prepares synthetic data for training

        args:
            pth: path to synthetic image
    """


    img = cv2.imread(pth)
    img = cv2.resize(img, (SIZE, SIZE*3), interpolation = cv2.INTER_AREA)
    board = 255*np.ones((SIZE*3, SIZE*3, 3), dtype=np.uint8)
    board[:, :SIZE, :] = img
    return board

def makeSynGrid(pths, out):
    """
        Prepares synthetic data for evaluation in a GRID like in the paper

        args:
            pths: paths to the synthetic images
            out: Folder to store the dataset
    
    """


    for i in range(0, 1000, 10):
        imgs = [cv2.imread(pths[k]) for k in range(i, i+10)]
        imgs = [cv2.resize(i, (SIZE, SIZE*3), interpolation = cv2.INTER_AREA) for i in imgs]
        grid = 255*np.ones((SIZE*10, SIZE*10, 3), dtype=np.uint8)

        for j in range(10):
            grid[SIZE*j:SIZE*(j+1), 0:SIZE, :] = imgs[j][SIZE:SIZE*2, 0:SIZE, :]
            
        cv2.imwrite(out+f"image_{i}.png", grid)



pths_r = glob('./data/sample/weizman_c/*png') # Glob path to real images
pths_syn = glob('./data/sample/synaction/*.png') # Glob path to synthetic images

shuffle(pths_r), shuffle(pths_syn)

out = './data/syn_weiz_6/' # Output folder to store the dataset

sp.run(['mkdir', '-p', out+'real_/real'])

for pth in pths_r[:-10]:
    file = out+'real_/real/'+pth.split('/')[-1]
    img = cv2.imread(pth)

    cv2.imwrite(file, img)

sp.run(['mkdir', '-p', out+'synth_/synth'])

for pth in pths_syn[:-1000]:
    file = out+'synth_/synth/'+pth.split('/')[-1]
    img = synthPrep(pth)
    cv2.imwrite(file, img)

sp.run(['mkdir', '-p', out+'rows_'])
sp.run(['mkdir', '-p', out+'rows_/real'])

for pth in pths_r[-10:]:
    file = out+'rows_/real/'+pth.split('/')[-1]
    img = cv2.imread(pth)
    cv2.imwrite(file, img)


sp.run(['mkdir', '-p', out+'rows_/synth'])

makeSynGrid(pths_syn[-1000:], out+'rows_/synth/')
