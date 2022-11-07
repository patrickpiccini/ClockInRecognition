# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from config.DataBaseConnection import ConnectionDatabase
from service.CameraService import OpenCamera
from service.ClockInService import ClockIn

from Utils.Utils import inputEmployeeData

ConnectionDatabase().create_tables()

while True:
	print("""=== Bem Vindo ao SnapFace ===
Sistema de gerenciamento de Funcionários em Obras\n
======================
[1] - Cadastrar Face
[2] - Registrar Ponto
[3] - Reconhecimento de Capacete
[9] - Sair
======================""")
	key = int(input("Escolha uma opção: "))

	match key:

		case 1:
			opanCamera = OpenCamera()
			clockIn = ClockIn()
			employee_info = inputEmployeeData()
			saved_image, employee_info[0] = opanCamera.screenShot(employee_info[0], employee_info[1])
			clockIn.registerFace(employee_info, saved_image)
		case 2:
			opanCamera = OpenCamera()
			opanCamera.openRecognitionCamera()
		case 3:
			opanCamera = OpenCamera()
			opanCamera.helmetHaarCascade()
		case 9:
				break

