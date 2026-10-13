import time
import sys

phonesafe = False
numlength = 0
placenumber = 0
name = ""
phone = ""


def usersupportstart(phonesafe, numlength, name, phone):
    
    def welcome(phonesafe, numlength):

        name = input("Welcome to Lloyds support, could I please take your name? ")
        
        while phonesafe == False:
            phone = input(f"Perfect thank you {name}, could I now please have your phone number? ")
            numlength = len(phone)

            
            if numlength == 10 or numlength == 11:
                print("Thank you for sharing your contact number")
                phonesafe = True
                
            else:
                print("Please make sure your phone number is 10-11 digits EG. (07863953173)")

        print("Trying to return")
        if phone and name != "":
            print("Both variables have values")
        
        return phone, name
  


    def supportconnection(name, phone):
        print("Connecting you to user support...")
        f = open("support.txt", "w")
        time.sleep(2)
        infomation = f"{name}, {phone}"
        f.write(infomation)
        f.close()
        print("Ticket Made")

    phone, name = welcome(phonesafe, numlength)
    supportconnection(name, phone)
    sys.exit


usersupportstart(phonesafe, numlength, name, phone)