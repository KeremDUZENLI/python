import cv2 as cv


img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)


#Convert Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)


#Edge Cascade
canny1 = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny1)

canny2 = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edge Blur", canny2)


#Dilating Image
dilated = cv.dilate(canny2, (7,7), iterations=3)
cv.imshow("Dilated", dilated)


#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)


#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized No Ratio", resized)


#Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
