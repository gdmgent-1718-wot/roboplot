import pygame, sys
from time import sleep
import RPi.GPIO as GPIO



pygame.init()
joystick_count = pygame.joystick.get_count()

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

def getAxis(number):
    # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
    # so this is used not "if joystick value not zero"
    if joystick.get_axis(number) < -0.1 or joystick.get_axis(number) > 0.1:
      # led oplichten bij kruisje
        print "lala"       
        
def getButton(number):
    # returns 1 or 0 - pressed or not
    if joystick.get_button(number):
        if number == 13:
            GPIO.setmode(GPIO.BCM)
            LED = 21
            GPIO.setup(LED, GPIO.OUT)
            GPIO.output(LED,False)
            print "uit" 
        if number == 14:
            GPIO.setmode(GPIO.BCM)
            LED = 21
            GPIO.setup(LED, GPIO.OUT)
            GPIO.output(LED,True)
            print "aan"

while True:
    for event in pygame.event.get():
      # loop through events, if window shut down, quit program
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if axes != 0:
      for i in range(axes):
        getAxis(i)
    if buttons != 0:
      for i in range(buttons):
        getButton(i)
    if hats != 0:
      for i in range(hats):
        getHat(i)
    sleep(0.1)