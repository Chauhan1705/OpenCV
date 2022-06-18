# Here if we cick left mouse button it should draw a circle and then if we click on next point will be join by the line :-

import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]     to see al the classes which has EVENT name
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >=2 :
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)

img = np.zeros((512, 512, 3), np.uint8)
#img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()