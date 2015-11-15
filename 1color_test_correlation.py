import numpy as np
from matplotlib import pyplot as plt
import cv2

def bgr_rgb_transform(img):
    """ Transform BGR image to RGB image. Is used for displaying images in pyplot"""
    b,g,r = cv2.split(img)
    res = cv2.merge([r,g,b])
    return res


def main():
    # open video file
    # cap = cv2.VideoCapture('video/pink_floyd_high_hopes.mp4')
    cap = cv2.VideoCapture('video/Elka - Vse zavisit ot nas.mp4')

    scale_img = cv2.imread('images/HueScale.png')
    # used for save every 25 frame
    save_flag = 0
    # number of saved frames
    counter = 0
    # for analyze farness from the center
    center_coeff = 1
    histograms = []

    while(cap.isOpened()):
        ok, frame = cap.read()
        if not ok:
            print("Can't open")
            break

        save_flag += 1
        if save_flag % 25 == 0:
            counter += 1
            # transform from BGR to HSV to analyze values of Hue
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # parametres: images, channels, mask, histSize, ranges[, hist[, accumulate]]
            hist = cv2.calcHist([hsv_frame],[0],None,[180],[0,256])
            histograms.append(hist)

            cv2.imwrite('out/img_out_' + str(counter) + '.png', frame)

        if counter >= 25:
            break

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame',frame)
        if save_flag == 500:
            save_flag = 0

        # quit if Q pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print('number of histograms', len(histograms))

    # show picture with scale and historgams in one window
    plt.subplot(2,1,1)
    plt.imshow(bgr_rgb_transform(scale_img))
    plt.title('Scale of Hue')

    plt.subplot(2,1,2)
    plt.title('Histogram')
    for hist in histograms:
        plt.plot(hist)
    plt.show()

    cap.release()
    cv2.destroyAllWindows()

# entry point
if __name__ == '__main__':
    main()
