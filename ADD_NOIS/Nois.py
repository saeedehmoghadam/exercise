import random
import cv2
import numpy as np

image = cv2.imread("hw2\chess pieces.jpg" ,0)
row , col = image.shape

for i in range(1000):
    nois = random.randint(0,255)
    random_x = random.randint(0,row-1)
    random_y = random.randint(0,col-1)
    image[random_x,random_y] = nois

cv2.imwrite('Chess pieces.jpg',image)
cv2.imshow('Chess pieces',image)
cv2.waitKey()