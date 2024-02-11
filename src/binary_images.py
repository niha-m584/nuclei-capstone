import os
import cv2
import skimage
import numpy as np

def convert_imgs(img, color):
    image = cv2.imread(img)
    if image is None:
        return None
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    target_color = np.array([int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)])
    mask = cv2.inRange(img_rgb, target_color, target_color)

    inverted_mask = cv2.bitwise_not(mask)
    white_image = np.ones_like(image) * 255

    result = cv2.bitwise_and(image, image, mask=inverted_mask)
    result = cv2.add(result, white_image, mask=mask)

    return result

img_path = '/Users/William/desktop/cropped-images/'
imgs = os.listdir(img_path)

for img in imgs:
    result = convert_imgs(img_path + img, '#f0027f')
    if result is not None:
        skimage.io.imsave(f'/Users/William/Desktop/binary-cropped-images/{img}_binary.png', result)