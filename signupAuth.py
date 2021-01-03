import pyrebase
from credentials.credentials import credentials
credentials = credentials()

firebase = pyrebase.initialize_app(credentials)

auth = firebase.auth()

# Sign up Process
def userSignUp():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    passwordConf = input("Please re-enter your password to confirm it: ")


    if password == passwordConf:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Sign up was successfully made.")
            return True

        except:
            print("Account with that email already exists.")
            return False

userSignUp()