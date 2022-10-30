# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from config.DataBaseConnection import ConnectionDatabase
from service.CameraService import OpenCamera
from service.ClockInService import ClockIn

# ConnectionDatabase()
while True:
    print("""======================
[1] - Cadastrar Face
[2] - Registrar Ponto
[9] - Sair
======================""")
    inp = input("escola uma opção: ")

    if inp == "1":
        CI = ClockIn()
        CI.registerFace()
    elif inp =="2":
        OC = OpenCamera()
        OC.openRecognitionCamera()

    elif inp =="9":
        break

