# -*- coding: utf-8 -*-import cv2
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Controlador de filtro de cores'
__exename__ = 'main'

import cv2 as cv

class ConvertColor():

	def __init__(self, frame: object) -> None:
		self.frame = frame        

	def convert_to_gray(self) -> object:
		"""Corver the frames to GARY scale"""
		gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
		return gray
		
	def convert_to_hsv(self) -> object:
		"""Corver the frames to HSV scale"""
		hvs = cv.cvtColor(self.frame, cv.COLOR_BGR2HSV)
		return hvs

	def convert_to_lab(self) -> object:
		"""Corver the frames to LAB scale"""
		lab = cv.cvtColor(self.frame, cv.COLOR_BGR2LAB)
		return lab

