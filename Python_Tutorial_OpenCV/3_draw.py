import cv2 as cv
from cv2 import circle
import numpy as np


blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow("Blank", blank)


#1. Paint Image
blank[:] = 0,255,0
blank[200:300, 300:400] = 0,0,255
cv.imshow("Green", blank)


#2. Draw Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.rectangle(blank, (250,250), (500,500), (255,0,0), thickness=cv.FILLED)
cv.rectangle(blank, (0,500), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
cv.imshow("Rectangle", blank)


#3. Draw Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow("Circle", blank)


#4. Draw Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("Line", blank)


#5. Write Text
cv.putText(blank, "Hello", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow("Text", blank)



cv.waitKey(0)
