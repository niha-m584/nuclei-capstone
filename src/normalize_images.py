import os
import skimage
import configparser
import numpy as np

config = configparser.ConfigParser()
config.read('config.ini')

img_path = config.get('Normalize', 'folder_path')
imgs = os.listdir(img_path)
imgs.remove('.DS_Store')

for img_name in imgs:
    img = skimage.io.imread(img_path + img_name).astype(np.float32)
    for channel in range(3):
        img[...,channel] = img[...,channel]/np.percentile(img[...,channel], 99.5)
    
    img = np.clip(img, 0, 1)
    # img = img[...,::-1].copy() # switch b and r channels
    img = (255 * img).astype(np.uint8)
    skimage.io.imsave(f'{img_path}/norm/{img_name}', img)
