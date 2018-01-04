import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import time
import json
import names

#Huidige tijd
now = datetime.datetime.now()

#waarden voor weg te schrijven
datum = now.strftime("%d-%m-%Y %H:%M")
naam = names.get_first_name(gender='female')
actief = False
waarden = {
    0:"l:47,r:69",
    1:"l:47,r:69",
    2:"l:47,r:69",
    3:"l:47,r:69",
    4:"l:47,r:69",
    5:"l:47,r:69",
}

#credentials voor firebase
cred = credentials.Certificate('./lib/key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://roboplot-1.firebaseio.com/'
})

#referenties instellen zowel voor get als voor write
records = db.reference('data').get()
write = db.reference('data')

#assign
rec = {
    'datum': datum,
    'actief': actief,
    'naam': naam,
    'waarden': waarden    
}
try:
    #write
    #newrecord = write.push(rec)
    newrecord = write.push(rec)
    unique = newrecord.key
    print('Toegevoegd')
except Exception:
    print('Het record met de naam %s bestaat al.'%naam)
