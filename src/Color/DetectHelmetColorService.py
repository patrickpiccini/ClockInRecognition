import cv2 as cv
import numpy as np

from utils.Utils import userRandonId, getDateTime


class DetectHelmetColor():

	def __init__(self) -> None:
		self.LOWER_BLUE = np.array([94,121,40])
		self.UPPER_BLUE = np.array([137,250,255])

		self.LOWER_RED = np.array([0,161,75])
		self.UPPER_RED = np.array([16,255,220])
		
		self.LOWER_GREEN = np.array([40,101,23])
		self.UPPER_GREEN = np.array([59,250,158])
		
		self.LOWER_YELLOW = np.array([14, 60, 169])
		self.UPPER_YELLOW = np.array([35,255,255])   

	def helmetColor(self, frame: object) -> None:
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

		# CREATE MASK OF COLORS
		maskRed     = cv.inRange(hsv, self.LOWER_RED, self.UPPER_RED)
		maskGreed   = cv.inRange(hsv, self.LOWER_GREEN, self.UPPER_GREEN)
		maskYellow  = cv.inRange(hsv, self.LOWER_YELLOW, self.UPPER_YELLOW)

		# CRIATE OF BITWISE
		bitRed      = cv.bitwise_and(frame, frame, mask=maskRed)
		bitGreen    = cv.bitwise_and(frame, frame, mask=maskGreed)
		bitYellow   = cv.bitwise_and(frame, frame, mask=maskYellow)

		# GRAY OF ALL COLORS
		grayRed 	= cv.cvtColor(bitRed, cv.COLOR_BGR2GRAY)
		grayGreen 	= cv.cvtColor(bitGreen, cv.COLOR_BGR2GRAY)
		grayYellow	= cv.cvtColor(bitYellow, cv.COLOR_BGR2GRAY)


		# COR VERMELHA
		#-----------------------------------------------------   
		_, borda = cv.threshold(grayRed, 3, 255, cv.THRESH_BINARY)
		contornosRed, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

		for contorno in contornosRed:
			area = cv.contourArea(contorno)
			if area > 1200 :
				(x, y, w, h) = cv.boundingRect(contorno)
				cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
				cv.putText(
					frame,
					str(f"x: {x} y: {y}"),
					(x, y-20),
					cv.FONT_HERSHEY_SIMPLEX,
					1, 1
				)

				# Escreve no arquivo access.txt
				with open(".\\security\\access.txt", 'a') as arquivo:
					photo_id = userRandonId()
					arquivo.write(f'{getDateTime()} - USUÁRIO NÃO AUTORIZADO! Cod:{photo_id}\n')
					return photo_id

 
		# COR VERDE
		#-----------------------------------------------------   
		_, borda = cv.threshold(grayGreen, 3, 255, cv.THRESH_BINARY)
		contornosGreen, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

		for contorno in contornosGreen:
			area = cv.contourArea(contorno)
			if area > 1200:
				(x, y, w, h) = cv.boundingRect(contorno)
				cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
				cv.putText(
					frame,
					str(f"x: {x} y: {y}"),
					(x, y-20),
					cv.FONT_HERSHEY_SIMPLEX,
					1, 1
				)

				# Escreve no arquivo access.txt
				with open(".\\security\\access.txt", 'a') as arquivo:
					photo_id = userRandonId()
					arquivo.write(f'{getDateTime()} - USUÁRIO NÃO AUTORIZADO! Cod:{photo_id}\n')
					return photo_id


		# COR AMARELA
		#-----------------------------------------------------   
		_, borda = cv.threshold(grayYellow, 3, 255, cv.THRESH_BINARY)
		contornosYellow, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

		for contorno in contornosYellow:
			area = cv.contourArea(contorno)

			if area > 1200:
				(x, y, w, h) = cv.boundingRect(contorno)
				cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
				cv.putText(
					frame,
					str(f"x: {x} y: {y}"),
					(x, y-20),
					cv.FONT_HERSHEY_SIMPLEX,
					1, 1
				)

				# Escreve no arquivo access.txt
				with open(".\\security\\access.txt", 'a', ) as arquivo:
					photo_id = userRandonId()
					arquivo.write(f'{getDateTime()} - USUÁRIO AUTORIZADO! Cod:{photo_id}\n')
					return photo_id

