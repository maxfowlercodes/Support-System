

f = open("staff-login.txt", "r")
file = open("staff-passwords", "r")




def login_system():
    
    username = input("Enter staff username: ")
    password = input("Enter your account password: ")

    if password.isdigit() == False:
        print("Only enter your pin number please. ")

    else:
        print("Checking detials... ")

    realuser = file.readline()
    realpass = f.readline()
    realuser = realuser.strip()

    if realuser == username and realpass == password:
        print(f"Logged in as {realuser}")

    else:
        print("Invalid login detials.")
