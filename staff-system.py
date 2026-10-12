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
        options = input(" 1 - Support tickets \n 2 - Refund Requests \n 3 - Settings")

        if options == 1:

            print("Securing connection to user support... ")
            f = open("support.txt", "r")
            time.sleep(2)
            print(f.read())


        elif options == 2:
            print("2")
        elif options == 3:
            print("3")








    login_system(username, password)
    home_system(username)


system()
