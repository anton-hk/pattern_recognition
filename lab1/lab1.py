import cv2

cap = cv2.VideoCapture(0)
success, img = cap.read()
cap.release()
cv2.imshow('1st Window', img)
cv2.imwrite('scrin.png', img)
img = cv2.imread('scrin.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_img.png', imgGray)
imgGray = cv2.imread('gray_img.png')
imgGray = cv2.line(imgGray, (100, 50), (350, 200), (255, 0, 255), 3)
imgGray = cv2.rectangle(imgGray, (384, 333), (510, 128), (0, 255, 0), 3)
cv2.imshow('2nd Window', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()


