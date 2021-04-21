from glob import glob
from random import shuffle

import cv2
import numpy as np
import subprocess as sp


def realPrep(pth):
    img = cv2.imread(pth)
    board = np.zeros((180, 180, 3), dtype=np.uint8)
    board[18:162, :, :] = img

    board = cv2.resize(board, (128, 128), interpolation = cv2.INTER_AREA)
    
    return board 

def synthPrep(pth):
    img = cv2.imread(pth)
    img = cv2.resize(img, (128, 384), interpolation = cv2.INTER_AREA)
    board = 255*np.ones((384, 384, 3), dtype=np.uint8)
    board[:, :128, :] = img
    return board

def makeSynGrid(pths, out):
    for i in range(0, 1000, 10):
        imgs = [cv2.imread(pths[k]) for k in range(i, i+10)]
        imgs = [cv2.resize(i, (128, 384), interpolation = cv2.INTER_AREA) for i in imgs]
        grid = 255*np.ones((1280, 1280, 3), dtype=np.uint8)

        for j in range(10):
            grid[128*j:128*(j+1), 0:128, :] = imgs[j][128:256, 0:128, :]
            
        cv2.imwrite(out+f"image_{i}.png", grid)

pths_r = glob('./data/syn-weiz/weizman/*png')
pths_syn = glob('./data/syn-weiz/synaction/*.png')

shuffle(pths_r), shuffle(pths_syn)

out = './data/syn_weiz/'

sp.run(['mkdir', '-p', out+'real_/real'])

for pth in pths_r[:-93]:
    file = out+'real_/real/'+pth.split('/')[-1]
    img = realPrep(pth)
    cv2.imwrite(file, img)

sp.run(['mkdir', '-p', out+'synth_/synth'])

for pth in pths_syn[:-1000]:
    file = out+'synth_/synth/'+pth.split('/')[-1]
    img = synthPrep(pth)
    cv2.imwrite(file, img)

sp.run(['mkdir', '-p', out+'rows_'])
sp.run(['mkdir', '-p', out+'rows_/real'])

for pth in pths_r[-93:]:
    file = out+'rows_/real/'+pth.split('/')[-1]
    img = realPrep(pth)
    cv2.imwrite(file, img)


sp.run(['mkdir', '-p', out+'rows_/synth'])

makeSynGrid(pths_syn[-1000:], out+'rows_/synth/')
