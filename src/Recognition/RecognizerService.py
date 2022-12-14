# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Reconhecimento de rostos registrados'
__exename__ = 'main'

import face_recognition, sys
import numpy as np

from .PreperedFilesRecognitionService import PreperedFilesRecognition
from ..RegisterPoint.ClockInService import ClockIn
from utils.Utils import done, error

class Recognizer(PreperedFilesRecognition):

	def __init__(self) -> None:
		super().__init__()
		self.faces_encodings 		= []
		self.registred_faces_names 	= []
		self.captured_face_locations= []
		self.captured_face_encodings= []
		self.captured_face_names 	= []
		self.recognizeRegisteredFaces()
		self.clockIn = ClockIn()



	def recognizeRegisteredFaces(self) -> None:
		"""Identifies faces contained in the Faces directory, and load in "registred_faces_names" var """
		for i in range(len(self.list_of_file)):
			try: 
				presets = face_recognition.load_image_file(self.list_of_file[i])
				encoding = face_recognition.face_encodings(presets)[0]
				self.faces_encodings.append(encoding)
				self.registred_faces_names.append(self.list_of_names[i])
			except IndexError as Erro:

				error("Verifique se há imagem cadastrada sem um rosto claramene exposto",Erro)
				sys.exit(1)


	def recognizeFaces(self, small_frame: object) -> bool:
		registred_clock=False
		self.captured_face_locations = face_recognition.face_locations(small_frame)
		self.captured_face_encodings = face_recognition.face_encodings(
			small_frame, self.captured_face_locations)
		self.captured_face_names = []

		for face_encoding in self.captured_face_encodings:
			matches = face_recognition.compare_faces(
				self.faces_encodings, face_encoding)

			name = "Desconhecido"
			face_distances = face_recognition.face_distance(
				self.faces_encodings, face_encoding)
			best_match_index = np.argmin(face_distances)

			if matches[best_match_index]:
				name = self.registred_faces_names[best_match_index]
				
				# REGISTRE POINT ON DATABASE
				registred_clock = self.clockIn.clockInOfEmployee(name)

			self.captured_face_names.append(name)

		return registred_clock


