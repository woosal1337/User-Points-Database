import pyrebase
from credentials.credentials import credentials
credentials = credentials()

firebase = pyrebase.initialize_app(credentials)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

# Upload file to the Firebase Storage
# Make sure rules are set right / true to upload the files/

def uploadFile():
    fileName = input("The name of the file you want to upload: ")
    cloudFileName = input("File name you would like to have on Cloud: ")

    try:
        storage.child(cloudFileName).put(fileName)
        print("{0} was successfully upload as {1}".format(fileName, cloudFileName))
        return True
    except:
        print("There was an issue while uploading {0} as {1}.".format(fileName, cloudFileName))
        return False



uploadFile()