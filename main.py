# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'title'
__exename__ = 'main'

from config.DataBaseConnection import ConnectionDatabase
from service.OpenCamService import OpenCamera
from service.ClockInService import ClockIn

ConnectionDatabase()

print("1 - cadastrar face | 2 - Registrar Ponto")
inp = input("escola uma opção: ")

if inp == "1":
    name = input("Nome do colaborador: ")
    age = input("Idade do colaborador: ")
    password = input("Senha do colaborador: ")
    # name = 'Gab'
    # age = '23'
    # password = 'teste'
    # password_again = input("Repita a Senha:  ")
    # if password_again == password:
    CI = ClockIn(name, age, password)
    CI.registerFace()
elif inp =="2":

    OC = OpenCamera()
    OC.openRecognitionCamera()

