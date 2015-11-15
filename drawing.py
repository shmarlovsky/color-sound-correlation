import numpy as np
import cv2

# Create a black image
img = np.zeros((600,800,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img,(0,0),(400,600),(0,255,0),-1)
img = cv2.rectangle(img, (100, 100), (200, 500), (255,0,0), -1)
img = cv2.rectangle(img, (400, 500), (600, 800), (0,0,255), -1)
cv2.imwrite('out_img.jpg', img)
while True:

    cv2.imshow('img', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
