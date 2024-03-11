import random

random_number=random.randint(1,10)

while True:
    guess=int(input("Guess a number between 1 and 10: "))
    if guess<random_number:
        print("Too Low!, try again")
    elif guess>random_number:
        print("too high!, try again")
    else:
        print("you guessed it! You won!")
        again=input("Do you want to keep playing? (y/n)")
        if again=="y":
            random_number=random.randint(1,10)
            guess=None
        else:
            print("Thank you for playing")
            break


   