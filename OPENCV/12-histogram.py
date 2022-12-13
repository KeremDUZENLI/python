import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle", circle)

mask1 = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Mask1", mask1)

mask2 = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Mask2", mask2)


#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask1, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


#Color histogram
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

colors = ("b", "g", "r")
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)
