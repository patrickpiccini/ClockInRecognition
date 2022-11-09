# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Interações com Banco de Dados'
__exename__ = 'main'

from utils.Utils import getDateTime, getDate, done, critical
from src.DataBase.DataBaseConnection import ConnectionDatabase

class DataBase(ConnectionDatabase):

	def __init__(self) -> None:
		super().__init__()


	def insertUser(self, employee_id: str ,name: str, age: int, password: str, img=None) -> None:
		try:
			has_user = self.getUser(employee_id)
			date= getDateTime()

			if has_user:
				query_insert = 'UPDATE users SET employee_id=%s, fullname=%s, password=%s, age=%s, created_at=%s, updated_at=%s WHERE employee_id=%s' 
				vars_query = (employee_id,name,password,int(age), date, date,employee_id)
				self.cursor.execute(query_insert, vars_query)
				self.connection.commit()

			else:
				query_insert = 'INSERT INTO users (employee_id, fullname, password, age, created_at, updated_at)VALUES (%s,%s,%s,%s,%s,%s)' 
				vars_query = (employee_id,name,password,int(age), date, date)
				self.cursor.execute(query_insert, vars_query)
				self.connection.commit()

			done('INSERTION DONE IN POSTGRES!')
		except Exception as error:
			critical('ERROR INSERTING IN POSTGRES!',error)
		finally:
			self.cursor.close()

	def getUser(self, employee_id) -> None:
		try:
			query_select = "SELECT employee_id from users where employee_id=%s;"
			vars_query= (employee_id,)
			self.cursor.execute(query_select, vars_query) 
			user = self.cursor.fetchone()
			self.connection.commit()

			done('SELECT DONE SUCCESSFULLY IN POSTGRES!')
			return user
		except Exception as error:
			critical('ERROR SELECT IN POSTGRES! ',error)


	def getAllUsers(self) -> None:
		try:

			query_select = 'SELECT fullname, photo from users;'
			self.cursor.execute(query_select) 
			record = self.cursor.fetchall()
			self.connection.commit()


			dict_all_users = []
			done('SELECT DONE SUCCESSFULLY IN POSTGRES!')
			return dict_all_users
		except Exception as error:
			critical('ERROR INSERTING IN POSTGRES!',error)
		finally:
			self.cursor.close()


	def selectAllClockInDay(self) -> None:
		todays_date = getDate()
		try:
			query_select = f"SELECT employee_id, hour from clockin where date = '{todays_date}' ORDER BY date DESC;"
			self.cursor.execute(query_select) 
			record = self.cursor.fetchall()
			self.connection.commit()

			done('SELECT DONE SUCCESSFULLY IN POSTGRES!')
			return record
		except Exception as error:
			critical('ERROR SELECT IN POSTGRES!',error)
		finally:
			self.cursor.close()


	def insertClockInEmployee(self,employee_id: str,desc: str,name: str) -> None:
		try:
			date = getDate()
			hour = getDateTime()
			query_insert = 'INSERT INTO clockin (employee_id, item_description, fullname, date, hour)VALUES (%s,%s,%s,%s,%s)' 
			vars_query = (employee_id, desc, name, date, hour)
			self.cursor.execute(query_insert, vars_query)
			self.connection.commit()

			done('INSERTION DONE IN POSTGRES!')
		except Exception as error:
			critical('ERROR INSERTING IN POSTGRES!',error)
		finally:
			self.cursor.close()




