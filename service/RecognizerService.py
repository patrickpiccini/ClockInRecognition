# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Reconhecimento de rostos registrados'
__exename__ = 'main'

import face_recognition
import numpy as np

from .PreperedFilesRecognitionService import PreperedFilesRecognition

class Recognizer(PreperedFilesRecognition):

	def __init__(self) -> None:
		super().__init__()
		self.faces_encodings 		= []
		self.registred_faces_names 	= []
		self.captured_face_locations= []
		self.captured_face_encodings= []
		self.captured_face_names 	= []
		self.recognizeRegisteredFaces()


	def recognizeRegisteredFaces(self) -> None:

		for i in range(len(self.list_of_file)):
			presets = face_recognition.load_image_file(self.list_of_file[i])
			encoding = face_recognition.face_encodings(presets)[0]
			self.faces_encodings.append(encoding)
			self.registred_faces_names.append(self.list_of_names[i])

	def recognizeFaces(self, small_frame: object) -> None:
		self.captured_face_locations = face_recognition.face_locations(small_frame)
		self.captured_face_encodings = face_recognition.face_encodings(
			small_frame, self.captured_face_locations)
		self.captured_face_names = []

		for face_encoding in self.captured_face_encodings:
			matches = face_recognition.compare_faces(
				self.faces_encodings, face_encoding)
			
			## marca ponto aqui

			name = "Desconhecido"
			face_distances = face_recognition.face_distance(
                self.faces_encodings, face_encoding)
			best_match_index = np.argmin(face_distances)
			# print("faces distances", face_distances)

			if matches[best_match_index]:
				name = self.registred_faces_names[best_match_index]

			self.captured_face_names.append(name)
			print(self.captured_face_names)
