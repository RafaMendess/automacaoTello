import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2
# Funciona

def detectar_rosto():
    video= cv2.VideoCapture(0)
    
    detector= FaceDetector(minDetectionCon=0.5,modelSelection=1)
    
    while video.isOpened():
        _,img= video.read()
        
        img,bboxs=detector.findFaces(img,draw=True)
        
        if bboxs:
            bbox= bboxs[0]
            x, y, w, h = bbox["bbox"]
            score = int(bbox["score"][0] * 100)
            
            if score>=80:
                cvzone.putTextRect(img, f'{score}%', (x, y - 10))
                cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0), 2)
            
        cv2.imshow("Testando cvzone",img) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
    video.release()
    cv2.destroyAllWindows()

detectar_rosto()
        

            
            
        