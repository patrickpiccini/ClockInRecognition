import numpy as np
import cv2
car_cascade = cv2.CascadeClassifier(".\\models\\train\\cascade.xml")
img = cv2.imread(".\\models\\positives\\hard_hat_workers262.png")
height, width, c = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
objetos = car_cascade.detectMultiScale(gray, 1., 5)
print(objetos)
for (x,y,w,h) in objetos:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('Analise', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


