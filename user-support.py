import time
import sys

phonesafe = False
numlength = 0
placenumber = 0
name = ""
phone = ""
busy = True
answered = False
ans = ""

def usersupportstart(phonesafe, numlength, name, phone, busy, answered, ans):
    
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

        
        return phone, name
  


    def supportconnection(name, phone, ans):
        print("Connecting you to user support...")
        f = open("support.txt", "w")
        time.sleep(2)
        ans = f"{name}, {phone}"
        f.write(ans)
        f.close()
        print("Ticket Made")
        busy = False

        return busy,ans



    def conversation_start(busy, answered, ans):
        while answered == False:
            f = open("support.txt", "r")
            if ans == f.readline().strip():
                busy = True
            else:
                busy = False
                answered = True


        while busy == False and answered == True:
            f = open("support.txt", "r")
            response = f.readline()
            if response == ans: 
                f.close()

            else:
                print(f"Staff says: {response}")
                f.close()
                f = open("support.txt", "w")
                ans = input("Your message: ")
                f.write(ans)
                f.close()

            

    phone, name = welcome(phonesafe, numlength)
    busy, ans = supportconnection(name, phone, ans)
    conversation_start(busy, answered, ans)
    sys.exit


usersupportstart(phonesafe, numlength, name, phone, busy, answered, ans)