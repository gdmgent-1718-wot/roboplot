import pygame, sys
import RPi.GPIO as GPIO
from time import sleep

# pygame init
pygame.init()

# Set board control
GPIO.setmode(GPIO.BCM)

# aantal joysticks geconnecteerd
joystick_count = pygame.joystick.get_count()
print "Aantal controllers: " + str(joystick_count)

if joystick_count == 0:
    # sluiten als er geen connectie is
    print ("Er zijn geen joysticks gevonden")
    pygame.quit()
    sys.exit()
else:
    # init joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()


axes = joystick.get_numaxes()
buttons = joystick.get_numbuttons()
hats = joystick.get_numhats()
speed = 30

# Set buttons
buttonUp = 4
buttonDown = 6
buttonLeft = 7
buttonRight = 5
buttonCross = 14

# Set motors
#motor1
Motor1A = 23 # Set GPIO-23 as Input 1 of the controller IC
Motor1B = 24 # Set GPIO-24 as Input 2 of the Controller IC
Motor1E = 25 # Set GPIO-25 as Enable pin 1 of the controller IC

#motor2
Motor2A = 22 # Set GPIO-23 as Input 1 of the controller IC
Motor2B = 27 # Set GPIO-24 as Input 2 of the Controller IC
Motor2E = 17 # Set GPIO-25 as Enable pin 1 of the controller IC

# Initialize motors
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwmA=GPIO.PWM(25,100) #confuguring Enable pin means GPIO-04 for PWM
pwmB=GPIO.PWM(17,100) #confuguring Enable pin means GPIO-04 for PWM

# functions
 
def getAxis(number):
    # bij het bewegen joystick (axis)
    # bij het loslaten van joystick is de axis niet altijd 0
    if joystick.get_axis(number) < -0.1 or joystick.get_axis(number) > 0.1:
      # waarden tussen -1.0 en 1.0
      print "Waarde %s" %(joystick.get_axis(number))
      print "KnopI d: %s" %(number)
 

def getButton(number):
    # 1 indien ingedrukt 0 indien niet ingedrukt
    if joystick.get_button(number):
      # weergeven button id
      print "Button ID is %s" %(number)

def getHat(number):
    if joystick.get_hat(number) != (0,0):
      print "Hat value is %s, %s" %(joystick.get_hat(number)[0],joystick.get_hat(number)[1])
      print "Hat ID is %s" %(number)

def resetMotor():
    print "NOW Stop A + B"
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    pwmA.stop()
    pwmB.stop() #stop PWM from GPIO output is necessary

def setDirection(control):
    if joystick.get_button(control):
        if control == buttonUp:
            resetMotor()
            print "Go forward"
            pwmA.start(speed) #Start it with 20% dutycycle
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            GPIO.output(Motor1E,GPIO.HIGH)
            pwmB.start(speed) #Start it with 20% dutycycle
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            GPIO.output(Motor2E,GPIO.HIGH)
        elif control == buttonDown:
            resetMotor()
            print "GO backward"
            pwmA.ChangeDutyCycle(speed) # increase dutycycle 30% dutycycle
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            GPIO.output(Motor1E,GPIO.HIGH)
            pwmB.ChangeDutyCycle(speed) # increase dutycycle 30% dutycycle
            GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor2B,GPIO.HIGH)
            GPIO.output(Motor2E,GPIO.HIGH)
        elif control == buttonCross:
            resetMotor()
            GPIO.cleanup()
        else: 
            print "button without function!"
    else:
        print "no button pressed"


while True:
    for event in pygame.event.get():
      # doorloop alle events met exit mogelijkheid
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if buttons != 0:
      for i in range(buttons):
        setDirection(i)
    sleep(0.1)