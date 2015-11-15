# coding: 'utf-8'

import numpy as np
import cv2
import time

cap = cv2.VideoCapture('/home/kirill/downloads/odnoklassniki-2010.flv')

save_flag = 0
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    save_flag += 1

    # if save_flag % 25 == 0:
    #     count += 1
    #     cv2.imwrite('lena_out_' + str(count) + '.png', frame)

    # if count >= 25:
    #     break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
