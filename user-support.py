phonesafe = False
numlength = 0


def usersupportstart(phonesafe, numlength):
    
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

        print("Continued work")
    welcome(phonesafe, numlength)


usersupportstart(phonesafe, numlength)