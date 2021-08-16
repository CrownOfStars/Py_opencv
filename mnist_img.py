import cv2
import numpy as np

"""
convert mnist .txt to img 
"""

def imread_txt(path):
    f = open(path)
    img = []
    for line in f:
        img.append([(0 if int(item)==0 else 255) for item in line.strip()])
    return np.array(img,dtype=np.uint8)

cv2.imshow('',imread_txt("D:/digits/testDigits/0_0.txt"))
cv2.waitKey(0)
