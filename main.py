import time
import Blackjack as blackjack
import TicTacToe as tic
import Hangman as hangman
import Poker as poker
import unoNew as uno

def startup():
    print("\n\nWelcome to Arcade")
    gameList()

def gameList():
    time.sleep(0.5)
    print("\nThis are the game we have.")
    print("+----+-----------------------------+")
    print("|    |           Arcade            |")
    print("+----+-----------------------------+")
    print("| 1  | BLACKJACK                   |")
    print("| 2  | HANGMAN                     |")
    print("| 3  | POKER                       |")
    print("| 4  | TIC TAC TOE                 |")
    print("| 5  | UNO                         |")
    print("+----+-----------------------------+")

    userInput = int(input("Enter the number of the game you want to play: "))
    if userInput == 1:
        blackjack.main()
    elif userInput == 2:
        hangman.main()
    elif userInput == 3:
        poker.main()
    elif userInput == 4:
        tic.main()
    elif userInput == 5:
        uno.main()
    else :
        print("Please choose the game from the above number.")
        gameList()

    print("\nYou have finish the game.")
    playAgain()

def playAgain():   
    print("Do you want to play again (y/Y for yes or n/N for no)")
    x = input("Enter your answer: ")
    if x.lower() == "y":
        startup()
    elif x.lower() == "n":
        print("Thank you for playing")
        exit()
    else:
        print("\nPlease enter only y for yes or n for no.")
        playAgain()


def main():
    startup()

main()
