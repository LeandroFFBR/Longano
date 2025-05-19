import firebase_admin
from firebase_admin import credentials, firestore

def iniciar_firebase():

    if not firebase_admin._apps:
        cred = credentials.Certificate('cadastrolongano-firebase-adminsdk-fbsvc-1e1af318e1.json')
        firebase_admin.initialize_app(cred)
    return firestore.client()