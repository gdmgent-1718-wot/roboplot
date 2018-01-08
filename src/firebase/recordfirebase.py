import math, time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import atexit
import time
import json
import names
from lib import PS3

record = True
counter = 0
toggle = False

# PS3 Controller setup
ps3 = PS3.Controller()
#Huidige tijd
now = datetime.datetime.now()
#waarden voor weg te schrijven
datum = now.strftime("%d-%m-%Y %H:%M")
naam = names.get_first_name(gender='female')
actief = False
#credentials voor firebase
cred = credentials.Certificate('../../driver/lib/key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://roboplot-1.firebaseio.com/'
})
#array for logging
data = []

#referenties instellen zowel voor get als voor write
records = db.reference('data').get()
write = db.reference('data')

#assign
rec = {
    'datum': datum,
    'actief': actief,
    'naam': naam,
    'waarden': []
}

def exit():
    try:
        if data:
            #write
            rec['waarden'] = data
            newrecord = write.push(rec)
    except Exception:
        print('Het record met de naam %s bestaat al.'%naam)
    print('afgesloten')
# Start update cycle
while record:
   # Get PS3 update
    ps3.update()
    # Left joystick parsing of data
    left_joystick_y = ps3.a_joystick_left_y
    if (left_joystick_y != 0):
        left_joystick_y = left_joystick_y * -1
    if (left_joystick_y < 0):
        left_joystick_y = (math.floor(left_joystick_y * 100)/ 100
    elif (lef_joystick_y > 0):
        left_joystick_y = (math.ceil(left_joystick_y * 100) / 100

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
    #print "[L: " + str(left) + ", R: " + str(right) + ", C" + str(counter) + "]"
    #logs to array
    if toggle==True:
        if counter%50 == 0:
            item = {"l": str(left),"r": str(right)}
            data.append(item)
    #stoppen met programma
    if (ps3.square):
        record = False
    #start met recorden
    if (ps3.r1):
        toggle = True
        print('Start opname')
    #Stop met recorden
    if (ps3.r2):
        toggle = False
        print('Stop opname')
    counter += 1
atexit.register(exit)

