import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
#motor1
Motor1A = 23 # Set GPIO-23 as Input 1 of the controller IC
Motor1B = 24 # Set GPIO-24 as Input 2 of the Controller IC
Motor1E = 25 # Set GPIO-25 as Enable pin 1 of the controller IC

#motor2
Motor2A = 22 # Set GPIO-23 as Input 1 of the controller IC
Motor2B = 27 # Set GPIO-24 as Input 2 of the Controller IC
Motor2E = 17 # Set GPIO-25 as Enable pin 1 of the controller IC

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwmA=GPIO.PWM(25,100) #confuguring Enable pin means GPIO-04 for PWM
pwmB=GPIO.PWM(17,100) #confuguring Enable pin means GPIO-04 for PWM


pwmA.start(15) #Start it with 20% dutycycle
print "GO forward"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

pwmB.start(15) #Start it with 20% dutycycle
print "GO forward"
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(5)



pwmA.ChangeDutyCycle(15) # increase dutycycle 30% dutycycle
print "GO backward A"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

pwmB.ChangeDutyCycle(15) # increase dutycycle 30% dutycycle
print "GO backward B"
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(5)

pwmA.start(20) # increase dutycycle 50% dutycycle
print "GO forward A"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

pwmB.start(20) # increase dutycycle 50% dutycycle
print "GO forward B"
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(5)

pwmA.ChangeDutyCycle(25) # increase dutycycle 50% dutycycle
print "GO backward A"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

pwmB.ChangeDutyCycle(25) # increase dutycycle 50% dutycycle
print "GO backward B"
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(5)

print "NOW Stop A + B"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
pwmA.stop()
pwmB.stop() #stop PWM from GPIO output is necessary

GPIO.cleanup()