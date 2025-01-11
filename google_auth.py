from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

authenticate()