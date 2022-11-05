import numpy as np
import cv2
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


class HelmetCascade():

	def __init__(self) -> None:
		super().__init__()

	def cascade(self):
		while True:
			car_cascade = cv2.CascadeClassifier(".\\models\\train\\cascade.xml")
			ret, frame = camera.read()

			if ret:
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				# hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
				# lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

				objetos = car_cascade.detectMultiScale(gray, 3, 5)
				# objetos = car_cascade.detectMultiScale(hvs, 1.5, 5)
				# objetos = car_cascade.detectMultiScale(lab, 1.5, 5)

				for (x, y, w, h) in objetos:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
					cv2.putText(frame, 'Hemlt', (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
					
				cv2.imshow('Analise', frame)

				key = cv2.waitKey(60)
				if key == "27":
					break
			
			else:
				break
			
		cv2.waitKey(0)	
		camera.release()
		cv2.destroyAllWindows()


if __name__ == "__main__":
	CD = HelmetCascade()
	CD.cascade()
