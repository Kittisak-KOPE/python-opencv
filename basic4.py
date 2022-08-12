import cv2

img = cv2.imread("image/cat.jpg",-1) #mode 0 : gray scale, 1 : color, -1 with alpha chanel
imgresize = cv2.resize(img,(400,400))

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()