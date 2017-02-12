import pandas as pd
from random import randint
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os

with open("trainingdata.txt") as textFile:
    features = [line.split() for line in textFile]
with open("traininglable.txt") as textFile:
    tagg = [line.split() for line in textFile]
tagi=np.array(tagg)
tag=np.ravel(tagi)
with open("input.txt") as textFile:
    test = [line.split() for line in textFile]
#with open("ansfile.txt") as textFile:
#    ans = [line.split() for line in textFile]
clf = KNeighborsClassifier(n_neighbors=2,weights='distance')
clf.fit(features, tag)
preds = clf.predict(test)
#b=[i for i, j in zip(preds, ans) if i == j]
#print b
#print len(b)
print preds
outfile = open('output.txt', 'w')
k = 0
for i in range(0,9):
	for j in range(0,9):
		outfile.write(str(preds[k])+" ")
		k = k+1
	outfile.write('\n')
#for i in preds:
#  outfile.write(str(i))
#  outfile.write('\n')
outfile.close()
