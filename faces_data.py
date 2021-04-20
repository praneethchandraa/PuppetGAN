from glob import glob
from random import shuffle

import cv2
import numpy as np
import subprocess as sp



def makeSynGrid(pths, out):
    box = (0, 128, 128, 128)
    for i in range(0, 1000, 10):
        imgs = [cv2.imread(pths[k]) for k in range(i, i+10)]
        grid = 255*np.ones((1280, 1280, 3), dtype=np.uint8)

        for j in range(10):
            grid[128*j:128*(j+1), 0:128, :] = imgs[j][128:256, 0:128, :]
            
        cv2.imwrite(out+f"image_{i}.png", grid)




real_f = ["./data/faces_009/*.png", "./data/faces_022/*.png"]
syn_f = './data/syn-face/*.png'


real = glob(real_f[0])
real.extend(glob(real_f[1]))

syn = glob(syn_f)


shuffle(real), shuffle(syn)

out = './data/mouth/'

sp.run(['mkdir', '-p', out+'real_/real'])

for pth in real[:-20]:
    sp.run(['cp', pth, out+'real_/real/'])

sp.run(['mkdir', '-p', out+'synth_/synth'])

for pth in syn[:-1000]:
    sp.run(['cp', pth, out+'synth_/synth/'])

sp.run(['mkdir', '-p', out+'rows_'])
sp.run(['mkdir', '-p', out+'rows_/real'])

for pth in real[-20:]:
    sp.run(['cp', pth, out+'rows_/real/'])

sp.run(['mkdir', '-p', out+'rows_/synth'])

makeSynGrid(syn[-1000:], out+'rows_/synth/')
