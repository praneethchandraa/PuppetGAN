import cv2
import scipy.io as io
import numpy as np

from glob import glob


mask_m = io.loadmat('./data/wezman/classification_masks.mat')['original_masks'] # Path to the masks for the weizmann dataset
paths = glob('./data/wezman/videos/*.avi') # Glob path to the Weizmann videos
save_path = './data/sample/weizman_c/' # Location to extract the frames

CROP = 86 # Size of the CROP around the mask
SIZE = 64 # Final size of the image

hcrop = CROP//2

masks = list(mask_m[0][0])
names = mask_m.dtype.names
mask_map = dict(zip(names, masks))


def getCropped(frame, mask):

    '''
        Takes a frame and the associated mask to crop out region around the mask

        args:
            frame : numpy array of the BGR image
            mask : numpy array of the mask 


    '''


    x, y = np.nonzero(mask)
    x, y = np.mean(x).astype(int), np.mean(y).astype(int)

    x = hcrop if x<hcrop else x
    x = 144-hcrop if x>144-hcrop else x

    y = hcrop if y<hcrop else y
    y = 180-hcrop if y>180-hcrop else y

    return frame[x-hcrop:x+hcrop, y-hcrop:y+hcrop, :]
    

def extractAndCrop(pth, skip=4):
    """
        Samples a video for frames, crops them and saves them

        args:
            pth: Path to the video
            skip: Number of frames to sample a single frame from

    """

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
                cropped = cv2.resize(cropped, (SIZE, SIZE), interpolation=cv2.INTER_AREA)
                cv2.imwrite(f'{save_path}{file_name}_{count}.png', cropped)
            except:
                print("failed")

for video in paths:
    extractAndCrop(video)

