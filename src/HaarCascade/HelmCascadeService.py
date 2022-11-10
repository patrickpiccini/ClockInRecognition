# -*- coding: utf-8 -*-
__author__ = 'Patrick Berlatto Piccini'
__title__ = 'Identificação de Capacete usando HaarCascade'
__exename__ = 'main'

import cv2

class HelmetCascade(object):

	def __init__(self) -> None:
		pass

	def cascade(self, frame: object):
		"""Aply the haar cascade technique"""

		car_cascade = cv2.CascadeClassifier(".\\data\\train\\cascade.xml")

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		objetos = car_cascade.detectMultiScale(gray, 3, 5)

		for (x, y, w, h) in objetos:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
			cv2.putText(frame, 'Hemlt', (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
			

# if __name__ == "__main__":
# 	CD = HelmetCascade()
# 	CD.cascade()
