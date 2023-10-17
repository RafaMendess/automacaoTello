from djitellopy import tello
import time
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
from threading import Thread

class CustomThread01(Thread):
    def __init__(self, img):
        Thread.__init__(self)
        self.img = img
        self.rosto_detectado = False
        self.bboxs = []

    def run(self):
        detector = FaceDetector(minDetectionCon=0.5,modelSelection=1)
        self.img, self.bboxs=detector.findFaces(self.img,draw=False)  

        if self.bboxs:
            self.rosto_detectado = True
            
class CustomThread02(Thread):
    def __init__(self, img):
        Thread.__init__(self)
        self.img = img

    def run(self):
            if self.img is None:
                return

            detector = HandDetector(maxHands=1,detectionCon=0.5,modelComplexity=1)
            hand_detected,_ = detector.findHands(self.img,draw=True,flipType=False)

            if not hand_detected:
                return
            
            hand = hand_detected[0]
            landmarks = hand["lmList"]
                    # detecta apenas a mão direita 
            if hand["type"] != "Right":
                return 
            
            dedos = [8, 12, 16, 20]
            contador = 0

            if not landmarks:
                return 
            
            for x in dedos:
                if landmarks[x][1] < landmarks[x-2][1]:
                    contador += 1

                    #  Detecta se apenas o dedão ta levantado
            if landmarks[4][0] < landmarks[3][0] :
                print("mover a esquerda")
                # me.move_left(30)
                contador += 1
            
                    # detecta se apenas o mindinho ta levantado
            elif contador==1 and landmarks[20][1]<landmarks[18][1]:
                print("mover para direita")
                # me.move_right(30)
                
                # Apenas indicador levantado
            elif contador==1 and landmarks[8][1]<landmarks[6][1]:
                print("subindo")
                # me.move_up(10)

                    # Dedão e mindinho levantado
            if contador==2 and landmarks[4][0] < landmarks[3][0] and landmarks[20][1]<landmarks[18][1]:
                print("flip para tras")
                # me.flip_back()
                    
                    # Desliga fazendo se fizer três dedos para cima
            if contador==3 and landmarks[4][0]> landmarks[3][0] and landmarks[20][1]>landmarks[18][1]:
                print("Desligando...")
                # print(f'Bateria: {battery}',end=" ")
                # me.move_forward(10)
                # me.land()

            cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
            cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)
            





#################################################################################




def detectar_rosto(img):
    rosto_detectado=False
    detector = FaceDetector(minDetectionCon=0.5,modelSelection=1)
    img,bboxs=detector.findFaces(img,draw=True)  

    if bboxs:
        rosto_detectado = True                 
            
    return (bboxs,rosto_detectado,img)
    
def detectaMao(img):
    if img is None:
        return img
    
    detector = HandDetector(maxHands=1,detectionCon=0.5,modelComplexity=1)
    hand_detected,_ = detector.findHands(img,draw=True,flipType=False)

    if not hand_detected:
        return img
    
    hand = hand_detected[0]
    landmarks = hand["lmList"]
            # detecta apenas a mão direita 
    if hand["type"] != "Right":
        return img
    
    dedos = [8, 12, 16, 20]
    contador = 0

    if not landmarks:
        return img
    
    for x in dedos:
        if landmarks[x][1] < landmarks[x-2][1]:
            contador += 1

            #  Detecta se apenas o dedão ta levantado
    if landmarks[4][0] < landmarks[3][0] :
        print("mover a esquerda")
        # me.move_left(30)
        contador += 1
    
            # detecta se apenas o mindinho ta levantado
    elif contador==1 and landmarks[20][1]<landmarks[18][1]:
        print("mover para direita")
        # me.move_right(30)
        
        # Apenas indicador levantado
    elif contador==1 and landmarks[8][1]<landmarks[6][1]:
        print("subindo")
        # me.move_up(10)

            # Dedão e mindinho levantado
    if contador==2 and landmarks[4][0] < landmarks[3][0] and landmarks[20][1]<landmarks[18][1]:
        print("flip para tras")
        # me.flip_back()
            
            # Desliga fazendo se fizer três dedos para cima
    if contador==3 and landmarks[4][0]> landmarks[3][0] and landmarks[20][1]>landmarks[18][1]:
        print("Desligando...")
        # print(f'Bateria: {battery}',end=" ")
        # me.move_forward(10)
        # me.land()

    cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
    cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)

    return img




#################################################################################    




#run = True
#listener = keyboard.Listener(on_press=on_press)
#listener.start()  # start to listen on a separate thread
#listener.join()  # remove if main thread is polling self.keys

#me = tello.Tello()

#me.connect()
#print(me.get_battery())
#print(me.get_temperature())

#me.streamon()
#me.set_video_fps("Tello.FPS_30")

video = cv2.VideoCapture(0)
# video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

try:
    while video.isOpened():

        #img = me.get_frame_read().frame
        _,img = video.read()
        img = cv2.flip(img, 1)

        bboxs,rosto_detectado,img=detectar_rosto(img)

        if rosto_detectado:
            bbox = bboxs[0]
            score= int(bbox['score'][0]*100)
        
        img = detectaMao(img)

        img_certa = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("frame", img)
        #cv2.imshow("frame", img_certa)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            cv2.destroyAllWindows()
            break
        
        #print(me.get_battery())
        #print(me.get_temperature())
        
        #if (me.get_battery() < 40):
        #    print("low battery level")
        #    break

    

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    exit(0) 
finally:
    #me.streamoff()
    #listener.join()
    print("end")

