import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #images, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#Resizing Photos
img1 = cv.imread("Photos/cat.jpg")
img2 = cv.imread("Photos/cat_large.jpg")

cv.imshow("Cat 1", img1)
cv.imshow("Cat 2", img2)

img1_rescaled = rescaleFrame(img1)
img2_rescaled = rescaleFrame(img2)

cv.imshow("Cat 1 Rescaled", img1_rescaled)
cv.imshow("Cat 2 Rescaled", img2_rescaled)
cv.waitKey(0)


#Resizing Videos
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("b"):
        break

capture.release()
cv.destroyAllWindows()
