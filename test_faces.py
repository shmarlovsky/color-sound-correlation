# coding: 'utf-8'

import sys, cv2 as cv
cap = cv.VideoCapture(0)
cascade = cv.CascadeClassifier(
 "lbpcascade_frontalface.xml")
  # Загрузка обученного каскадного классификатора
while True:
 ok, img = cap.read()
 if not ok:
  break
 gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 sf = min(640./img.shape[1], 480./img.shape[0])
 gray = cv.resize(gray, (0,0), None, sf, sf)
  # Масштабирование
 rects = cascade.detectMultiScale(gray, scaleFactor=1.3,
                minNeighbors=4, minSize=(40, 40),
                flags=cv.CV_HAAR_SCALE_IMAGE) % Детектирование
 gray = cv.GaussianBlur(gray, (3, 3), 1.1)
  # Размываем
 edges = cv.Canny(gray, 5, 50) # Детектируем ребра

 out = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
 for x, y, w, h in rects:
  cv.rectangle(out, (x, y), (x+w, y+h), (0,0,255), 2)
   # Вокруг найденного лица
   # рисуем красный прямоугольник
 cv.imshow("edges+face", out)
 if cv.waitKey(30) > 0:
  break
