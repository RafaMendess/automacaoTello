import cv2 as open

video = open.VideoCapture(0)

while video.isOpened():
    
    red,frame=video.read()
    frame= open.resize(frame, (540, 380), fx = 0, fy = 0,
                         interpolation = open.INTER_CUBIC)
    
    gaussianblur = open.GaussianBlur(frame, (5, 5), 0)
    
    open.imshow("Camera",gaussianblur)


    if open.waitKey(1) & 0xFF==ord("1"):
        break
    

video.release()

open.destroyAllWindows()
        

