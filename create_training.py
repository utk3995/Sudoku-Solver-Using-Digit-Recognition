from PIL import Image
import cv2
import glob
import sys
import numpy as np


f1 = open('trainingdata.txt','w')
f2 = open('traininglable.txt','w')

for foldername in range(1,10):
	for img in glob.glob("data/training/"+str(foldername)+"/*.jpg"):
		#print "hello "
		f2.write(str(foldername))
		f2.write('\n')
		im = cv2.imread(img,0)
		#im = imm[38:88, 38:88] 
		#(thresh, im) = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		im = cv2.resize(im, (28, 28))
		im_new = np.zeros((28,28))
		for i in range(0,28):
			for j in range(0,28):
				if(im[i][j]>50):
					im_new[i][j] = 0;
					f1.write("0 ")
				else:
					im_new[i][j] = 1
					f1.write("1 ")
		f1.write("\n")
