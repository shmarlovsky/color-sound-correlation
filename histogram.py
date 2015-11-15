
import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('wrong args')
    sys.exit(1)

input_filename = args[0]

def bgr_rgb_transform(img):
    """ Transform BGR image to RGB image. Use for displaying images in pyplot"""
    b,g,r = cv2.split(img)
    res = cv2.merge([r,g,b])
    return res


img = cv2.imread(input_filename)

# for analyze farness from the center
center_coeff = 1

# transform from BGR to HSV to analyze values of Hue
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# parametres: images, channels, mask, histSize, ranges[, hist[, accumulate]]
hist = cv2.calcHist([hsv_img],[0],None,[180],[0,256])

# show original image
plt.subplot(2,1,1)
plt.imshow(bgr_rgb_transform(img))
plt.title('img')

plt.subplot(2,1,2)

#  show histogram
plt.plot(hist)
plt.xlim(-3, 183)
plt.title('hist')
plt.show()

# color = ('b','g','r')
# for i,col in enumerate(color):
#     hist = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist,color = col)
#     plt.xlim([0,256])







