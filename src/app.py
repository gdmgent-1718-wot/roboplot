#!/usr/bin/env python

# Imports
#import depencies
import math, time
import datetime
import RPi.GPIO as GPIO
from lib import PS3 
import json
import io
import names
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#Huidige tijd
now = datetime.datetime.now()

#global variablen
counter = 0
toggle = False
data = []
active = True
buttonTriangleDelay = 0

#waarden voor weg te schrijven
datum = now.strftime("%d-%m-%Y %H:%M")
naam = names.get_first_name(gender='female')
actief = False

#load Firebase credentials
cred = credentials.Certificate('./lib/key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://roboplot-1.firebaseio.com/'
})

#referenties ophalen voor get
records_active = db.reference('actief').get()

#referenties instellen zowel voor get als voor write
records = db.reference('data').get()
write = db.reference('data')


#GPIO mode selecteren
GPIO.setmode(GPIO.BCM)
#motor1
Motor1A = 23 # Set GPIO-23 as Input 1 of the controller IC
Motor1B = 24 # Set GPIO-24 as Input 2 of the Controller IC
Motor1E = 25 # Set GPIO-25 as Enable pin 1 of the controller IC

#motor2
Motor2A = 22 # Set GPIO-23 as Input 1 of the controller IC
Motor2B = 27 # Set GPIO-24 as Input 2 of the Controller IC
Motor2E = 17 # Set GPIO-25 as Enable pin 1 of the controller IC

#motoren
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwmA=GPIO.PWM(25,100) #confuguring Enable pin means GPIO-25 for PWM
pwmB=GPIO.PWM(17,100) #confuguring Enable pin means GPIO-17 for PWM

#lampen
lamp1 =  5
GPIO.setup(lamp1, GPIO.OUT)

#buzzer
buzzerP = 2
buzzerE = 3
GPIO.setup(buzzerP, GPIO.OUT)
GPIO.setup(buzzerE, GPIO.OUT)
GPIO.output(buzzerP, GPIO.HIGH)

#assign
rec = {
		'datum': datum,
		'actief': actief,
		'naam': naam,
		'waarden': []
}

#for x in range(0, 4):
#	GPIO.output(lamp1, GPIO.HIGH)
#	GPIO.output(buzzerE, GPIO.HIGH)
#	time.sleep(0.1)
#	GPIO.output(lamp1, GPIO.LOW)
#	GPIO.output(buzzerE, GPIO.LOW)
#	time.sleep(0.1)

#time.sleep(10)
# PS3 Controller setup
ps3 = PS3.Controller()

#Print Controls to user
print("")
print("Controls:")
print("LEFT JOY UP/DOWN:    LEFT MOTOR FORWARD/BACKWARD")
print("RIGHT JOY UP/DOWN:   RIGHT MOTOR FORWARD/BACKWARD")
print("")
print("R1:    START RECORDING PATH")
print("R2:    STOP RECORDING PATH")
print("")
print("TRIANGLE:    EXECUTE ACTIVE PATH FROM APP")
print("CROSS:    TOGGLE LIGHT ON/OFF")
print("")
print("")
print("To Close, press 'Ctrl + C' of push SQUARE")

GPIO.output(lamp1, GPIO.HIGH)
GPIO.output(buzzerE, GPIO.HIGH)
time.sleep(1)
GPIO.output(lamp1, GPIO.LOW)
GPIO.output(buzzerE, GPIO.LOW)


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

		buttonTriangleDelay += 1
		if (buttonTriangleDelay > 1500):
			if (ps3.a_triangle > 0):
				records_active = db.reference('actief').get()
				if records_active:
					array = records_active['waarden']
					for coord in array:
						fbLeft = float(coord['l'][0:7])
						fbRight = float(coord['r'][0:7])
						setMotor(fbLeft, fbRight)
						time.sleep(0.0178)
				else:
					for x in range(0, 3):
						GPIO.output(lamp1, GPIO.HIGH)
						GPIO.output(buzzerE, GPIO.HIGH)
						time.sleep(0.1)
						GPIO.output(lamp1, GPIO.LOW)
						GPIO.output(buzzerE, GPIO.LOW)
						time.sleep(0.1)

				buttonTriangleDelay = 0

		#logs to array
		if toggle==True:
			if counter%5 == 0:
				item = {"l": str(left),"r": str(right)}
				data.append(item)

		#start met recorden
		if (ps3.r1):
			toggle = True
			GPIO.output(lamp1, GPIO.HIGH)
			#print('Start opname')
		#Stop met recorden
		if (ps3.r2):
			if toggle==True:
				if data:
					#write
					GPIO.output(lamp1, GPIO.LOW)
					rec['waarden'] = data
					newrecord = write.push(rec)
					data = []
					rec['naam'] = names.get_first_name(gender='female')
			toggle = False
			#print('Stop opname')
		counter += 1

except KeyboardInterrupt:
	GPIO.output(lamp1, GPIO.HIGH)
	GPIO.output(buzzerE, GPIO.HIGH)
	time.sleep(2)
	GPIO.cleanup()