import cv2

img = cv2.imread("image/cat.jpg")   #image read
print(type(img.ndim))
print(img)