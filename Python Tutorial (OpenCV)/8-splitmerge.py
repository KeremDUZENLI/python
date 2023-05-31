import cv2 as cv
import numpy as np


img     = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

blank   = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)


#Split
b,g,r   = cv.split(img)

cv.imshow("B", b)
cv.imshow("G", g)
cv.imshow("R", r)

merged  = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


#Split Color Filter
b,g,r   = cv.split(img)

blue    = cv.merge([b,blank,blank])
green   = cv.merge([blank,g,blank])
red     = cv.merge([blank,blank,r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)



cv.waitKey(0)
