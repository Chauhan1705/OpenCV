import cv2

img = cv2.imread('lena.jpg', -1)
print(img)

cv2.imshow('image', img)        # use to read image
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)    # use to write image
    cv2.destroyAllWindows()

