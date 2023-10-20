import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
from djitellopy import Tello 

def detectar_maos():
    detector = HandDetector(maxHands=1, detectionCon=0.5, modelComplexity=1)
    me= Tello()
    me.connect()
    me.streamon()
    
    # me.set_video_fps(Tello.FPS_30)
    # me.set_video_resolution(me.RESOLUTION_480P)
    
    # me.takeoff()
   
    
    
    battery= me.get_battery()
    if battery<=30:
        print(f'Bateria: {battery}')
        return
    
    while True:
        img= me.get_frame_read().frame
        hand_detected,img= detector.findHands(img, draw=True, flipType=True)
        if hand_detected:
            hand = hand_detected[0]
            landmarks = hand["lmList"]
                    # detecta apenas a mão direita 
            if hand["type"] == "Right":
                print(landmarks)
                dedos = [8, 12, 16, 20]
                contador = 0
                
                if landmarks: 
                                 
                    for x in dedos:
                        if landmarks[x][1] < landmarks[x-2][1]:
                          contador += 1
                                    
                             #  Detecta se apenas o dedão ta levantado
                        if landmarks[4][0] > landmarks[3][0] :
                            contador += 1
                            if contador==1:
                                print("mover a esquerda")
                                    # me.move_left(30)
                                    
                            # detecta se apenas o mindinho ta levantado
                        if contador==1 and landmarks[20][1]>landmarks[18][1]:
                            print("mover para direita")
                                # me.move_right(30)
                            # Dedão e mindinho levantado
                        if contador==2 and landmarks[4][0] > landmarks[3][0] and landmarks[20][1]>landmarks[18][1]:
                            print("flip para tras")
                                # me.flip_back()
                            
                            # Apenas indicador levantado
                        if contador==1 and landmarks[8][1]>landmarks[6][1]:
                            print("subindo")
                                # me.move_up(10)
                                
                            # Desliga fazendo se fizer joia pra baixo
                        if landmarks[4][1]< landmarks[0][1] and landmarks[4][0]> landmarks[5][0]:
                             print("Desligando...",end="\n")
                                # print(f'Bateria: {battery}',end=" ")
                                # me.move_forward(10)
                                # me.land()
                             break
        cv2.imshow("Tello", img)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    me.streamoff()
    cv2.destroyAllWindows()
detectar_maos()    

    
    
        
  
           
            
            

    
    
      
        
 
        

            
            
    