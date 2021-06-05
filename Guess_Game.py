#Python
#Guessing a random number game
import random
class guessgame():
    def __init__(self):
        self.choice=random.randint(0,10)
    def reset_random(self):
        print("Resetting random number")
        self.coice=random.choice_int(0,10)

    def guess(self):
        Guessnow=int(input("Enter any number between 0 to 10:"))
        if Guessnow==self.choice:
            print("The guess is correct")
        else:
            if Guessnow<self.choice:
                print("Wrong Guess higher number!!!")
            else:
                print("Wrong Guess lower number!!!")
myobj=guessgame()
myobj.guess()
