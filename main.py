# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from src.DataBase.DataBaseConnection import ConnectionDatabase
from src.RegisterPoint.ClockInService import ClockIn
from src.Camera.StreamService import OpenStream
from src.Camera.CameraService import OpenCamera

from utils.Utils import inputEmployeeData

ConnectionDatabase().create_tables()

while True:
	print("""=== Bem Vindo ao SnapFace ===
Sistema de gerenciamento de Funcionários em Obras\n
======================
[1] - Cadastrar Face
[2] - Registrar Ponto
[3] - Reconhecimento de Capacete HC
[4] - Reconhecimento de Capacete TF
[9] - Sair
======================""")
	key = int(input("Escolha uma opção: "))

	match key:

		case 1:
			openCamera = OpenCamera()
			openCamera.openCamera()
			clockIn = ClockIn()
			employee_info = inputEmployeeData()
			saved_image, employee_info[0] = openCamera.screenShot(employee_info[0], employee_info[1])
			clockIn.registerFace(employee_info, saved_image)
		case 2:
			openCamera = OpenCamera()
			openCamera.openCamera()
			openCamera.openRecognitionCamera()
		case 3:
			openCamera = OpenCamera()
			openCamera.openCamera()
			openCamera.helmetHaarCascade()
		case 4:
			openStream = OpenStream()
			openStream.openVideoStream()
			openStream.helmetTensorFLow()
		case 9:
				break

