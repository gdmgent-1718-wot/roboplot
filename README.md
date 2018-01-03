# RoboPlot
Pi Robotcar with Ps3-controller  | New Media Development | Graphic and Digital Media | Artevelde University College Ghent


In deze demo demonstreren wij het gebruik van een pi robotauto aangestuurd met een Playstation3-controller met eventuele uitbreidingen. 




Documentatie
-------------
**stap1**
Installatie van de Ps3-controller op de Pi via volgende commands in juiste volgorde:	
```
//alle packages updaten en packages installeren voor joystick en usb
sudo apt-get update
sudo apt-get -y install libusb-dev joystick python-pygame
//sixpair installeren
cd ~
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb
//pi opnieuw opstarten voor te zien of alles goed is geïnstalleerd
sudo reboot
//zien of je na dit command jouw bluetooth hardware-adres verkrijgt
sudo ~/sixpair
//connecteren via bluetooth indien ps3-controller een pin vraagt gewoon leeg laten (paar keer proberen tot het lukt)
//vervolgens testen of je ps3-controller is geconnecteerd
jstest /dev/input/js0
//dit levert een lijst met alle waarden voor elke knop indien je op een knop drukt veranderd de waarde in de console
```
**stap2**
Nu we alle actions hebben kunnen opvangen in de console moeten we alle handelingen kunnen afwerken binnen python, hiervoor gebruiken we de pygame library. (bestand ps3.py)
```
import pygame, sys
from time import sleep

# pygame init
pygame.init()

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

print "Aantal axes: " + str(axes)
print "Aantal knoppen: " + str(buttons)

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

while True:
    for event in pygame.event.get():
      # doorloop alle events met exit mogelijkheid
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
    sleep(0.2)
```
**stap3**
Aanschakelen van een led bij 'x' en uitschakelen bij 'o'.
Hiervoor gebruiken we de RPi library. (bestand led.py)
```
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
```

## Technische Tekening

![Robotplot Connections](https://github.com/gdmgent-1718-wot/roboplot/blob/master/docs/Roboplot_Schema.png)



 Gemaakt door   en **Lode Muylaert** en **Jef Roosens**