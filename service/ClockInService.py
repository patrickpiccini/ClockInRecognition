# -*- coding: utf-8 -*-
__author__ = 'Patrick Berlatto Piccini'
__title__ = 'Registro de ponto e gravação de log'
__exename__ = 'main'


from .ConvertImageService import ConvertImage
from .DataBaseService import DataBase
from Utils.Utils import debug, error, info
from datetime import timedelta, datetime



class ClockIn(object):

    def __init__(self) -> None:
        self.has_all_cloks = False
        self.all_clocks = []

    def getPassEmployee(self) -> str:
        """Retunr the employee password"""

        return self.__pass_employee

    def setPassEmployee(self, password: str) -> str:
        """Change the employee password"""

        self.__pass_employee = password

    def registerFace(self, employee_info: list, saved_image: str) -> None:
        """Call the insert user from DataBase to try insert our upload user on database"""

        try:
            # convertImage = ConvertImage()
            DataBase().insertUser(
                employee_info[0], employee_info[1], employee_info[2], employee_info[3])
        except Exception as Error:
            error('Erro ao tentar registrar nova face')

    def clockInOfEmployee(self, employee_name: str) -> None:
        """Register the hours of emploeers in database"""

        description = 'Registro de Ponto'
        while self.has_all_cloks == False:
            self.all_clocks = DataBase().selectAllClockInDay()
            self.has_all_cloks = True

        if not self.all_clocks:
            DataBase().insertClockInEmployee(
                employee_name[-5:], description, employee_name[:-6])
            self.all_clocks = DataBase().selectAllClockInDay()
            info("Ponto registrado com sucesso", time=True)
            return True

        len_all_clocks = len(self.all_clocks)
        for index in range(len_all_clocks, -1, -1):
            if employee_name[-5:] == self.all_clocks[index-1][0]:
                if self.all_clocks[index-1][1] + timedelta(minutes=30) < datetime.now():
                    DataBase().insertClockInEmployee(
                        employee_name[-5:], description, employee_name[:-6])
                    self.all_clocks = DataBase().selectAllClockInDay()
                    info("Ponto registrado com sucesso", time=True)
                    return True
                return False

        DataBase().insertClockInEmployee(
            employee_name[-5:], description, employee_name[:-6])
        self.all_clocks = DataBase().selectAllClockInDay()
        info("Ponto registrado com sucesso", time=True)
        return True
