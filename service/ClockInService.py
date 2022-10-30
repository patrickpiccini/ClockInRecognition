# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Registro de ponto e gravação de log'
__exename__ = 'main'

import os

from .CameraService import OpenCamera
from .ConvertImageService import ConvertImage
from .DataBaseService import DataBase

class ClockIn(OpenCamera):

	def __init__(self) -> None:
		super().__init__()
		pass

	def getPassEmployee(self) -> str:
		return self.__pass_employee

	def setPassEmployee(self, password: str) -> str:
		self.__pass_employee = password

	def registerFace(self) -> None:
		CI = ConvertImage()
		# DB = DataBase()
		user_existe = False
		while user_existe == False:
			name = input("Nome do colaborador: ")
			age = input("Idade do colaborador: ")
			password = input("Senha do colaborador: ")
			# name = 'patrick berlatto piccini'
			# age = '23'
			# password = 'teste'
			# password_again = input("Repita a Senha:  ")
			# if password_again == password:

			user_existe = self.verifyUserExistence(name)

		saved_image = self.screenShot(name)
		print(saved_image)
		encoded_image = CI.encodeImage(saved_image)
		# print(len(encoded_image))

		# DB.inserUser(self.name_employee , self.age_employee, self.getPassEmployee(), encoded_image)

	def verifyUserExistence(self, name):
		dir = f'.\\data\\faces\\{name}.jpg'
		if os.path.exists(dir):
			print('='*30)
			choice = input("Usuario com nome já cadastrado!\nDeseja continuar [Y|N] ")

			match choice.lower():
				case "y":
					return True
				case "n":
					print("------Preencha os dados novamente------")
					return False
		return True


