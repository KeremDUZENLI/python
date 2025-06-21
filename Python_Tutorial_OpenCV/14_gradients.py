import cv2 as cv
import numpy as np


img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)


#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
cv.imshow("Sobel X", sobelx)

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow("Sobel Y", sobely)

sobel_combine = cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel Combine", sobel_combine)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)



cv.waitKey(0)
