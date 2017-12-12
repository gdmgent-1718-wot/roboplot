#!/usr/bin/env python

# Imports
#import math, time, explorerhat
import math, time
from lib import PS3

# PS3 Controller setup
ps3 = PS3.Controller()

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

	#if (left == 0):
	#	explorerhat.motor.one.stop()
	#elif (left > 0):
	#	explorerhat.motor.one.forward(left)
	#elif (left < 0):
	#	explorerhat.motor.one.backward(left * -1)

        #if (right == 0):
        #        explorerhat.motor.two.stop()
        #elif (right > 0):
        #        explorerhat.motor.two.forward(right)
        #elif (right < 0):
         #       explorerhat.motor.two.backward(right * -1)
