# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Registro de ponto e gravação de log'
__exename__ = 'main'


import base64

class ConvertImage(object):

	def __init__(self) -> None:
		pass

	def encodeImage(self, img: object=None) -> None:
		with open(img, "rb") as image2string:
			converted_string = base64.b64encode(image2string.read())
			return (converted_string)
		

	def decodeImage(self, base: object) -> None:
		decodeit = open('hello_level.jpeg', 'wb')
		decodeit.write(base64.b64decode((base)))
		decodeit.close()

# if __name__ == "__main__":
# 	base = ConvertImage().encodeImage()
# 	ConvertImage().decodeImage(base)