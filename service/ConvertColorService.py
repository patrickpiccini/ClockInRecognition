# -*- coding: utf-8 -*-import cv2
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Controlador de filtro de cores'
__exename__ = 'main'
import cv2 as cv
import numpy as np

class ConvertColor():

    def __init__(self, frame: object) -> None:
        self.cam = frame        

    def convert_to_gray(self) -> object:
        gray = cv.cvtColor(self.cam, cv.COLOR_BGR2GRAY)
        return gray
        
    def convert_to_hvs(self) -> object:
        hvs = cv.cvtColor(self.cam, cv.COLOR_BGR2HSV)
        return hvs

    def convert_to_lab(self) -> object:
        lab = cv.cvtColor(self.cam, cv.COLOR_BGR2LAB)
        return lab

