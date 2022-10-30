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

			user_existe, user_id = self.verifyUserExistence(name)

		saved_image = self.screenShot(name, user_id)
		print(saved_image)
		encoded_image = CI.encodeImage(saved_image)
		# print(len(encoded_image))

		# DB.inserUser(self.name_employee , self.age_employee, self.getPassEmployee(), encoded_image)

	def verifyUserExistence(self, name: str) -> bool:
		for _, _, file in os.walk('.\\data\\faces\\'):
			for name_in_file in file:
				if name_in_file[:-10] == name:
					print('='*30)
					choice = input("Usuario com nome já cadastrado!\nDeseja continuar [Y|N] ")

					match choice.lower():
						case "y":
							return True, name_in_file[-9:-4]
						case "n":
							print("------Preencha os dados novamente------")
							return False, None
					return True, None


