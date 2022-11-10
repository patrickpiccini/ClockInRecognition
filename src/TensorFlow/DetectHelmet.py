# -*- coding: utf-8 -*-
__author__  = 'Patrick Berlatto Piccini'
__title__   = 'Identificação de Capacete usando TensorFlow'
__exename__ = 'main'



# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from utils.Utils import info, debug
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os


class DetectHelmetTensoFLow():

	def __init__(self) -> None:
			# load our serialized face detector model from disk
			info('loading face detector model...')
			self.prototxtPath = "src\\TensorFlow\\data\\deploy.prototxt"
			self.weightsPath = "src\\TensorFlow\\data\\res10_300x300_ssd_iter_140000.caffemodel"
			self.faceNet = cv2.dnn.readNet(self.prototxtPath, self.weightsPath)

			# load the face helmet detector model from disk
			info("loading face helmet detector model...")
			self.helmetNet = load_model("src\TensorFlow\data\helmet_detector.model")

	def detectAndPredictHelmet(self, frame):
		"""Compute the prediction to find the helmet"""

		# grab the dimensions of the frame and then construct a blob
		# from it
		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
			(104.0, 177.0, 123.0))

		# pass the blob through the network and obtain the face detections
		self.faceNet.setInput(blob)
		detections = self.faceNet.forward()

		# initialize our list of faces, their corresponding locations,
		# and the list of predictions from our face helmet network
		faces = []
		locs = []
		preds = []

		# loop over the detections
		for i in range(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with
			# the detection
			confidence = detections[0, 0, i, 2]

			# filter out weak detections by ensuring the confidence is
			# greater than the minimum confidence
			if confidence > 0.5:
				# compute the (x, y)-coordinates of the bounding box for
				# the object
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				# ensure the bounding boxes fall within the dimensions of
				# the frame
				(startX, startY) = (max(0, startX), max(0, startY))
				(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

				# extract the face ROI, convert it from BGR to RGB channel
				# ordering, resize it to 224x224, and preprocess it
				face = frame[startY:endY, startX:endX]
				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
				face = cv2.resize(face, (224, 224))
				face = img_to_array(face)
				face = preprocess_input(face)
				face = np.expand_dims(face, axis=0)

				# add the face and bounding boxes to their respective
				# lists
				faces.append(face)
				locs.append((startX, startY, endX, endY))

		# only make a predictions if at least one face was detected
		if len(faces) > 0:
			# for faster inference we'll make batch predictions on *all*
			# faces at the same time rather than one-by-one predictions
			# in the above `for` loop
			preds = self.helmetNet.predict(faces[0])

		# return a 2-tuple of the face locations and their corresponding
		# locations
		return (locs, preds)

	def callThePredictHelmet(self, frame: object) -> None:
		"""Call the method to do detetion and prediction helmet"""

		(locs, preds) = self.detectAndPredictHelmet(frame)
		debug(locs, preds)

		for (box, pred) in zip(locs, preds):

			(startX, startY, endX, endY) = box
			(helmet, withoutHelmet) = pred
			print(helmet,withoutHelmet)

			label = "Helmet" if helmet > withoutHelmet else "No Helmet"
			color = (0, 255, 0) if label == "Helmet" else (0, 0, 255)

			### Verify percentege without helmet
			# if ......

			label = "{}: {:.2f}%".format(label, max(helmet, withoutHelmet) * 100)

			cv2.putText(frame, label, (startX, startY - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)