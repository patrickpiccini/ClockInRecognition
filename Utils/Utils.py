# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Funções para uso geral no sistema'
__exename__ = 'main'


import os, random
from datetime import datetime


def userRandonId() -> str :
	"""Generate a random number in to be a user_id"""
	number = random.randint(1,10000)
	return str(f'{number:0>5}')


def getDateTime() -> str:
	"""Get day and hour"""
	date_time_now = datetime.now()
	return date_time_now.strftime('%d/%m/%Y %H:%M')


def getDate() -> str:
	"""Get only day"""
	date_time_now = datetime.now()
	return date_time_now.strftime('%d-%m-%Y')


def inputEmployeeData() -> list:
	"""
	Registre the new person face.\n
	It is necessary input a ``Full Name``, ``Age`` and ``Password`` 
	"""
	user_existe = False
	while user_existe == False:
		employee_name = input("Nome do colaborador: ").lower().replace(' ','_')
		employee_age = int(input("Idade do colaborador: "))
		psw = True
		while psw == True:
			employee_password = input("Senha do colaborador: ")
			break
		# password_again = input("Repita a Senha:  ")
		# if password_again == password:

		user_existe, employee_id = verifyUserExistence(employee_name)

	return [employee_id , employee_name, employee_age, employee_password]


def verifyUserExistence(name: str) -> bool:
	"""
	Check if the same employee name is registered.\n
	Wait for the user to say if they want to update the employee's photo or rewrite the employee's data.
	"""
	for _, _, file in os.walk('.\\faces\\'):
		for name_in_file in file:
			if name_in_file[:-10] == name:
				print('='*30)
				info("Usuario com nome já cadastrado!")
				choice = input("Deseja atualizar [Y|N] ")

				match choice.lower():
					case "y":
						debug('Abrindo Camera')
						info('Pressione "S" para capturara foto')
						return True, name_in_file[-9:-4]
					case "n":
						info("------Preencha os dados novamente------")
						return False, False
	return True, False



def createRecognizedFacesDir() -> None:
	"""Verify and create face dir if not exists"""
	if not os.path.exists(os.getcwd()+'\\faces\\'):
		os.mkdir(os.getcwd()+'\\faces\\')

def createSecurityDir() -> None:
	"""Verify and create security dir if not exists"""
	if not os.path.exists(os.getcwd()+'\\security\\'):
		os.mkdir(os.getcwd()+'\\security\\')

def createUnauthorizedAccessyDir() -> None:
	"""Verify and create unauthorized_access dir if not exists"""
	if not os.path.exists(os.getcwd()+'\\security\\unauthorized_access\\'):
		os.mkdir(os.getcwd()+'\\security\\unauthorized_access\\')

def createWithoutHelmetDir() -> None:
	"""Verify and create without_helmet dir if not exists"""
	if not os.path.exists(os.getcwd()+'\\security\\without_helmet\\'):
		os.mkdir(os.getcwd()+'\\security\\without_helmet\\')

def createAccessFile() -> None:
	"""Create access file"""
	arquivo = open('.\\security\\access.txt', 'w')
	arquivo.close()



def done(text,error='',time='')-> str:
	if time:
		time = " "+getDateTime()
	if error:
		error = '\n',error
	print(f'\033[1m\033[32m[√] SUCESSO:\033[0;0m{time} {text}{error}')

def warning(text,error='',time='') -> str:
	if time:
		time = getDateTime()
	print(f'\033[1m\033[33m[!] WARNIN:\033[0;0m{time} {text}{error}')

def error(text,error='',time='')-> str:
	if time:
		time = getDateTime()
	print(f'\033[1m\033[31m[X] ERROR:\033[0;0m{time} {text}{error}')

def info(text,error='',time='')-> str:
	if time:
		time = getDateTime()
	print(f'\033[1m\033[34m[!] INFO:\033[0;0m{time} {text}{error}')

def debug(text,error='',time='')-> str:
	if time:
		time = getDateTime()
	print(f'\033[0m\033[33m[>] DEGUB:\033[0;0m{time} {text}{error}')

def critical(text,error='',time='')-> str:
	if time:
		time = getDateTime()
	print(f'\033[3m\033[41m[#] CRITICAL:\033[0;0m{time} {text}{error}')