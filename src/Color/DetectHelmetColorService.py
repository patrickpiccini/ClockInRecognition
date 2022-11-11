import cv2 as cv
import numpy as np

from ..Color.ConvertColorService import ConvertColor


class DetectHelmetColor():

	def __init__(self) -> None:
		self.Color = ConvertColor()
		self.LOWER_BLUE = np.array([94,121,40])
		self.UPPER_BLUE = np.array([137,250,255])

		self.LOWER_RED = np.array([0,161,75])
		self.UPPER_RED = np.array([16,255,220])
		
		self.LOWER_GREEN = np.array([40,101,23])
		self.UPPER_GREEN = np.array([59,250,158])
		
		self.LOWER_YELLOW = np.array([14, 60, 169])
		self.UPPER_YELLOW = np.array([35,255,255])   

	def helmetColor(self, frame) -> None:
		hsv = self.Color.convert_to_hsv(frame)
		mask = cv.inRange(hsv, self.LOWER_YELLOW, self.UPPER_YELLOW)
		result = cv.bitwise_and(frame, frame, mask=mask)

		gray = self.Color.convert_to_gray(frame)
		_, borda = cv.threshold(gray, 3, 255, cv.THRESH_BINARY)

		contornos, _ = cv.findContours(
			borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

		for contorno in contornos:
			area = cv.contourArea(contorno)
			if area > 800:
				(x, y, w, h) = cv.boundingRect(contorno)
				#cv.drawContours(frame, contorno, -1, (255,0,0), 2)
				cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
				cv.putText(
					frame,
					str(f"x: {x} y: {y}"),
					(x, y-20),
					cv.FONT_HERSHEY_SIMPLEX,
					1, 1
				)


camera = cv.VideoCapture(0, cv.CAP_DSHOW)


# while 1:
#     _, frame = camera.read()
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     lowerBlue = np.array([102, 74, 112])
#     upperBlue = np.array([255, 255, 255])

#     mask = cv.inRange(hsv, lowerBlue, upperBlue)
#     result = cv.bitwise_and(frame, frame, mask=mask)

#     gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
#     _, borda = cv.threshold(gray, 3, 255, cv.THRESH_BINARY)

#     contornos, _ = cv.findContours(
#         borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#     for contorno in contornos:
#         area = cv.contourArea(contorno)
#         if area > 800:
#             (x, y, w, h) = cv.boundingRect(contorno)
#             #cv.drawContours(frame, contorno, -1, (255,0,0), 2)
#             cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
#             cv.putText(
#                 frame,
#                 str(f"x: {x} y: {y}"),
#                 (x, y-20),
#                 cv.FONT_HERSHEY_SIMPLEX,
#                 1, 1
#             )

#     #cv.imshow("result mask", borda)
#     cv.imshow("result", frame)
#     k = cv.waitKey(60)
#     if k == 27:
#         break

# camera.release()
# cv.destroyAllWindows()