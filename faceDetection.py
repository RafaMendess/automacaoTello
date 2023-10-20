import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2

def detectar_rosto(img):
   
    rosto_detectado=False
    detector= FaceDetector(minDetectionCon=0.5,modelSelection=1)
    img,bboxs=detector.findFaces(img,draw=True)
    
    if bboxs:
        rosto_detectado=True
            
    return (bboxs,rosto_detectado,img)
    
def detectar_rosto2 (video):
    detector= FaceDetector(minDetectionCon=0.5,modelSelection=1)
    while True:
        img= cv2.flip(video.read()[1],1)
      
        img,bboxs=detector.findFaces(img,draw=True)
        
        cv2.imshow("Deteccao de rosto",img)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    cv2.destroyAllWindows()


detectar_rosto2(cv2.VideoCapture(0))
        
 
        

            
            
        