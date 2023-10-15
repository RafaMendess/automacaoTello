import cv2
import numpy as np
# Não funciona

video= cv2.VideoCapture(0)
hog= cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# img=cv2.imread("testeDeteccao.jpg")



while video.isOpened():
    _,img= video.read()
    img=cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    humans,weights=hog.detectMultiScale(img, winStride=(8, 8),
    padding=(32, 32), scale=1.05)
        
        
    print(humans)
    print(" ")
    print(len(humans))
    if len(humans)!=0:
        for (x, y, w, h) in humans:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
            
    cv2.imshow("Teste",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
            break
     
video.release()
cv2.destroyAllWindows()


    

