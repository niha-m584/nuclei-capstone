import os
import skimage
import numpy as np

img_path = '/Users/William/desktop/nuclei-test/assets/cell-images/'
imgs = os.listdir(img_path)
imgs.remove('.DS_Store')

for img_name in imgs:
    img = skimage.io.imread(img_path + img_name).astype(np.float32)
    for channel in range(3):
        img[...,channel] = img[...,channel]/np.percentile(img[...,channel], 99.5)
    
    img = np.clip(img, 0, 1)
    # img = img[...,::-1].copy() # switch b and r channels
    img = (255 * img).astype(np.uint8)
    skimage.io.imsave(f'/Users/William/desktop/nuclei-test/assets/new-cell-images/{img_name}', img)
