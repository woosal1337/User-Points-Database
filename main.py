import pyrebase
from credentials.credentials import credentials
credentials = credentials()

firebase = pyrebase.initialize_app(credentials)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

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

# Sign up Process
def userSignUp():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    passwordConf = input("Please re-enter your password to confirm it: ")

    try:
        if password == passwordConf:
            auth.create_user_with_email_and_password(email, password)
            print("Sign up was successfully made.")
            return True
    except:
        print("Make sure that mail does not exist, or your password is right.")
        return False