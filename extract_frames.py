import cv2
import scipy.io as io
import numpy as np

from glob import glob


mask_m = io.loadmat('./data/wezman/classification_masks.mat')['original_masks']
paths = glob('./data/wezman/videos/*.avi')
save_path = './data/syn-weiz/weizman/'

masks = list(mask_m[0][0])
names = mask_m.dtype.names
mask_map = dict(zip(names, masks))


def getCropped(frame, mask):
    x, y = np.nonzero(mask)
    x, y = np.mean(x).astype(int), np.mean(y).astype(int)

    x = 64 if x<64 else x
    x = 80 if x>80 else x

    y = 64 if y<64 else y
    y = 116 if y>116 else y

    return frame[x-64:x+64, y-64:y+64, :]
    

def extractAndCrop(pth, skip=4):
    file_name = video.split('/')[-1][:-4]

    vidcap = cv2.VideoCapture(pth)
    count = -1
    success = 1


    while success:
        success, frame = vidcap.read()
        count += 1

        if count%skip==0 and success==1:
            try:
                cropped = getCropped(frame, mask_map[file_name][:, :, count])
                cv2.imwrite(f'{save_path}{file_name}_{count}.png', cropped)
            except:
                print("failed")

for video in paths:
    extractAndCrop(video)

