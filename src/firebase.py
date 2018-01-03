#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
from firebase import firebase
cred = credentials.Certificate("wheeloffortune2-c0e4a-firebase-adminsdk-xx83k-8a28c73b1e.json")
firebase_admin.initialize_app({'databaseURL':'https://roboplot-1.firebaseio.com/'})
records = db.reference()
print(records)