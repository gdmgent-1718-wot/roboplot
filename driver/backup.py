#!/usr/bin/env python

# Imports
#import math, time, explorerhat
import math, time
import RPi.GPIO as GPIO
from lib import PS3 
import json
import io
import threading
active = True
#write to json
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
#interval for logging axis to json in seconds
interval = 0.5
# data
data = []
#create data
x = 1
# PS3 Controller setup
ps3 = PS3.Controller()

GPIO.setmode(GPIO.BCM)
#motor1
Motor1A = 23 # Set GPIO-23 as Input 1 of the controller IC
Motor1B = 24 # Set GPIO-24 as Input 2 of the Controller IC
Motor1E = 25 # Set GPIO-25 as Enable pin 1 of the controller IC

#motor2
Motor2A = 22 # Set GPIO-23 as Input 1 of the controller IC
Motor2B = 27 # Set GPIO-24 as Input 2 of the Controller IC
Motor2E = 17 # Set GPIO-25 as Enable pin 1 of the controller IC

#lampen
lamp1 =  5
klakson = 6

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(lamp1, GPIO.OUT)
GPIO.setup(klakson, GPIO.OUT)

pwmA=GPIO.PWM(25,100) #confuguring Enable pin means GPIO-25 for PWM
pwmB=GPIO.PWM(17,100) #confuguring Enable pin means GPIO-17 for PWM

buttonDelay = 0

# Start update cycle
while active:
	# Get PS3 update
	ps3.update()

	# Left joystick parsing of data
	left_joystick_y = ps3.a_joystick_left_y
	if (left_joystick_y != 0):
		left_joystick_y = left_joystick_y * -1
	if (left_joystick_y < 0):
		left_joystick_y = math.floor(left_joystick_y * 100) / 100
	elif (left_joystick_y > 0):
		left_joystick_y = math.ceil(left_joystick_y * 100) / 100
	left = ((left_joystick_y + 1) / 2) * 100
	if (left < 0):
                left = 0
	if (left == 50):
		left = 0
	else:
		left = left * 2 - 100
	
	# Right joystick parsing of data
        right_joystick_y = ps3.a_joystick_right_y
        if (right_joystick_y != 0):
                right_joystick_y = right_joystick_y * -1 
        if (right_joystick_y < 0):
                right_joystick_y = math.floor(right_joystick_y * 100) / 100
        elif (right_joystick_y > 0):
                right_joystick_y = math.ceil(right_joystick_y * 100) / 100
	right = ((right_joystick_y + 1) / 2) * 100
	if (right < 0):
		right = 0
        if (right == 50):
                right = 0
        else:
                right = right * 2 - 100

	# Debugging
	print "[L: " + str(left) + ", R: " + str(right) + "]"
	#item = {"l": str(left),"r": str(right)}
	#data.append(item)
	if (left == 0):		
		pwmA.stop()
	elif (left > 0):
		pwmA.start(0)
		pwmA.ChangeDutyCycle(left)
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
	elif (left < 0):
		pwmA.start(0)
		pwmA.ChangeDutyCycle(left * -1)
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
        if (right == 0):
                pwmB.stop()
        elif (right > 0):
		pwmB.start(0)
		pwmB.ChangeDutyCycle(right)
		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
        elif (right < 0):
		pwmB.start(0)
		pwmB.ChangeDutyCycle(right * -1)
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
	buttonDelay += 1
	print buttonDelay
	if (ps3.a_square > 0):
		active = False
	if (buttonDelay > 1500):
		if (ps3.a_cross > 0):
			buttonDelay = 0
			GPIO.output(lamp1, not GPIO.input(lamp1))
		if (ps3.a_triangle > 0):
			buttonDelay = 0
			pitch_s = raw_input(1500) 
			pitch = float(pitch_s)    #convert user input to a floating decimal
			print pitch
			duration_s = raw_input(4)  #ask the user to type in the duration
			duration = float(duration_s)  #convert user input to a floating decimal
			buzz(pitch, duration)  #feed the pitch and duration to the function, "buzz"
#with io.open('data.json', 'w', encoding='utf8') as outfile:
#    str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ': '), ensure_ascii=False)
#    outfile.write(to_unicode(str_))