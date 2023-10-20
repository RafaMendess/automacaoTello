from cvzone.HandTrackingModule import HandDetector
import cv2
from djitellopy import Tello
from time import sleep


# Codigo de reconhecimento de gestos (utilizar esse para apresentar)

def detectarMaos(video):
    # variavéis para definir qual ação foi executada anteriormente 
    estados={"esquerda":1,"direita":2,"flip":3,"subir":4,"desligar":5,"foto":6}
    estadoAtual=0
    
    detector= HandDetector(maxHands=1,detectionCon=0.5,modelComplexity=1)

    while video.isOpened():
        
        img=cv2.flip(video.read()[1],1)
        
        
        hand_detected,_= detector.findHands(img,draw=True,flipType=False)
        
        if hand_detected:
            # Primeira mão a ser detectada
            hand = hand_detected[0]
            landmarks = hand["lmList"]
                    # detecta apenas a mão direita 
            if hand["type"] == "Right":
                dedos = [8, 12, 16, 20]
                contador = 0
                
                if landmarks: 
                        # Contador de dedos da mão 
                        for x in dedos:
                            if landmarks[x][1] < landmarks[x-2][1]:
                                contador += 1

                             #  Detecta se apenas o dedão ta levantado
                        if landmarks[4][0] <landmarks[3][0] :
                            contador += 1
                            if contador==1 and estadoAtual!=estados["esquerda"]:
                                print("mover a esquerda")
                                estadoAtual=estados["esquerda"]
                                    # me.move_left(30)
                            # detecta se apenas o mindinho ta levantado
                        elif contador==1 and landmarks[20][1]<landmarks[18][1] and estadoAtual!=estados["direita"]:
                            print("mover para direita")
                            estadoAtual=estados["direita"]
                                # me.move_right(30)
                            # Dedão e mindinho levantado
                        if contador==2 and landmarks[4][0] < landmarks[3][0] and landmarks[20][1]<landmarks[18][1] and estadoAtual!=estados["flip"]:
                            print("flip para tras")
                            estadoAtual=estados["flip"]
                                # me.flip_back()
                            
                            # Apenas indicador levantado
                        elif contador==1 and landmarks[8][1]<landmarks[6][1] and estadoAtual!=estados["subir"]:
                            print("subindo")
                            estadoAtual=estados["subir"]
                                # me.move_up(10)
                                
                            # Desliga fazendo se fizer joia pra baixo
                        elif contador==5 and estadoAtual!=0:
                            print("detectando...")
                            estadoAtual=0
                        if contador==3 and landmarks[4][0]> landmarks[3][0] and landmarks[20][1]>landmarks[18][1] and estadoAtual!=estados["desligar"]:
                             print("Desligando...")
                             estadoAtual=estados["desligar"]
                                # print(f'Bateria: {battery}',end=" ")
                                # me.move_forward(10)
                                # me.land()
                            #  break
                        if contador==2 and landmarks[8][1]<landmarks[6][1] and landmarks[12][1]<landmarks[10][1] and estadoAtual!=estados["foto"]:
                                print("Foto")
                                estadoAtual= estados["foto"]
                        
                        
                cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
                cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)
        cv2.imshow("Tello", img)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    

    cv2.destroyAllWindows()
# detectarMaos(cv2.VideoCapture(0))  

def detectarMaos_tello():
    me= Tello()
    me.connect()    
    me.streamon()
    # variavéis para definir qual ação foi executada anteriormente 
    estados={"esquerda":1,"direita":2,"flip":3,"subir":4,"desligar":5,"foto":6}
    estadoAtual=0
    
    
    
    detector= HandDetector(maxHands=1,detectionCon=0.5,modelComplexity=1)
    
    while True:
        
        img= me.get_frame_read().frame
        
        hand_detected,_= detector.findHands(img,draw=True,flipType=False)
        img=cv2.flip(img,1)
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        if estadoAtual==estados["foto"]:
            heights,width,_=img.shape
            new_h=int(heights)
            new_w= int(width)
            photo= cv2.resize(img,(new_h,new_w))
    
            cv2.imwrite("fotos.jpg",photo)
        if hand_detected:
        # Primeira mão a ser detectada
            hand = hand_detected[0]
            landmarks = hand["lmList"]
                    # detecta apenas a mão direita 
            if hand["type"] == "Right":
                dedos = [8, 12, 16, 20]
                contador = 0
                
                if landmarks: 
                        # Contador de dedos da mão 
                        for x in dedos:
                            if landmarks[x][1] < landmarks[x-2][1]:
                                contador += 1

                            #  Detecta se apenas o dedão ta levantado
                        if landmarks[4][0] <landmarks[3][0] :
                            contador += 1
                            if contador==1 and estadoAtual!=estados["esquerda"]:
                                print("mover a esquerda")
                                estadoAtual=estados["esquerda"]
                                    # me.move_left(30)
                            # detecta se apenas o mindinho ta levantado
                        elif contador==1 and landmarks[20][1]<landmarks[18][1] and estadoAtual!=estados["direita"]:
                            print("mover para direita")
                            estadoAtual=estados["direita"]
                                # me.move_right(30)
                            # Dedão e mindinho levantado
                        if contador==2 and landmarks[4][0] < landmarks[3][0] and landmarks[20][1]<landmarks[18][1] and estadoAtual!=estados["flip"]:
                            print("flip para tras")
                            estadoAtual=estados["flip"]
                                # me.flip_back()
                            
                            # Apenas indicador levantado
                        elif contador==1 and landmarks[8][1]<landmarks[6][1] and estadoAtual!=estados["subir"]:
                            print("subindo")
                            estadoAtual=estados["subir"]
                                # me.move_up(10)
                                
                            # Desliga fazendo se fizer joia pra baixo
                        elif contador==5 and estadoAtual!=0:
                            print("detectando...")
                            estadoAtual=0
                        if contador==3 and landmarks[4][0]> landmarks[3][0] and landmarks[20][1]>landmarks[18][1] and estadoAtual!=estados["desligar"]:
                            print("Desligando...")
                            estadoAtual=estados["desligar"]
                                # print(f'Bateria: {battery}',end=" ")
                                # me.move_forward(10)
                                # me.land()
                            #  break
                        if contador==2 and landmarks[8][1]<landmarks[6][1] and landmarks[12][1]<landmarks[10][1] and estadoAtual!=estados["foto"]:
                            print("Foto")
                            estadoAtual= estados["foto"]
                        
                        
                cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
                cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)
        cv2.imshow("Tello",imgRGB)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    



    me.streamoff()
    cv2.destroyAllWindows()

detectarMaos_tello()
        
    
    
    