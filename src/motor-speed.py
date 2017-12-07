import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 23 # Set GPIO-23 as Input 1 of the controller IC
Motor1B = 24 # Set GPIO-24 as Input 2 of the Controller IC
Motor1E = 24 # Set GPIO-25 as Enable pin 1 of the controller IC

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
pwm=GPIO.PWM(24,100) #confuguring Enable pin means GPIO-04 for PWM

pwm.start(20) #Start it with 20% dutycycle
print "GO forward"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
sleep(2)

pwm.ChangeDutyCycle(30) # increase dutycycle 30% dutycycle
print "GO backward"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
sleep(2)

pwm.start(50) # increase dutycycle 50% dutycycle
print "GO forward"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
sleep(2)

pwm.ChangeDutyCycle(80) # increase dutycycle 50% dutycycle
print "GO backward"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
sleep(2)

print "NOW Stop"
GPIO.output(Motor1E,GPIO.LOW)
pwm.stop() #stop PWM from GPIO output is necessary

GPIO.cleanup()