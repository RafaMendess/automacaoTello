from djitellopy import Tello
import cv2 
import time

me= Tello()
me.connect()
me.streamon()

battery= me.get_battery()

me.takeoff()

time.sleep(10)
me.land()