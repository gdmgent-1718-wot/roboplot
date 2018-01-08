import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('../../driver/lib/key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://roboplot-1.firebaseio.com/'
})

records = db.reference('actief').get()
if records:
    array = records['waarden']
    for x in (0, len(array)):
        print (array[x].l + ' ' + array[x].r)
else:
    print('geen records in afspeellijst')