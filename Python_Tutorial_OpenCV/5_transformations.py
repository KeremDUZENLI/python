from unicodedata import mirrored
import cv2 as cv
import numpy as np


img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)


#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down 

translated = translate(img, 100, 100)
cv.imshow("Translated", translated)


#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)


#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


#Mirror
mirrored = cv.flip(img, 1)
cv.imshow("Mirrored", mirrored)


#Cropping
cropped = img[100:400, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
