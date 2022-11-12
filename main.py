# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from src.DataBase.DataBaseConnection import ConnectionDatabase
from src.RegisterPoint.ClockInService import ClockIn
from src.Camera.StreamService import OpenStream
from src.Camera.CameraService import OpenCamera
import os

from utils.Utils import inputEmployeeData, createRecognizedFacesDir, createSecurityDir, createUnauthorizedAccessyDir, createWithoutHelmetDir, createAccessFile

ConnectionDatabase().create_tables()
createUnauthorizedAccessyDir()
createRecognizedFacesDir()
createWithoutHelmetDir()
createSecurityDir()
createAccessFile()

while True:
	os.system('cls')
	print("{:-^50}\n".format("Bem Vindo ao SnapFace"))
	print("Sistema de gerenciamento de Funcionários em Obras\n" \
	"======================\n" \
	"[1] - Cadastrar Face\n" \
	"[2] - Registro de Ponto\n" \
	"[3] - Monitoramento de Capacete HC\n" \
	"[4] - Monitoramento de Capacete TF\n" \
	"[9] - Sair\n" \
	"======================\n") 
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

