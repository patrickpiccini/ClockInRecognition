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
		self.frame=None
		self.small_frame=None
		self.key=None

	def openRecognitionCamera(self) -> None:
		RE = Recognizer()
		while True:
			self.frame = self.camera.read()[1]
			self.small_frame = cv.resize(self.frame, (0,0), fx=0.25, fy=0.25)

			RE.recognizeFaces(self.small_frame)
			
			self.drawFacesIdentificator(RE.captured_face_locations, RE.captured_face_names)
			
			cv.imshow("camera", self.frame)
			self.key = cv.waitKey(60)
			if self.key == 27:
				break

		cv.waitKey(0)
		cv.destroyAllWindows()

	def screenShot(self,name) -> None:
		while True:
			self.frame = self.camera.read()[1]

			cv.imshow("camera", self.frame)
			self.key = cv.waitKey(60)
			if self.key == 27:
				break
			if self.key == ord('s'):
				saved_dir = f'.\\data\\faces\\{name}.jpg'
				cv.imwrite(saved_dir, self.frame)
				return saved_dir
				break


	def drawFacesIdentificator(self,face_locations: dict, face_names: dict) -> None:
		for (top, right, bottom, left), name in zip(face_locations, face_names):
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
