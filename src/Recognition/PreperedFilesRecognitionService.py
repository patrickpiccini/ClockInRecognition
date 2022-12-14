# -*- coding: utf-8 -*- 
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Montagen de dados para reconhecimento facial'
__exename__ = 'main'

import glob, os

EXTENSION_FILES = ["png", "jpeg", "jpg"]

class PreperedFilesRecognition(object):

	def __init__(self) -> None:
		self.current_dir 	= os.getcwd()
		self.face_dir		= os.path.join(self.current_dir + '\\faces\\')
		self.list_of_file 	= []
		self.list_of_names	= []
		
		self.loadListOfFiles()
		
	
	def loadListOfFiles(self) -> None:
		"""Load the list os files on face dir"""
		for ext in EXTENSION_FILES:
			for f in glob.glob(self.face_dir + f"*.{ext}"):
				self.list_of_file.append(f)

		self.replaceNameFromFaceFiles()


	def replaceNameFromFaceFiles(self) -> None:
		"""Load the list os names on face dir"""
		for file in self.list_of_file:
			name = ''
			for ext in EXTENSION_FILES:
				name = file.replace(self.face_dir, '').replace(f".{ext}", '')
				
			self.list_of_names.append(name)



# if __name__ == "__main__":
# 	FR= PreperedFilesRecognition()
# 	FR.loadListOfFiles()

