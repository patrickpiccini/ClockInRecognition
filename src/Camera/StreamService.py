# -*- coding: utf-8 -*-
__author__ = 'Patrick Berlatto Piccini'
__title__ = 'Abertura de camera Geral'
__exename__ = 'main'

from ..TensorFlow.DetectHelmet import DetectHelmetTensoFLow
from imutils.video import VideoStream
from utils.Utils import info
import cv2

class OpenStream():

    def __init__(self) -> None:
        self.video_stream = None
        self.stream_frame = None


    def openVideoStream(self) -> None:
        """Start the video streaming"""

        info('Starting video stream...')
        self.video_stream = VideoStream(src=0).start()


    def closeVideoStream(self) -> None:
        """Stoping the video streaming"""

        info('Stoping video stream...')
        self.video_stream.stop()
        cv2.destroyAllWindows()


    def readVideoStrem(self) -> None:
       self.stream_frame = self.video_stream.read()


    def helmetTensorFLow(self) -> None:
        DHTF = DetectHelmetTensoFLow()
        while True:
            self.readVideoStrem()
            DHTF.renderizeVideoStream(self.stream_frame)
            # show the output frame
            cv2.imshow("Frame", self.stream_frame)
            key = cv2.waitKey(1) & 0xFF

            # if the `esc` key was pressed, break from the loop
            if key == 27:
                break
        
        self.closeVideoStream()
