# coding: 'utf-8'

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg', 1)
cv2.imshow('image',img)
plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('lena_out.png',img)
    cv2.destroyAllWindows()
