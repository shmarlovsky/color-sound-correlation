
#!/usr/bin/env python

import numpy as np
import cv2

# built-in modules
import sys
from time import clock

# local modules
import video

if __name__ == '__main__':

    hsv_map = np.zeros((180, 256, 3), np.uint8)
    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv_map', hsv_map)

    cv2.namedWindow('hist', 0)
    hist_scale = 10
    def set_scale(val):
        global hist_scale
        hist_scale = val
    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

    # try:
    #     fn = sys.argv[1]
    # except:
    #     fn = 0
    # cam = video.create_capture(fn, fallback='synth:bg=../data/baboon.jpg:class=chess:noise=0.05')
    # cam = cv2.VideoCapture('video/Elka - Vse zavisit ot nas.mp4')
    cam = cv2.VideoCapture('video/pink_floyd_high_hopes.mp4')
    while True:
        flag, frame = cam.read()
        cv2.imshow('camera', frame)

        small = cv2.pyrDown(frame)

        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
        dark = hsv[...,2] < 32
        hsv[dark] = 0
        h = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )


        h = np.clip(h*0.005*hist_scale, 0, 1)
        vis = hsv_map*h[:,:,np.newaxis] / 255.0
        cv2.imshow('hist', vis)

        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break
    cv2.destroyAllWindows()



#############################
#############################

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('images/test_img.png')
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# print(hist.shape)
# while(1):
#     cv2.imshow('hist',hist)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()
