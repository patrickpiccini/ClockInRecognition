# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from config.DataBaseConnection import ConnectionDatabase
from service.ConvertImageService import ConvertImage
from service.DataBaseService import DataBase
from service.CameraService import OpenCamera
from service.ClockInService import ClockIn

ConnectionDatabase()
while True:
	print("""======================
[1] - Cadastrar Face
[2] - Registrar Ponto
[9] - Sair
======================""")
	inp = int(input("Escolha uma opção: "))

	match inp:

		case 1:
			OC = OpenCamera()
			CI =  ClockIn()
			COI = ConvertImage()
			employee_info = CI.registerFace()
			print(employee_info)
			saved_image, employee_info[0] = OC.screenShot(employee_info[0], employee_info[1])
			# encoded_image = COI.encodeImage(saved_image)

			DataBase().inserUser(employee_info[0], employee_info[1] , employee_info[2], employee_info[3], employee_info[0])
		case 2:
			OC = OpenCamera()
			OC.openRecognitionCamera()
		case 9:
				break

