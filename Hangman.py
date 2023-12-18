import random 
import time

def startup():
    print("\n----H A N G M A N----")
    #Welcoming the user
    UserName = input("Enter your name: ")
    print("Hello,", UserName, "Welcome to HANGMAN.\n")
    #sleep for 0.5 seconds
    time.sleep(0.5)

#selection for animals
def animals():
    words = ["bee", "giraffe", "leopard", "monkey", "zebra"]
    usedWord = random.choice(words)

    #describe for the guess words
    if usedWord == "bee":
        print("This animal collect honey.")
    elif usedWord == "giraffe":
        print("This animal have a long neck.")
    elif usedWord == "leopard":
        print("Body of this animal spots placed into rosettes.")
    elif usedWord == "monkey":
        print("This animal live in a tree and they like to eat banana.")
    elif usedWord == "zebra":
        print("Body of this animal is with black and white strips.")

    guesses = ''
    turns = 6

    while turns > 0:
        failed = 0
        for char in usedWord:
            if char in guesses:
                print(char,end="")
            else:
                print("_",end="")
                failed += 1

        if failed == 0:
            print("\nYou are won!")
            break

        guess = input("Guess a letter: ")
        guesses += guess

        if guess not in usedWord:
            turns -= 1

            print("You are wrong")
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You have lost the game")

#selection for fruits
def fruits():
    words = ["apple", "banana", "cherry", "durian", "grape", "orange"]
    usedWord = random.choice(words)

    if usedWord == "apple":
        print("It is a rounded fruit with red or green skin, firm white flesh and a seedy core.")
    elif usedWord == "banana":
        print("This fruit with a yellow skin.")
    elif usedWord == "cherry":
        print("This fruit are deep red and exquisitely sweet, with small inedible pits.")
    elif usedWord == "durian":
        print("This fruit have a pricky shell and its flesh are yellow.")
    elif usedWord == "grape":
        print("It is a smooth-skined juicy light green or deep red to purplish black berry eaten dried or fresh as a fruit or fermented to produce wine.")
    elif usedWord == "orange":
        print("It is a citrus fruits with fragrant, leathery skin, and juicy flesh.")

    guesses = ''
    turns = 6

    while turns > 0:
        failed = 0
        for char in usedWord:
            if char in guesses:
                print(char,end="")
            else:
                print("_",end="")
                failed += 1

        if failed == 0:
            print("\nYou are won!")
            break

        guess = input("Guess a letter: ")
        guesses += guess

        if guess not in usedWord:
            turns -= 1

            print("You are wrong")
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You have lost the game")


def main():
    startup()
    print("You can choose to guess animals or fruits.")
    userInput = input("Enter your answer: ")

    if userInput == "animals":
        animals()
    elif userInput == "fruits":
        fruits()
