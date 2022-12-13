import cv2 as cv


#Reading Photos
img1 = cv.imread("Photos/cat.jpg")
img2 = cv.imread("Photos/cat_large.jpg")

cv.imshow("Cat 1", img1)
cv.imshow("Cat 2", img2)

cv.waitKey(0)


#Reading Videos
capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("b"):
        break

capture.release()
cv.destroyAllWindows()
