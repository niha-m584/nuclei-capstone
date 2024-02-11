# importing the module 
import cv2 
from collections import defaultdict
import os, glob
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import skimage
import subprocess as sp

img_path = img = buttons = clone = None

def reset_img():
    global clone, img_boxes, img_path
    clone = img.copy()
    for pair in img_boxes[img_path]:
        cv2.rectangle(clone, pair[0],
                        pair[1],
                        (255, 0, 0),
                        thickness = 1,
                        )
    cv2.imshow('image', clone)

## FROM https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
    global buttons
    global clone

    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN and len(buttons) < 2:
  
        # displaying the coordinates 
        # on the Shell

        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        buttons.append((x, y))
        reset_img()
        if len(buttons) == 1:
            cv2.putText(clone, str(x) + ',' +
                        str(y), (x,y), font, 
                        1, (255, 0, 0), 2)
        else:   
            cv2.rectangle(clone, buttons[0],
                        buttons[1],
                        (255, 0, 0),
                        thickness = 1,
                        )
    elif event == cv2.EVENT_RBUTTONDOWN or (event == cv2.EVENT_LBUTTONDOWN and len(buttons) >= 2):
        buttons = []
        reset_img() 


img_boxes = defaultdict(list)
## Reference from https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picturehttps://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture
img_root = "/Users/William/desktop/cell-images/*.tif"
for i, img_path in enumerate(glob.glob(img_root), start=1):
    print(os.path.basename(img_path))
    img = cv2.imread(img_path, 1)
    buttons = []
    clone = img.copy()

    while(1):
        cv2.imshow('image', clone) 
        cv2.setMouseCallback('image', click_event) 
        k = cv2.waitKey(1) & 0xFF
        if k == ord("s"):
            if len(buttons) == 2:
                img_boxes[img_path].append(buttons)
            break
        elif k == ord("n"):
            if len(buttons) == 2:
                img_boxes[img_path].append(buttons)
            buttons = []
        elif k == 27:
            img_boxes[img_path] = []
            buttons = []
            reset_img()
    cv2.destroyAllWindows()


outfile_name = f"/Users/William/desktop/output/{str(datetime.datetime.now()).replace(' ', '_')}.txt"
with open(outfile_name, 'w') as outfile:
    outfile.write(str(dict(img_boxes)))
sp.run(f'open {outfile_name}', shell=True)
