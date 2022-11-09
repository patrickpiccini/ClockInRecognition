# -*- coding: utf-8 -*-
__author__ = 'Patrick Berlatto Piccini'
__title__ = 'Abertura de camera Geral'
__exename__ = 'main'

from ..HaarCascade.HelmCascadeService import HelmetCascade
from ..Recognition.RecognizerService import Recognizer

from utils.Utils import userRandonId, debug, info
import cv2 as cv


# Open notebook camera
class OpenCamera():

    def __init__(self) -> None:
        self.frame = None
        self.value_frame = None
        self.small_frame = None
        self.key = None

    def openCamera(self) -> None:
        """Open communication with camera's hardware"""

        debug("Inicializando Camera...")
        self.camera = cv.VideoCapture(0, cv.CAP_DSHOW)


    def closeCamera(self) -> None:
        """Stop communication with camera's hardware end destroys all windows"""

        debug("Finalizando Camera...")
        self.camera.release()
        cv.destroyAllWindows()


    def readCamera(self) -> None:
        """Read the frames of camera, values and resize to small frame"""

        self.frame = self.camera.read()[1]
        self.value_frame = self.camera.read()[0]
        self.small_frame = cv.resize(self.frame, (0, 0), fx=0.25, fy=0.25)


    def openRecognitionCamera(self) -> None:
        """Recognizes faces with registered users"""

        RE = Recognizer()
        registred_clock = False
        # while registred_clock == False:
        while True:
            self.readCamera()

            registred_clock = RE.recognizeFaces(self.small_frame)
            self.drawFacesIdentificator(
                RE.captured_face_locations, RE.captured_face_names)

            cv.imshow("FaceRecognition", self.frame)
            self.key = cv.waitKey(10)
            if self.key == 27:
                break

        self.closeCamera()


    def screenShot(self, user_id: int = None, name: str = '') -> str:
        """Register new faces on system"""

        if user_id == False:
            user_id = userRandonId()

        while True:
            self.readCamera()
            cv.imshow("Register Face", self.frame)
            self.key = cv.waitKey(10)

            if self.key == 27:
                break

            if self.key == ord('s'):
                saved_dir = f'.\\faces\\{name}_{user_id}.jpg'
                cv.imwrite(saved_dir, self.frame)
                break

        self.closeCamera()
        return saved_dir, user_id


    def helmetHaarCascade(self) -> None:
        """Open camera to identify helmet"""

        HC = HelmetCascade()
        while True:
            self.readCamera()

            if self.value_frame:
                HC.cascade(self.frame)

            cv.imshow("FaceRecognition", self.frame)
            self.key = cv.waitKey(10)
            if self.key == 27:
                break

        self.closeCamera()


    def drawFacesIdentificator(self, face_locations: dict, face_names: dict) -> None:
        """Draw a rectangle and write the employee's name on the camera"""
		
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top = int(top*4)
            right = int(right*4)
            bottom = int(bottom * 4)
            left = int(left * 4)

            # Draw a rectangle around the face
            cv.rectangle(self.frame, (left, top),
                         (right, bottom), (0, 0, 255), 2)

            # Input text label with a name below the face
            cv.rectangle(self.frame, (left, bottom - 35),
                         (right, bottom), (0, 0, 255), cv.FILLED)

            font = cv.FONT_HERSHEY_DUPLEX
            cv.putText(self.frame, name, (left + 6, bottom - 6),
                       font, 0.5, (255, 255, 255), 1)
