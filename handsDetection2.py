from cvzone.HandTrackingModule import HandDetector
import cv2

# codigo base

def detectarMaos(video):
    detector= HandDetector(maxHands=1,detectionCon=0.5,modelComplexity=1)

    while video.isOpened():
        _,img= video.read()
        img=cv2.flip(img,1)
        
        hand_detected,_= detector.findHands(img,draw=True,flipType=False)
        
        if hand_detected:
            hand= hand_detected[0]
            landmarks= hand["lmList"]
    
    
            if hand["type"]=="Right":
                dedos=[8,12,16,20] 
                contador= 0
                fingers= detector.fingersUp(hand)
                
                if landmarks: 
                    if landmarks[4][0]<landmarks[3][0]:
                        contador+=1
                            
                    for x in dedos:
                        if landmarks[x][1]<landmarks[x-2][1]:
                            contador+=1
                
                cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
                cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)    
                    
                
        cv2.imshow("Testando cvzone",img) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
    video.release()
    cv2.destroyAllWindows()
detectarMaos(cv2.VideoCapture(0))  
    
    