import pyrebase
from credentials.credentials import credentials
credentials = credentials()

firebase = pyrebase.initialize_app(credentials)

auth = firebase.auth()

# Auth Process
def userAuth():
    email = input("Please, enter your email: ")
    password = input("Please, enter your password: ")

    try:
        auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in.")
        return True
    except:
        print("Invalid login or password.")
        return False

userAuth()