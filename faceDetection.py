import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import cv2

def detectar_rosto(img):
   
    rosto_detectado=False
    detector= FaceDetector(minDetectionCon=0.5,modelSelection=1)
    img,bboxs=detector.findFaces(img,draw=True)
        
  
           
            
            
    return (bboxs,rosto_detectado,img)
    
    
      
        
 
        

            
            
        