import random
import os
import sys
import numpy as np
import cv2

f1 = open('input.txt','w')

img = cv2.imread('image.png',0) 		#load in grascale
img = cv2.GaussianBlur(img, (5, 5), 0)
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 	# resizing the image
cropimg = small[107:467, 0:360] 		# will output a sudoku of size 360 * 360
crop2 = cv2.resize(cropimg, (252, 252)) 
(thresh, finalimg) = cv2.threshold(crop2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #convert it in binary image
height, width = finalimg.shape[:2]

for i in range(0,height):
	for j in range(0,width):
		finalimg[i,j] = 255 - finalimg.item(i,j)
		
for row_number in range(0,9):
	for col_number in range(0,9):
		cellimg = np.zeros((28,28)) 	#to store the 28 * 28 image for debugging purpose
		#running the loop to take in the pixel values for each cells. 2 pixels padding is done to ignore the cell borders.
		for i in range(2,26):
			for j in range(2,26):
				pixel_value = finalimg.item(row_number*28+i,col_number*28+j)
				if (pixel_value == 255):
					pixel_value = 1
				cellimg[i,j] = pixel_value

		for i in range(0,28):
			for j in range(0,28):
				f1.write(str(int(cellimg.item(i,j)))+" ");
		f1.write('\n')
		#cv2.imshow('image',cellimg)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		#break
	#break

