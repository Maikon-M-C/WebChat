import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('./webchat.json')
firebase_admin.initialize_app(cred)

conn = firestore.client(database_id='usuarios')
