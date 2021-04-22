import subprocess as sp
from glob import glob


paths = glob('./data/wezman/videos/*.avi')
save_path = './data/syn-weiz/weizman/'

for video in paths:
    file_name = video.split('/')[-1][:-4]
    sp.run(['ffmpeg', '-i', video, f'{save_path}{file_name}_%04d.png'])
