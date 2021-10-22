import cv2

cap=cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,img=cap.read()
    img=cv2.flip(img,1)
    cv2.rectangle(img,(30,30),(280,280),(255,255,1),3)
    cv2.imshow("frame",img)
    img1=img[30:280,30:280]
    cv2.imshow("frame2",img1)
    white=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(white,(5,5),0)
    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    hand_resize = cv2.resize(thresh1, (130, 100))
    cv2.imshow("Threshold", thresh1)

    k = 0xFF & cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()