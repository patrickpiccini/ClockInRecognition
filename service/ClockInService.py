# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Registro de ponto e gravação de log'
__exename__ = 'main'

import os

from Utils.Utils import error
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

	def registerFace(self, employee_info) -> None:
		try:
			convertImage = ConvertImage()
			DataBase().inserUser(employee_info[0], employee_info[1] , employee_info[2], employee_info[3], employee_info[0])
		except Exception as Error:
			error('Erro ao tentar registrar nova face')
			
	def clockInOfEmployee(self, employee_name, all_clocks) -> None:
		if employee_name:
			print(all_clocks)
			# description = 'Registro de Ponto'
			# DataBase().insertClockInEmployee(employee_name[-5:], description, employee_name[:-6])

