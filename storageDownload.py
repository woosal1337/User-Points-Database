import pyrebase
from credentials.credentials import credentials
credentials = credentials()

firebase = pyrebase.initialize_app(credentials)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

# Download file from the Firebase Storage
# Make sure rules are set right / true to upload the files/

def downloadFile():
    cloudFileName = input("File name you have on Cloud: ")

    try:
        storage.child(cloudFileName).download("downloads/", "downloads/downloadedfile.png")
        print("{0} was successfully downloaded".format(cloudFileName))
        return True
    except:
        print("There was an issue while downloading {0}.".format(cloudFileName))
        return False

downloadFile()