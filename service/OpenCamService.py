# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Abertura de camera Geral'
__exename__ = 'main'

import cv2 as cv
import numpy as np


from .RecognizerService import Recognizer

# Open notebook camera    
class OpenCamera():

	def __init__(self) -> None:
		self.camera = cv.VideoCapture(0, cv.CAP_DSHOW)
		self.RE = Recognizer()
		self.frame = None

	def openCamera(self) -> None:
		while True:
			self.frame = self.camera.read()[1]
			small_frame = cv.resize(self.frame, (0,0), fx=0.25, fy=0.25)

			self.RE.recognizeFaces(small_frame)
			self.drawFacesIdentificator(self.RE.captured_face_locations, self.RE.captured_face_names)
			
			cv.imshow("camera", self.frame)
			key = cv.waitKey(60)
			if key == 27:
				break

		cv.waitKey(0)
		cv.destroyAllWindows()

	def drawFacesIdentificator(self,face_locations,face_names) -> None:
		print("faces camera",face_locations)
		print("names camera",face_names)
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			print('name',name)
			top = int(top*4)
			right = int(right*4)
			bottom = int(bottom * 4)
			left = int(left * 4)

			# Draw a rectangle around the face
			cv.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)

			# Input text label with a name below the face
			cv.rectangle(self.frame, (left, bottom - 35),
						(right, bottom), (0, 0, 255), cv.FILLED)

			font = cv.FONT_HERSHEY_DUPLEX
			cv.putText(self.frame, name, (left + 6, bottom - 6),
						font, 0.5, (255, 255, 255), 1)
