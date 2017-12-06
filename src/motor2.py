import cv2
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1 = 16
Motor2 = 18 
Motor3 = 22
 
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
 
ck=1
while ck==1:
    vis=cv2.imread("pic5.png")
    cv2.imshow('image', vis)
    ch = 0xFF &amp; cv2.waitKey(1)
 
    if ch == ord('1'):                 # Press the key '1'
        print("FORWARD MOTION")
        GPIO.output(Motor1,GPIO.HIGH)
        GPIO.output(Motor2,GPIO.LOW)
        GPIO.output(Motor3,GPIO.HIGH)
 
    if ch == ord('2'):                 # Press the key '2'
        print("BACKWARD MOTION")
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.HIGH)
        GPIO.output(Motor3,GPIO.HIGH)
 
    if ch == ord('3'):                  # Press the key '3'
        print("STOP")
        GPIO.output(Motor3,GPIO.LOW)
 
    if ch == ord('4'):                  # Press the key '4'
        print("FINISHED")
        ck=4
        GPIO.cleanup()