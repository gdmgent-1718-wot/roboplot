#!/usr/bin/env python

# Imports
#import math, time, explorerhat
import math, time
import RPi.GPIO as GPIO
from lib import PS3

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
lamp1 =  29

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(lamp1, GPIO.OUT)

pwmA=GPIO.PWM(25,100) #confuguring Enable pin means GPIO-25 for PWM
pwmB=GPIO.PWM(17,100) #confuguring Enable pin means GPIO-17 for PWM

# Start update cycle
while True:
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

	if (ps3.cross):
		print "use cross"
		GPIO.output(lamp1, GPIO.IN)
		print "aan"
