import cv2
import skimage
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

img_path = config.get('Boxes', 'folder_path')
coords = config.get('Boxes', 'coords_path')

with open(coords) as f:
    for line in f:
        dictionary = eval(line)
        for k, v in dictionary.items():
            img_name = k.split('/')[-1].replace('.tif', '')
            img = skimage.io.imread(img_path + img_name + '.png')
            for i in range(len(v)):
                box = v[i]
                xs = sorted([box[0][0], box[1][0]])
                ys = sorted([box[0][1], box[1][1]])
                start_x = xs[0]
                end_x = xs[1]
                start_y = ys[0]
                end_y = ys[1]
                cropped_img = img[start_y:end_y, start_x:end_x]
                skimage.io.imsave(f'{img_path}/cropped-images/{img_name}_{i}.png', cropped_img)