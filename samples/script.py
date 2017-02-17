''' Script to convert the screenshot to sudoku input '''


import os
import cv2

count = 0

for file in os.listdir("."):
    if file.endswith(".png"):
        img = cv2.imread(file)
        small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        cropimg = small[107:467, 0:360]
       	cv2.imwrite("image" + str(count) + ".jpg",cropimg)
       	count = count + 1
