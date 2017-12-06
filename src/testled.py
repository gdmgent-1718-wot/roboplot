import RPi.GPIO as GPIO        #This line alone caused 90 minutes of frustration

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT) #set pin 21 to output
p = GPIO.PWM(40,400)        #set the PWM on pin 21 to 50%
p.start(0) #I don’t remember what this does but trust me, you need it.
try:
    while True:
        for i in range (100):
            p.ChangeDutyCycle(i)            
            time.sleep(0.02)        #These last three lines are going to loop and increase the power from 1% to 100% gradually   aankrijgen
        for i in range(100):            
            p.ChangeDutyCycle(100-i)
            time.sleep(0.02)         #These three lines loop and decrease the power from 100%-1% gradually    uitkrijgen
except KeyboardInterrupt:
    pass                   #This is supposed to stop the program if a key is hit, but it doesn’t work for us.  Only ctrl^c works

p.stop()

GPIO.cleanup()

