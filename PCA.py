import numpy as np
from os import listdir
import cv2

def imread_txt(path):
    f = open(path)
    img = []
    for line in f:
        img.append([(0 if int(item)==0 else 255) for item in line.strip()])
    return np.array(img,dtype=np.uint8)

def read_img(path):
    data = open(path).read().replace("\n","")
    return np.array([int(item) for item in data])

def PCA():
    path = "D:/digits/testDigits"
    ims = []
    for pim in listdir(path):
        ims.append(read_img(path+'/'+pim))
    ims = np.array(ims)
    cov = np.dot(ims,ims.T)
    div = []
    for i in range(len(cov)):
        div.append(cov[i]/946)
    
    print(len(np.linalg.eig(div)[1]))

cv2.imshow('',imread_txt("D:/digits/testDigits/0_0.txt"))
cv2.waitKey(0)
PCA()
