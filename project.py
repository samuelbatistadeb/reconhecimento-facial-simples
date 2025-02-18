import numpy as np
import cv2 as cv

face_classifier = cv.CascadeClassifier('haarcascade_frontface_default.xml')

image = cv.imready('image.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()