# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Registro de ponto e gravação de log'
__exename__ = 'main'

import os

from datetime import timedelta, datetime

from Utils.Utils import error,getDateTime
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
			
	def clockInOfEmployee(self, employee_name) -> None:
		description = 'Registro de Ponto'
		employe_id=[]
		has_all_cloks = False
		while has_all_cloks == False:
			all_clocks = DataBase().selectAllClockInDay()
			has_all_cloks = True
			print('--------aqui-------')

		for id in all_clocks:
			employe_id.append(id[0])
			print(employe_id)


		for registred_informations in all_clocks:
			if employee_name[-5:] in employe_id:
				time_now = getDateTime()
				if registred_informations[1] + timedelta(minutes=30) < datetime.now(): 
					DataBase().insertClockInEmployee(employee_name[-5:], description, employee_name[:-6])
					all_clocks = DataBase().selectAllClockInDay()
			else:
				DataBase().insertClockInEmployee(employee_name[-5:], description, employee_name[:-6])
				all_clocks = DataBase().selectAllClockInDay()