# Here we use some basic arthemetic operations on image using opencv:-

import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo.png')

print(img.shape)    # return a tuple of number of rows, columns, and channels
print(img.size)     # return total number of pixels is accessed
print(img.dtype)    # return image datatype is obtained
b,g,r = cv.split(img)
img   = cv.merge((b,g,r))

# Here we copy an image(ball) to the another index of the image:-
ball = img[280:340, 330:390]    # actual co-ordinates of ball
img[273:333, 100:160] = ball    # co-ordinates of ball where we want to copy

# Here we resize the images for adding them:-
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

# Here we add two images :- (Note - we can only add images of arrays of same size)
#dst = cv.add(img, img2);

# There is also a method in which we can adjust the %tage of images  overlapping known as addWeighted method
dst = cv.addWeighted(img, .9,  img2, .1, 0);    # here 90% messi image is overlapped on openCV image( we can change the perecenntage )

cv.imshow('image', dst)

#cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()
