import cv2 

cap = cv2.VideoCapture("image/Video.mp4") #ตำแหน่งที่เก็บวีดีโอ

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame

    if check == True :
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()

