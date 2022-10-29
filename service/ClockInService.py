# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Registro de ponto e gravação de log'
__exename__ = 'main'

from .OpenCamService import OpenCamera
from .ConvertImageService import ConvertImage
from .DataBaseService import DataBase

class ClockIn(OpenCamera):

	def __init__(self, name, age, password) -> None:
		super().__init__()
		self.name_employee = name
		self.age_employee = age
		self.__pass_employee = password

	def getPassEmployee(self) -> str:
		return self.__pass_employee

	def setPassEmployee(self, password: str) -> str:
		self.__pass_employee = password

	def registerFace(self) -> None:
		CI = ConvertImage()
		DB = DataBase()
		salved_image = self.screenShot(self.name_employee)
		encoded_image = CI.encodeImage(salved_image)

		DB.inserUser(self.name_employee , self.age_employee, self.getPassEmployee(), encoded_image)



