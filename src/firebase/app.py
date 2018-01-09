#!/usr/bin/env python

# Imports
#import depencies
import math, time
import RPi.GPIO as GPIO
from lib import PS3 
import json
import io
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#load Firebase credentials
cred = credentials.Certificate('../../driver/lib/key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://roboplot-1.firebaseio.com/'
})
records = db.reference('actief').get()

active = True
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

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(lamp1, GPIO.OUT)

pwmA=GPIO.PWM(25,100) #confuguring Enable pin means GPIO-25 for PWM
pwmB=GPIO.PWM(17,100) #confuguring Enable pin means GPIO-17 for PWM


buttonCrossDelay = 0
buttonTriangleDelay = 0

#Print Controls to user
print("")
print("Joysticks:")
print("LEFT JOY UP/DOWN:    LEFT MOTOR FORWARD/BACKWARD")
print("RIGHT JOY UP/DOWN:   RIGHT MOTOR FORWARD/BACKWARD")
print("SELECT: TOGGLE LIGHT ON/OFF")
print("")
print("To Close, press 'Ctrl + C'")

def setMotor(l, r):
	leftMotor = float(l)
	rightMotor = float(r)
	if (leftMotor == 0):		
		pwmA.stop()
	elif (leftMotor > 0):
		pwmA.start(0)
		pwmA.ChangeDutyCycle(leftMotor)
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
	elif (leftMotor < 0):
		pwmA.start(0)
		pwmA.ChangeDutyCycle(leftMotor * -1)
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)

	if (rightMotor == 0):
		pwmB.stop()
	elif (rightMotor > 0):
		pwmB.start(0)
		pwmB.ChangeDutyCycle(rightMotor)
		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
	elif (rightMotor < 0):
		pwmB.start(0)
		pwmB.ChangeDutyCycle(rightMotor * -1)
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)

try:
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

		setMotor(left, right)
		# Debugging
		#print "[L: " + str(left) + ", R: " + str(right) + "]"

		if (ps3.a_square > 0):
			active = False
			GPIO.cleanup()

		buttonCrossDelay += 1

		if (buttonCrossDelay > 1500):
			if (ps3.a_cross > 0):
				buttonCrossDelay = 0
				GPIO.output(lamp1, not GPIO.input(lamp1))
		
		buttonTriangleDelay += 1
		if (buttonTriangleDelay > 1500):
			if (ps3.a_triangle > 0):
				records = db.reference('actief').get()
				if records:
					array = records['waarden']
					for coord in array:
						fbLeft = float(coord['l'][0:7])
						fbRight = float(coord['r'][0:7])
						setMotor(fbLeft, fbRight)
						time.sleep(1)
						print('links : ' + coord['l'][0:7] + '   rechts : ' + coord['r'][0:7] )
				else:
					print('geen records in afspeellijst')

				buttonTriangleDelay = 0

except KeyboardInterrupt:
  GPIO.cleanup()