numsafe = False

def usersupportstart(numsafe):
    
    def welcome(numsafe):
        name = input("Welcome to Lloyds support, could I please take your name? ")
        
        while numsafe == False:
            phone = input(f"Perfect thank you {name}, could I now please have your phone number? ")

            phone = phone.strip()
            phone = str(phone)
            
            if len(phone) == 10 or 11:
                print("Thank you for sharing your contact number")
                phone = True
            else:           
                print("That number does not look correct, please try again. ")
                phone = False

        print("Continued")
    welcome(numsafe)


usersupportstart(numsafe)