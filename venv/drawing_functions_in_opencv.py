# Here we see how to draw different geometric shapes:-

import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)        # it shows background as a image which is seleted
#img = np.zeros([512, 512, 3], np.uint8) # another method which shows backround as black

img = cv2.line(img, (0,0), (255,255), (0, 0, 255), 5)               # to draw a line
img = cv2.arrowedLine(img, (0,255), (255,255), (0, 255, 0), 5)      # to draw a arrow
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)     # to draw a rectangle * if we did -1(thickness) the colur will be filled in the rectangle which is specified before
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)               # to draw a circle
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font,4, (255, 255, 255), 10, cv2.LINE_AA)  # to put some text on image

cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
