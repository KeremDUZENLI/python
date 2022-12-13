import cv2 as cv
import numpy as np


img = cv.imread("Photos/cats 2.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)


#Mask 1
mask1 = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask1", mask1)

masked1 = cv.bitwise_and(img, img, mask=mask1)
cv.imshow("Masked1", masked1)


#Mask 2
mask2 = cv.rectangle(blank.copy(), (100,100), (400,400), 255, -1)
cv.imshow("Mask2", mask2)

masked2 = cv.bitwise_and(img, img, mask=mask2)
cv.imshow("Masked2", masked2)


#Mask 3
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
weird_shape = cv.bitwise_and(rectangle, circle)
cv.imshow("Weird Shape", weird_shape)

masked_weird = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked Weird", masked_weird)



cv.waitKey(0)
