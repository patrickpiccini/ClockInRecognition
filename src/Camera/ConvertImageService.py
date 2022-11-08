# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Converte imagens para base64'
__exename__ = 'main'

from utils.Utils import done,error
import base64

class ConvertImage(object):

	def __init__(self) -> None:
		pass

	def encodeImage(self, img: object=None) -> None:
		"""Encode the image to base 64"""
		try:
			with open(img, "rb") as image2string:
				converted_string = base64.b64encode(image2string.read())
				done('Encode realizado com sucesso')
				return (converted_string)
		except Exception as Error:
			error('Erro ao encodificar para Base64',Error)
			
		

	def decodeImage(self, base: object) -> None:
		"""Decode the images from base 64"""
		try:
			decodeit = open('hello_level.jpeg', 'wb')
			decodeit.write(base64.b64decode((base)))
			decodeit.close()
			done('Decode realizado com sucesso')
		except Exception as Error:
			error('Erro ao encodificar para Base64',Error)
			

# if __name__ == "__main__":
# 	base = ConvertImage().encodeImage()
# 	ConvertImage().decodeImage(base)