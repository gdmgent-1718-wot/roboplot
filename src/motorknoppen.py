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
    if buttons != 0:
      for i in range(buttons):
        getButton(i)
    sleep(0.1)