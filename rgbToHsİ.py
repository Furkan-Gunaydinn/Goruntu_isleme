import cv2

img = cv2.imread("teska.jpg")
imgh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("araba", img)
cv2.imshow("hsv",imgh)
cv2.waitKey(0)
