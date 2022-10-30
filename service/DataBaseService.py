# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Interações com Banco de Dados'
__exename__ = 'main'

import base64
from distutils import extension
import cv2 as cv
from datetime import datetime

from config.DataBaseConnection import ConnectionDatabase

class DataBase(ConnectionDatabase):

	def __init__(self) -> None:
		super().__init__()


	def getDateTime(self) -> str:
		date_time_now = datetime.now()
		return date_time_now.strftime('%Y/%m/%d %H:%M')


	def inserUser(self, name: str, age: int, password: str, img) -> None:
		try:
			date= self.getDateTime()
			query_insert = 'INSERT INTO users (fullname, password, age, photo, created_at, updated_at)VALUES (%s,%s,%s,%s,%s,%s)' 
			vars_query = (name,password,int(age),img, date, date)
			self.cursor.execute(query_insert, vars_query)
			self.connection.commit()

			print('[✓] INSERTION DONE IN POSTGRES!')
		except Exception as error:
			print(error)
			return f'[X] ERROR INSERTING IN POSTGRES! {error}'
		finally:
			self.cursor.close()

	def getAllUsers(self) -> None:
		try:

			query_select = 'SELECT fullname, photo from users;'
			self.cursor.execute(query_select) 
			record = self.cursor.fetchall()
			self.connection.commit()
			print(record)

			dict_all_users = []
			print('[✓] SELECT DONE SUCCESSFULLY IN POSTGRES!')
			return dict_all_users
		except Exception as error:
			print(error)
			return f'[X] ERROR INSERTING IN POSTGRES! {error}'
		finally:
			self.cursor.close()





