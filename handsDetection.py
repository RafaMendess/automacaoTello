import cv2
import mediapipe as mp

# codigo que testei inicialmente com mediapipe
# Funciona!
video= cv2.VideoCapture(0)

hands= mp.solutions.hands
Hands= hands.Hands(max_num_hands=1)
mpDraw= mp.solutions.drawing_utils


while video.isOpened():
    _,img=video.read()
    img= cv2.flip(img,1)
    frameRGB= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results= Hands.process(frameRGB)
    
    handPoints=results.multi_hand_landmarks
    height,width,_=img.shape
    pontos=[]
    
    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img,points,hands.HAND_CONNECTIONS)
            #pegando os numeros de cada ponto 
            for id,cord in enumerate(points.landmark):
                cx,cy=int(cord.x*width),int(cord.y*height)
                cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)
                
                pontos.append((cx,cy))
               
                
            dedos=[8,12,16,20] 
            contador= 0
            
            if pontos: 
                if pontos[4][0]>pontos[3][0]:
                        contador+=1
                for x in dedos:
                    if pontos[x][1]<pontos[x-2][1]:
                        contador+=1
            
            cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
            cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)
    cv2.imshow('Imagem',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


