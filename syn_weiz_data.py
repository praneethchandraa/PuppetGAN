from glob import glob
from random import shuffle

import cv2
import numpy as np
import subprocess as sp


def realPrep(pth):
    img = cv2.imread(pth)
    board = 255*np.ones((256, 256, 3), dtype=np.uint8)
    board[56:200, 38:218, :] = img
    
    return board 

def synthPrep(pth):
    img = cv2.imread(pth)
    board = 255*np.ones((768, 768, 3), dtype=np.uint8)
    board[:768, :256, :] = img
    return board

def makeSynGrid(pths, out):
    for i in range(0, 1000, 10):
        imgs = [cv2.imread(pths[k]) for k in range(i, i+10)]
        grid = 255*np.ones((2560, 2560, 3), dtype=np.uint8)

        for j in range(10):
            grid[256*j:256*(j+1), 0:256, :] = imgs[j][256:512, 0:256, :]
            
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
