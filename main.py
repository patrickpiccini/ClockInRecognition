# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from config.DataBaseConnection import ConnectionDatabase
from service.CameraService import OpenCamera
from service.ClockInService import ClockIn

from Utils.Utils import inputEmployeeData

# ConnectionDatabase()

while True:
	print("""======================
[1] - Cadastrar Face
[2] - Registrar Ponto
[9] - Sair
======================""")
	inp = int(input("Escolha uma opção: "))

	match inp:

		case 1:
			opanCamera = OpenCamera()
			clockIn = ClockIn()
			employee_info = inputEmployeeData()
			saved_image, employee_info[0] = opanCamera.screenShot(employee_info[0], employee_info[1])
			clockIn.registerFace(employee_info)
		case 2:
			opanCamera = OpenCamera()
			opanCamera.openRecognitionCamera()
		case 9:
				break

