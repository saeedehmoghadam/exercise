import cv2 as cv
import numpy as np

img_sajjad = cv.imread('img/me.jpg', 0)
img_lion = cv.imread('img/eliot.jpg', 0)

height, width = img_sajjad.shape
eliot_img = cv.resize(img_lion, (height, width))

merge1 = img_sajjad//2 + eliot_img//4
merge2 = img_sajjad//4 + eliot_img//2

result = np.zeros((height, width*4), dtype='uint8')

result[0:height, 0:width]=img_sajjad
result[0:height, width:width*2]=merge1
result[0:height, width*2:width*3]=merge2
result[0:height, width*3:width*4]=eliot_img

cv.imwrite('result_5.jpg', result)