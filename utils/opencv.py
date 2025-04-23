import cv2
import numpy as np


def findFace(img_up:np.ndarray) -> np.ndarray:


    gray_image = cv2.cvtColor(img_up, cv2.COLOR_BGR2GRAY)
    #print(gray_image.shape)

    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    for (x, y, w, h) in face:
        cv2.rectangle(img_up, (x, y), (x + w, y + h), (0, 255, 0), 4)

    return img_up