import cv2

aventador = cv2.imread("aventador.jpg")
gray = cv2.cvtColor(aventador, cv2.COLOR_BGR2GRAY)
cv2.imshow("£", gray)
cv2.waitKey(50)

hsv = cv2.cvtColor(aventador, cv2.COLOR_BGR2HSV)
cv2.imshow("££", hsv)
cv2.waitKey(10)

hsv2 = cv2.cvtColor(aventador, cv2.COLOR_BGR2HSV_FULL)
cv2.imshow("£££", hsv2)
cv2.waitKey(10)

r = cv2.rotate(aventador, cv2.ROTATE_180)
cv2.imshow("££££", r)
cv2.waitKey(10)

e = cv2.Canny(aventador, 1, 2)
cv2.imshow("£££££", e)
cv2.waitKey(5437623)