# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Registro de ponto e gravação de log'
__exename__ = 'main'

import os

from .DataBaseService import DataBase
from .ConvertImageService import ConvertImage

class ClockIn(object):

	def __init__(self) -> None:
		pass

	def getPassEmployee(self) -> str:
		"""
		Retunr the employee password
		"""
		return self.__pass_employee

	def setPassEmployee(self, password: str) -> str:
		"""
		Change the employee password
		"""
		self.__pass_employee = password

	def registerFace(self) -> None:
		"""
		Registre the new person face.\n
		It is necessary input a ``Full Name``, ``Age`` and ``Password`` 
		"""
		CI = ConvertImage()
		user_existe = False
		while user_existe == False:
			employee_name = input("Nome do colaborador: ").lower().replace(' ','_')
			employee_age = int(input("Idade do colaborador: "))
			employee_password = input("Senha do colaborador: ")
			# password_again = input("Repita a Senha:  ")
			# if password_again == password:

			user_existe, employee_id = self.verifyUserExistence(employee_name)

		return [employee_id , employee_name, employee_age, employee_password]
		

	def verifyUserExistence(self, name: str) -> bool:
		"""
		Check if the same employee name is registered.\n
		Wait for the user to say if they want to update the employee's photo or rewrite the employee's data.
		"""
		for _, _, file in os.walk('.\\data\\faces\\'):
			for name_in_file in file:
				if name_in_file[:-10] == name:
					print('='*30)
					choice = input("Usuario com nome já cadastrado!\nDeseja atualizar [Y|N] ")

					match choice.lower():
						case "y":
							return True, name_in_file[-9:-4]
						case "n":
							print("------Preencha os dados novamente------")
							return False, False
		return True, False

	def clockInOfEmployee(self, employee_name, all_clocks) -> None:
		if employee_name:
			print(all_clocks)
			# description = 'Registro de Ponto'
			# DataBase().insertClockInEmployee(employee_name[-5:], description, employee_name[:-6])

