# -*- coding: utf-8 -*- 
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Montagen de dados para reconhecimento'
__exename__ = 'main'

import cv2
import numpy as np
import glob, os

EXTENSION_FILES = ["png", "jpeg", "jpg"]

class PreperedFilesRecognition(object):

	def __init__(self) -> None:
		self.current_dir 	= os.getcwd()
		self.face_dir		= os.path.join(self.current_dir + '\\data\\faces\\')
		self.face_clock_in  = os.path.join(self.current_dir + '\\data\\clockin\\')
		self.list_of_file 	= []
		self.list_of_names	= []
		
		self.createRecognizedFacesDir()
		self.createFaceClockInDir()
		

	def createRecognizedFacesDir(self) -> None:
		if not os.path.exists(self.face_dir):
			os.mkdir(self.current_dir + "\\data\\faces\\")

		self.loadListOfFiles()
	
	def createFaceClockInDir(self) -> None:
		if not os.path.exists(self.face_clock_in):
			os.mkdir(self.current_dir + "\\data\\clockin\\")


	def loadListOfFiles(self) -> None:
		for ext in EXTENSION_FILES:
			for f in glob.glob(self.face_dir + f"*.{ext}"):
				self.list_of_file.append(f)

		self.replaceNameFromFaceFiles()


	def replaceNameFromFaceFiles(self) -> None:
		for file in self.list_of_file:
			name = ''
			for ext in EXTENSION_FILES:
				name = file.replace(self.face_dir, '').replace(f".{ext}", '')
				
			self.list_of_names.append(name)



# if __name__ == "__main__":
# 	FR= PreperedFilesRecognition()
# 	FR.loadListOfFiles()
