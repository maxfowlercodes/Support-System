import time


f = open("staff-login.txt", "r")
file = open("staff-passwords.txt", "r")

def system():

    username = input("Enter staff username: ")
    password = input("Enter your account password: ")


    def login_system(username, password):
    

        if password.isdigit() == False:
            print("Only enter your pin number please. ")
            system()

        else:
            print("Checking detials... ")
            time.sleep(1)

        realuser = f.readline()
        realpass = file.readline()
        realuser = realuser.strip()

        if realuser == username and realpass == password:
            time.sleep(0.5)

        else:
            print("Invalid login detials.")

    def home_system(username):
        print(f"Welcome back {username}.")
        time.sleep(1)
        print(" 1 - Support tickets \n 2 - Refund Requests \n 3 - Settings")

    







    login_system(username, password)
    home_system(username)


system()
