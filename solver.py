import pandas as pd
from random import randint
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os
import random
import sys
import cv2

f1 = open('testingdata.txt','w')
outfile = open('sudoku_input.txt', 'w')

filename = sys.argv[-1]

img = cv2.imread(filename,0) 		#load in grascale
img = cv2.GaussianBlur(img, (5, 5), 0)
crop = cv2.resize(img, (252, 252)) 
(thresh, finalimg) = cv2.threshold(crop, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #convert it in binary image
height, width = finalimg.shape[:2]

for i in range(0,height):
	for j in range(0,width):
		finalimg[i,j] = 255 - finalimg.item(i,j)
		
valid = np.zeros((28,28))
		
for row_number in range(0,9):
	for col_number in range(0,9):
		cellimg = np.zeros((28,28)) 	#to store the 28 * 28 image for debugging purpose
		#running the loop to take in the pixel values for each cells. 2 pixels padding is done to ignore the cell borders.
		count_pixel=0
		for i in range(2,26):
			for j in range(2,26):
				pixel_value = finalimg.item(row_number*28+i,col_number*28+j)
				if (pixel_value == 255):
					pixel_value = 1
					count_pixel = count_pixel+1
				cellimg[i,j] = pixel_value
		if (count_pixel != 0):
			valid[row_number,col_number]=1
		for i in range(0,28):
			for j in range(0,28):
				f1.write(str(int(cellimg.item(i,j)))+" ");
		f1.write('\n')
f1.close()
		
		
with open("trainingdata.txt") as textFile:
    features = [line.split() for line in textFile]
with open("traininglable.txt") as textFile:
    tagg = [line.split() for line in textFile]
tagi=np.array(tagg)
tag=np.ravel(tagi)
with open("testingdata.txt") as textFile:
    test = [line.split() for line in textFile]
clf = KNeighborsClassifier(n_neighbors=2,weights='distance')
clf.fit(features, tag)
preds = clf.predict(test)
k = 0
for i in range(0,9):
	for j in range(0,9):
		if (valid[i][j] == 1):
			outfile.write(str(preds[k])+" ")
		else:
			outfile.write("0 ")
		k = k+1
	outfile.write('\n')
outfile.close()

os.system("./sudoku_solver")
os.system("rm testingdata.txt")
os.system("rm sudoku_input.txt")		

