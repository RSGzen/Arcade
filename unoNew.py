import time # imported to use time.sleep() for better card drawing experience
import random # imported to use to draw and shuffle card decks randomly
from colorama import Fore, Style # imported to use to display colours of cards in the terminal

VALUE_DICT = { # Constant dictionary used to represent the name of cards from value 10-14
    10: "Skip",
    11: "Reverse",
    12: "Draw 2",
    13: "Wild Card",
    14: "Draw 4"
}

COLOURS = ["Red","Yellow","Green","Blue"] # Constant list that represent all the colours of cards

class Card:

    def __init__(self,colourC,valueC): # Initialization of individual card with colour and value
        self.colourC = colourC
        self.valueC = valueC
    
    def showValueColour(self): # Method used to display cards of their corresponding colour and value
        if self.valueC in VALUE_DICT:
            if self.colourC == "Red":
                print(Fore.RED + f"{VALUE_DICT[self.valueC]}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Yellow":
                print(Fore.YELLOW + f"{VALUE_DICT[self.valueC]}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Blue":
                print(Fore.BLUE + f"{VALUE_DICT[self.valueC]}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Green":
                print(Fore.GREEN + f"{VALUE_DICT[self.valueC]}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Empty": # Empty color corresponds to Wild Cards and Draw 4 Cards which can be used with any colour
                print(f"{VALUE_DICT[self.valueC]}",end="")
        else:
            if self.colourC == "Red":
                print(Fore.RED + f"{self.valueC}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Yellow":
                print(Fore.YELLOW + f"{self.valueC}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Green":
                print(Fore.GREEN + f"{self.valueC}",end="")
                print(Style.RESET_ALL, end="")
            if self.colourC == "Blue":
                print(Fore.BLUE + f"{self.valueC}",end="")
                print(Style.RESET_ALL, end="")
        
    def showColour(self): # Method to specifically display colour of the card
        if self.colourC == "Red":
            print(Fore.RED + "Red")
            print(Style.RESET_ALL, end="")
        if self.colourC == "Yellow":
            print(Fore.YELLOW + "Yellow")
            print(Style.RESET_ALL, end="")
        if self.colourC == "Blue":
            print(Fore.BLUE + "Blue")
            print(Style.RESET_ALL, end="")
        if self.colourC == "Green":
            print(Fore.GREEN + "Green")
            print(Style.RESET_ALL, end="")
        if self.colourC == "Empty" and self.valueC == 13:
            print(Fore.RED + "Red",end=" ")
            print(Style.RESET_ALL + ", ", end="")
            print(Fore.YELLOW + "Yellow",end=" ")
            print(Style.RESET_ALL + ", ", end="")
            print(Fore.GREEN + "Green",end=" ")
            print(Style.RESET_ALL + "or ", end="")
            print(Fore.BLUE + "Blue",end="")
            print(Style.RESET_ALL,end="")
            print("")
        if self.valueC == 14:
            pass

    def showValue(self): # Method to specifically display value of the card
        if self.valueC == 13:
            print("Wild Card")
        elif self.valueC == 14:
            print("Draw 4")
        else:
            if self.valueC in VALUE_DICT:
                print(VALUE_DICT[self.valueC])
            else:
                print(self.valueC)

def createDeck(deck): # Create new card deck with 108 cards 

    for i in range(1,13): 
        for colour in COLOURS:
            tempCard = Card(colour, i)
            deck.append(tempCard)
            deck.append(tempCard)
    
    weirdCardValue = [13,14]

    for value in weirdCardValue:
        tempCard = Card("Empty",value)
        for _ in range(0,4):
            deck.append(tempCard)

    for colour in COLOURS:
        tempCard = Card(colour,0)
        deck.append(tempCard)
    
    return deck

def borderline(): # Used to separate different scenarios in game
    print("=====================================================")

def welcomeMessage(): #As suggested, is a welcome text for the user
    borderline()
    print("\tWelcome to UNO.\t")
    time.sleep(0.8)
    print("\nI am the host for today.\n")
    time.sleep(0.8)
    print("You may call me ",end="")
    time.sleep(0.4)
    print("JARViS.")
    borderline()

def userSetName(): # Set a name for the user be addressed as
    borderline()
    print("\nHow would you like to address yourself?")
    time.sleep(0.8)
    tempName = input(": ")
    borderline()

    return tempName

def menuChoice(username): # Let user to choose whether they want to view rules, view leaderboard or start uno game
    choiceStatus = False
    while (choiceStatus == False):
        borderline()
        print(f"Hi {username}. \n")
        print("Do you want to.........\n")
        print("1. Start Game\n2. Read Rules\n3. View Leaderboard\n4. Exit")
        print("--------------------------------------------")
        choice = input("Choice: ")
        if choice.isdigit():
            choice = int(choice)
            
            if choice >= 1 and choice <= 4:
                choiceStatus = True
        
            else:
                borderline()
                print("\nYou can only enter numbers from 1-4.\nPlease try again.\n")
                borderline()
        
        else:
            borderline()
            print("\nYou can only enter positive integers.\nPlease try again.\n")
            borderline()
    
    borderline()
    return choice

def rulesOfUno(): # Prints out the rules of Uno which may help smoother gameplay 
    # https://en.wikipedia.org/wiki/Uno_(card_game) 
    borderline()
    print(Fore.CYAN + "\n\tRULES OF UNO: \n")
    print("1. The deck has 108 cards")
    print("2. There are 4 colours of cards ranging from 1-9, Skip, Reverse and Draw 2 of 2 copies")
    print("3. There are 5 kinds of special cards which are Skip, Reverse, Wild Card, Draw 2 and Draw 4\n")
    print("4. Skip - When played, this forces the next player to be skipped without needing to place a card")
    print("5. Reverse - When played, the playing order will be reversed")
    print("6. Wild Card - Can be used as a colour of any colour")
    print("7. Draw 2 - Force the next player to draw 2 cards")
    print("8. Draw 4 - Force the next player to draw 4 cards\n")
    print("9. Special cards such as Draw 2 and Draw 4 can be stacked upon each other")
    print("10. Draw 2 and 4 stacks will be executed when the current player doesn't stack it higher up")
    print("11. There are also four colours of cards of 0, Draw 4 and Wild Card each one copy")
    print("12. The four colour of the cards are: ", end="")
    print(Fore.RED + "Red", end=", ")
    print(Fore.YELLOW + "Yellow", end=", ")
    print(Fore.GREEN + "Green", end=", ")
    print(Fore.BLUE + "Blue")
    print(Fore.CYAN + "13. Wild cards or Draw 4 cards can be used as any colours\n")

    print(Fore.CYAN + "\tHOW TO PLAY UNO: \n")
    print("1. Each player is assigned 7 cards at the start")
    print("2. One card will be drawn from the deck as start")
    print("3. Each round, players must place a card unless being skipped by previous player")
    print("4. Cards placed must either have the same number(including special cards) or colour of the previous card placed")
    print("5. If the player doesn't have a card to place, they have to draw from the deck until they have a suitable card")
    print("6. The first player to placed all their cards out will be the winner ")
    print("7. Each winner of the round will gain 1 point in the leaderboard")
    print("8. The player with the most numbers of points during exit will be the ultimate winner.\n")
    print(Style.RESET_ALL,end="")
    borderline()

def showLeaderboard(leaderBoard): # Show how many times the user or the three bots won in previous games
    borderline()
    print(Fore.LIGHTCYAN_EX + "\nLeaderboard of Fame\n")
    print(Style.RESET_ALL,end="")
    for i in range(0,4):
        print(f"{leaderBoard[0][i]} won : ",end="")
        print(Fore.RED + f"{leaderBoard[1][i]} ", end="")
        print(Style.RESET_ALL, end="")
        print("points")
    print("")
    borderline()

def checkWinner(leaderBoard): #Check who is the winner before user quits the program 
    numWins = 0
    maxWin = max(leaderBoard[1])
    equalWin = -1

    winnersList = []

    for i in range(0,3):
        if leaderBoard[1][i] > 0:
            numWins += 1
        if maxWin == leaderBoard[1][i]:
            equalWin += 1
            winnersList.append(i)

    if numWins > 0:
        if equalWin > 1:
            print("\nThere is a tie among: ",end="")
            for win in winnersList:
                print(leaderBoard[0][win])
            print(f"\nwith a score of {maxWin}\n!!")
        else:
            print(f"\nThe winner is {leaderBoard[0][winnersList[0]]} with ")
            print(Fore.RED + f"{maxWin} points! \n")
            print(Style.RESET_ALL, end="")

    else:
        print("\nThank you for your visit!!!\n")

def giveStartCards(cardDeck,handCardDeck): # Give out 7 cards to each player in the game (user + 3 bots)
    for i in range(0,28):
        tempCard = cardDeck[i]

        if i%4 == 0:
            handCardDeck[0].append(tempCard)
            cardDeck.remove(tempCard)
        
        if i%4 == 1:
            handCardDeck[1].append(tempCard)
            cardDeck.remove(tempCard)
        
        if i%4 == 2:
            handCardDeck[2].append(tempCard)
            cardDeck.remove(tempCard)
        
        if i%4 == 3:
            handCardDeck[3].append(tempCard)
            cardDeck.remove(tempCard)
    
    return cardDeck, handCardDeck

def showPlayerDrawn(username,handCardDeck): # Show prompt of the cards given to the user
    borderline()

    print("The cards being shuffled",end="")
    for _ in range(0,6):
        print(".",end="")

    print(f"\n\nI will now distribute the starting cards to {username}: \n")
    for card in handCardDeck[0]:
        time.sleep(0.8)
        print("You drawn: ",end="")
        card.showValueColour()
        print("")
    
    print("\nCards will also be distributed to the other 3 AI players\n")
    for _ in range(0,6):
        time.sleep(0.8)
        print(".",end="")
    
    print("")
    borderline()

def startDraw(deck): # Start random draw of one card as the starting card to play 
    tempCard = random.choice(deck)

    borderline()
    print("The starting card is: ",end="")
    time.sleep(0.8)
    tempCard.showValueColour()
    print("")
    borderline()

    return tempCard

def checkNumCards(deck): # Check the number of cards remaining in a deck
    numCard = 0
    for _ in deck:
        numCard += 1
    
    return numCard

def nextTurn(ascendingTurn,currentTurn): # Progress to the next round of the game after current round ends
    print("\nProceeding to next round",end="")
    for _ in range(0,3):
        time.sleep(0.9)
        print(".",end="")
    
    print("\n")

    if (ascendingTurn == False): 
        if (currentTurn == 0):
            currentTurn = 3
        else:
            currentTurn -= 1

    if (ascendingTurn == True): 
        if (currentTurn == 3):
            currentTurn = 0
        else:
            currentTurn += 1
    
    return currentTurn

def reverseFunc(ascendingTurn,turnTable): # Function to reverse the playing sequence when the reverse action card is played
    if ascendingTurn == True:
        turnTable = [3,2,1,0]

        return False, turnTable
    
    if ascendingTurn == False:
        turnTable = [0,1,2,3]
    
        return True, turnTable

def specialCardFunc(value,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable): # Function that calls to the corresponding effects of individual action cards

    match value:

        case 10:
            borderline()
            currentTurn = nextTurn(ascendingTurn,currentTurn)
            print(f"The current player {leaderboard[0][currentTurn]} will be skipped!!!")
            borderline()

        case 11:
            borderline()
            print("\nThe order of play will now be reversed!")
            
            print("\nFrom: ",end="")
            for turns in turnTable:
                print(" --> ",end="")
                print(leaderboard[0][turns],end="")
            
            ascendingTurn,turnTable = reverseFunc(ascendingTurn,turnTable)

            print("\n\nTo: ",end="")
            for turns in turnTable:
                print(" --> ",end="")
                print(leaderboard[0][turns],end="")
            print("\n")
            borderline()
            
        case 12:
            borderline()
            print("\nThe next player must draw 2 more cards!\n")
            numDraw+= 2
            draw2Check = True
            print(f"The next player must draw {numDraw} cards or play a Draw 2 card to avoid it!")
            borderline()

        case 14:
            borderline()
            print("The next player must draw 4 more cards!!!\n")
            numDraw += 4
            draw4Check = True
            print(f"The next player must draw {numDraw} cards or play a Draw 4 card to avoid it!")
            borderline()
    
    return currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable

def playerPlayCard(availableCardCheck,handCardDeck,discardDeck,leaderboard,winnerCircle,currentCard,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentTurn): # User can play cards if available 
    borderline()

    print("\nAvailable cards to play: \n")
    for i in range(0,len(availableCardCheck)):
        print(f"{i+1}. ",end="")
        handCardDeck[0][availableCardCheck[i]].showValueColour()
        print("")
    
    time.sleep(1)
    choiceCheck = False
    while(choiceCheck == False):
        playerChoice = input("\nChoice of card: ")
        borderline()
        if playerChoice.isdigit():
            playerChoice = int(playerChoice)
            if playerChoice >= 1 and playerChoice <= len(availableCardCheck):
                currentCard = handCardDeck[0][availableCardCheck[playerChoice-1]]
                handCardDeck[0].remove(currentCard)
                discardDeck.append(currentCard)
                lenDeck = checkNumCards(handCardDeck[0])

                if lenDeck == 0:
                    leaderboard[1][currentTurn] += 1
                    print(f"\n{leaderboard[0][currentTurn]} has won this game!!!!")
                    winnerCircle = True
                    choiceCheck = True
                    borderline()
                
                else:
                    print(f"\n{leaderboard[0][0]} has played ",end="")
                    currentCard.showValueColour()
                    print("!\n")
                    if currentCard.valueC >= 10 and currentCard.valueC != 13:
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                    choiceCheck = True
                    borderline()
            
            else:
                print(f"\nYou can only input between 1 or {len(availableCardCheck)}.")
        else:
            print("\nYou can only enter integers.")

    borderline()
    
    return availableCardCheck,handCardDeck,discardDeck,leaderboard,winnerCircle,currentCard,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentTurn

def botPlayCard(availableCardCheck,handCardDeck,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle): # Bots can play cards if available
    borderline()
    
    randomNum = random.choice(availableCardCheck)
    currentCard = handCardDeck[currentTurn][randomNum]
    handCardDeck[currentTurn].remove(currentCard)   
    time.sleep(1.5)
    print(f"\n{leaderboard[0][currentTurn]} has played ",end="")
    currentCard.showValueColour()
    print("!\n")
    lenDeck = checkNumCards(handCardDeck[currentTurn])

    if lenDeck == 0:
        leaderboard[1][currentTurn] += 1
        print(f"\n{leaderboard[0][currentTurn]} has won this game!!!!")
        winnerCircle = True
        borderline()
    else:
        if currentCard.valueC >= 10 and currentCard.valueC != 13:
            currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
        borderline()

    return availableCardCheck,handCardDeck,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle

def afterDrawPlayPlayer(handCardDeck,currentCard,currentTurn,leaderboard,discardDeck,draw4Check,draw2Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck): # After forced to draw cards due to Draw 4 Cards, any card in deck can be played by user 

    borderline()
    if currentCard.valueC == 14:
        lenDeck = checkNumCards(handCardDeck[0])
        print("\nYou can now play any cards.\n")
        print("Available Cards to Play:\n")
        for i in range(0,lenDeck):
            print(f"{i+1}. ",end="")
            handCardDeck[0][i].showValueColour()
            print("")

        time.sleep(1.1)
        choiceCheck = False
        while(choiceCheck == False):
            playerChoice = input("\nChoice of card: ")
            borderline()
            if playerChoice.isdigit():
                playerChoice = int(playerChoice)
                if playerChoice >= 1 and playerChoice <= lenDeck:
                    currentCard = handCardDeck[0][playerChoice-1]
                    handCardDeck[0].remove(currentCard)
                    discardDeck.append(currentCard)
                    
                    print(f"{leaderboard[0][0]} has played ",end="")
                    currentCard.showValueColour()
                    print("!\n")
                    if (currentCard.valueC >= 10 and currentCard.valueC != 13):
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                    borderline()
                    choiceCheck = True

                else:
                    print(f"\nYou can only input between 1 or {lenDeck}.")
            else:
                print("\nYou can only enter integers.")
    
    elif currentCard.valueC == 12:
        cardC = currentCard.colourC
        cardV = currentCard.valueC
        availableCardCheck = []

        lenDeck = checkNumCards(handCardDeck[currentTurn])

        for i in range(0,lenDeck):
            tempCard = handCardDeck[currentTurn][i]
            if tempCard.colourC == cardC or tempCard.valueC == cardV or tempCard.colourC == "Empty":
                availableCardCheck.append(i)

        lenAvailableDeck = checkNumCards(availableCardCheck)

        if lenAvailableDeck >= 1:
            availableCardCheck,handCardDeck,discardDeck,leaderboard,winnerCircle,currentCard,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentTurn = playerPlayCard(availableCardCheck,handCardDeck,discardDeck,leaderboard,winnerCircle,currentCard,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentTurn)

        else:
            leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,winnerCircle,numDraw = drawCardPlayer(leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,numDraw,winnerCircle)

    return handCardDeck,currentCard,currentTurn,leaderboard,discardDeck,draw4Check,draw2Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck

def afterDrawPlayBot(handCardDeck,currentTurn,currentCard,leaderboard,discardDeck,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck): # After forced to draw cards due to Draw 4 card, bot will randomly select a card in deck to play 
    
    borderline()

    if currentCard.valueC == 14:
        print(f"\nAfter drawing cards, {leaderboard[0][currentTurn]} can place any cards to its liking.")
        lenDeck = checkNumCards(handCardDeck[currentTurn])
        randomNum = random.randint(0,lenDeck-1)

        currentCard = handCardDeck[currentTurn][randomNum]
        handCardDeck[currentTurn].remove(currentCard)
        discardDeck.append(currentCard)
        time.sleep(1.5)
        print(f"\n{leaderboard[0][currentTurn]} has played ",end="")
        currentCard.showValueColour()
        print("!\n")  

        if currentCard.valueC >= 10 and currentCard.valueC != 13:
            currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)  
        
        borderline()
    
    else:
        cardC = currentCard.colourC
        cardV = currentCard.valueC
        
        lenDeck = checkNumCards(handCardDeck[currentTurn])
        availableCardCheck = []

        for i in range(0,lenDeck):
            tempCard = handCardDeck[currentTurn][i]
            if tempCard.colourC == cardC or tempCard.valueC == cardV or tempCard.colourC == "Empty":
                availableCardCheck.append(i)

        lenAvailableDeck = checkNumCards(availableCardCheck)

        if lenAvailableDeck >= 1:
            availableCardCheck,handCardDeck,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle = botPlayCard(availableCardCheck,handCardDeck,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle)

        else:
            discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle = drawCardBot(discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle)

    return handCardDeck,currentTurn,currentCard,leaderboard,discardDeck,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck

def drawCardPlayer(leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,numDraw,winnerCircle): # Force player to draw card due to draw 2, 4 or not having cards to play until the required card is drawn

    drawCardCheck = False
    lenDeck = checkNumCards(cardDeck)
    borderline()
    if (draw2Check == True or draw4Check == True):
        print(f"\nDue to not having a draw card, you are forced to draw {numDraw} cards.\n")
        while (numDraw > 0):
            if lenDeck > 0:
                time.sleep(1.1)
                pickCard = random.choice(cardDeck)
                cardDeck.remove(pickCard)
                handCardDeck[0].append(pickCard)
                print("You have drawn: ", end= "")
                pickCard.showValueColour()
                print("")
                numDraw -= 1
                
            else:
                time.sleep(1.1)
                pickCard = discardDeck[0]
                discardDeck.remove(pickCard)
                handCardDeck[0].append(pickCard)
                print("You have drawn: ", end= "")
                pickCard.showValueColour()
                print("")
                numDraw -= 1

        draw4Check = False
        draw2Check = False
        handCardDeck,currentCard,currentTurn,leaderboard,discardDeck,draw4Check,draw2Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck = afterDrawPlayPlayer(handCardDeck,currentCard,currentTurn,leaderboard,discardDeck,draw4Check,draw2Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck)

    else:
        print("\nDue to not having the required cards, you are forced draw until a card can be played.\n")
        while(drawCardCheck == False):
            if lenDeck > 0:
                time.sleep(1.1)
                pickCard = random.choice(cardDeck)
                cardDeck.remove(pickCard)
                handCardDeck[0].append(pickCard)
                print("You have drawn: ", end= "")
                pickCard.showValueColour()
                print("")
                if pickCard.colourC == currentCard.colourC or pickCard.valueC == currentCard.valueC or pickCard.colourC == "Empty":
                    currentCard = pickCard
                    handCardDeck[0].remove(currentCard)
                    discardDeck.append(currentCard)
                    print("\nThe card: ",end="")
                    pickCard.showValueColour()
                    print(" has been played")
                    print("")
                    if currentCard.valueC >= 10 and currentCard.valueC != 13:
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                    drawCardCheck = True
                
            else:
                time.sleep(1.1)
                pickCard = discardDeck[0]
                discardDeck.remove(pickCard)
                handCardDeck[0].append(pickCard)
                print("You have drawn: ", end= "")
                pickCard.showValueColour()
                print("")
                if pickCard.colourC == currentCard.colourC or pickCard.valueC == currentCard.valueC or pickCard.colourC == "Empty":
                    currentCard = pickCard
                    handCardDeck[0].remove(currentCard)
                    discardDeck.append(currentCard)
                    print("\nThe card: ",end="")
                    pickCard.showValueColour()
                    print(" has been played.")
                    print("")
                    if currentCard.valueC >= 10 and currentCard.valueC != 13:
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                    drawCardCheck = True

    borderline()
    return leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,winnerCircle,numDraw

def drawCardBot(discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle): # Force bots to draw card due to draw 2, 4 or not having cards to play until the required card is drawn
    drawCardCheck = False
    borderline()

    if (draw2Check == True or draw4Check == True):
        print(f"\n{leaderboard[0][currentTurn]} is forced to draw {numDraw} cards.")
        while (numDraw > 0):
            time.sleep(1.1)
            print(".",end="")
            if len(cardDeck) > 0:
                pickCard = random.choice(cardDeck)
                cardDeck.remove(pickCard)
                handCardDeck[currentTurn].append(pickCard)
                numDraw -= 1
            
            else:
                pickCard = discardDeck[0]
                discardDeck.remove(pickCard)
                handCardDeck[currentTurn].append(pickCard)
                numDraw -= 1

        print("\n")
        draw2Check = False
        draw4Check = False
        handCardDeck,currentTurn,currentCard,leaderboard,discardDeck,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck = afterDrawPlayBot(handCardDeck,currentTurn,currentCard,leaderboard,discardDeck,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,winnerCircle,cardDeck)

    else:

        print(f"\nDue to {leaderboard[0][currentTurn]} not having the required card, it is forced to draw until they have the required card.")
        while(drawCardCheck == False):
            time.sleep(1.1)
            print(".",end="")

            if len(cardDeck) > 0:
                pickCard = random.choice(cardDeck)
                cardDeck.remove(pickCard)  
                handCardDeck[currentTurn].append(pickCard)       
                if pickCard.colourC == currentCard.colourC or pickCard.valueC == currentCard.valueC or pickCard.colourC == "Empty":
                    currentCard = pickCard
                    handCardDeck[currentTurn].remove(currentCard)
                    discardDeck.append(currentCard)
                    print(f"\n\n{leaderboard[0][currentTurn]} has played ",end="")
                    currentCard.showValueColour()
                    print("")
                    if currentCard.valueC >= 10 and currentCard.valueC != 13:
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                    drawCardCheck = True
            
            else:
                pickCard = discardDeck[0]
                discardDeck.remove(pickCard)
                handCardDeck[currentTurn].append(pickCard)       
                if pickCard.colourC == currentCard.colourC or pickCard.valueC == currentCard.valueC or pickCard.colourC == "Empty":
                    currentCard = pickCard
                    discardDeck.append(currentCard)
                    handCardDeck[currentTurn].remove(currentCard)       
                    print(f"\n\n{leaderboard[0][currentTurn]} has played ",end="")
                    currentCard.showValueColour()
                    print("")
                    if currentCard.valueC >= 10 and currentCard.valueC != 13:
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                    drawCardCheck = True
    
    return discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle

def draw2or4Player(draw2Check,draw4Check,currentTurn,numDraw,ascendingTurn,turnTable,handCardDeck,availableCardCheck,discardDeck,leaderboard,winnerCircle,cardDeck,currentCard): # Check available cards to play for user
    borderline()
    lenDeck = checkNumCards(handCardDeck[0])
    for i in range(0,lenDeck):
        if draw2Check == True:
            if handCardDeck[0][i].valueC == 12:
                availableCardCheck.append(i)
        if draw4Check == True:
            if handCardDeck[0][i].valueC == 14:
                availableCardCheck.append(i)

    if len(availableCardCheck) > 0:
        print("\nAvailable cards to play: \n")
        for i in range(0,len(availableCardCheck)):
            print(f"{i+1}. ",end="")
            handCardDeck[0][availableCardCheck[i]].showValueColour()
            print("")
        
        choiceCheck = False
        while(choiceCheck == False):
            playerChoice = input("\nChoice of card: ")
            borderline()
            if playerChoice.isdigit():
                playerChoice = int(playerChoice)
                if playerChoice >= 1 and playerChoice <= len(availableCardCheck):
                    currentCard = handCardDeck[0][availableCardCheck[playerChoice-1]]
                    handCardDeck[0].remove(currentCard)
                    discardDeck.append(currentCard)
                    lenDeck = checkNumCards(handCardDeck[0])

                    if lenDeck == 0:
                        leaderboard[1][currentTurn] += 1
                        print(f"{leaderboard[0][currentTurn]} has won this game!!!!")
                        winnerCircle = True
                    
                    else:
                        print(f"{leaderboard[0][0]} has played ")
                        currentCard.showValueColour()
                        print("")
                        currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)
                
                else:
                    print(f"\nYou can only input between 1 or {len(availableCardCheck)}.")
            else:
                print("\nYou can only enter integers.")
            
            choiceCheck = True

    else:
        leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,winnerCircle,numDraw = drawCardPlayer(leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,numDraw,winnerCircle)
    
    return draw2Check,draw4Check,currentTurn,numDraw,ascendingTurn,turnTable,handCardDeck,availableCardCheck,discardDeck,leaderboard,winnerCircle,cardDeck,currentCard

def draw2or4Bot(currentCard,availableCardCheck,handCardDeck,draw2Check,draw4Check,currentTurn,leaderboard,ascendingTurn,turnTable,numDraw,cardDeck,discardDeck,winnerCircle): # Check available cards to play for bot
    lenDeck = checkNumCards(handCardDeck[currentTurn])
    for i in range(0,lenDeck):
        if draw2Check == True:
            if handCardDeck[currentTurn][i].valueC == 12:
                availableCardCheck.append(i)
        if draw4Check == True:
            if handCardDeck[currentTurn][i].valueC == 14:
                availableCardCheck.append(i)

    if len(availableCardCheck) > 0:
        randomNum = random.choice(availableCardCheck)
        currentCard = handCardDeck[currentTurn][randomNum]
        handCardDeck[currentTurn].remove(currentCard)   
        print(f"\n{leaderboard[0][currentTurn]} has played ")
        currentCard.showValueColour()
        print("")  
        lenDeck = checkNumCards(handCardDeck[currentTurn])

        if lenDeck == 0:
            leaderboard[1][currentTurn] += 1
            print(f"{leaderboard[0][currentTurn]} has won this game!!!!")
            winnerCircle = True

        elif currentCard.valueC >= 10 and currentCard.valueC != 13:
            currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)    
    
    else:
        discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle = drawCardBot(discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle)
    
    return currentCard,availableCardCheck,handCardDeck,draw2Check,draw4Check,currentTurn,leaderboard,ascendingTurn,turnTable,numDraw,cardDeck,discardDeck,winnerCircle

def playerCurrentCards(handCardDeck): # Show user current cards in card deck
    time.sleep(1.5)
    numCards = checkNumCards(handCardDeck[0])
    borderline()
    print("\nYour Card Deck: \n")
    for i in range(0,numCards):
        print(f"{i+1}. ",end="")
        handCardDeck[0][i].showValueColour()
        print("")
    print("")
    borderline()

def controlFunc(currentCard,handCardDeck,currentTurn,ascendingTurn,leaderboard,draw2Check,draw4Check,numDraw,turnTable,discardDeck,winnerCircle,cardDeck): # Control which function should be called in different situations
    cardV = currentCard.valueC
    cardC = currentCard.colourC
    availableCardCheck = []

    if draw2Check == True:
        if currentTurn == 0:
            draw2Check,draw4Check,currentTurn,numDraw,ascendingTurn,turnTable,handCardDeck,availableCardCheck,discardDeck,leaderboard,winnerCircle,cardDeck,currentCard = draw2or4Player(draw2Check,draw4Check,currentTurn,numDraw,ascendingTurn,turnTable,handCardDeck,availableCardCheck,discardDeck,leaderboard,winnerCircle,cardDeck,currentCard)
            currentTurn = nextTurn(ascendingTurn,currentTurn)
        
        else:
            currentCard,availableCardCheck,handCardDeck,draw2Check,draw4Check,currentTurn,leaderboard,ascendingTurn,turnTable,numDraw,cardDeck,discardDeck,winnerCircle = draw2or4Bot(currentCard,availableCardCheck,handCardDeck,draw2Check,draw4Check,currentTurn,leaderboard,ascendingTurn,turnTable,numDraw,cardDeck,discardDeck,winnerCircle)
            currentTurn = nextTurn(ascendingTurn,currentTurn)

    elif draw4Check == True:
        if currentTurn == 0:
            draw2Check,draw4Check,currentTurn,numDraw,ascendingTurn,turnTable,handCardDeck,availableCardCheck,discardDeck,leaderboard,winnerCircle,cardDeck,currentCard = draw2or4Player(draw2Check,draw4Check,currentTurn,numDraw,ascendingTurn,turnTable,handCardDeck,availableCardCheck,discardDeck,leaderboard,winnerCircle,cardDeck,currentCard)
            currentTurn = nextTurn(ascendingTurn,currentTurn)
        
        else:
            currentCard,availableCardCheck,handCardDeck,draw2Check,draw4Check,currentTurn,leaderboard,ascendingTurn,turnTable,numDraw,cardDeck,discardDeck,winnerCircle = draw2or4Bot(currentCard,availableCardCheck,handCardDeck,draw2Check,draw4Check,currentTurn,leaderboard,ascendingTurn,turnTable,numDraw,cardDeck,discardDeck,winnerCircle)
            currentTurn = nextTurn(ascendingTurn,currentTurn)

    else:
        borderline()
        print(f"\nThe current player is {leaderboard[0][currentTurn]}\n")
        print("The next card played can either be: ")
        currentCard.showColour()
        currentCard.showValue()
        if currentCard.valueC == 13:
            print("Draw 4")
        elif currentCard.valueC == 14:
            pass
        else:
            print("Draw 4")
            print("Wild Card")

        lenDeck = checkNumCards(handCardDeck[currentTurn])

        if currentCard.colourC == "Empty":
            availableCardCheck = range(0,lenDeck)
        else:
            for i in range(0,lenDeck):
                tempCard = handCardDeck[currentTurn][i]
                if tempCard.colourC == cardC or tempCard.valueC == cardV or tempCard.colourC == "Empty":
                    availableCardCheck.append(i)

        lenAvailableDeck = checkNumCards(availableCardCheck)

        if lenAvailableDeck >= 1:
            if currentTurn == 0:
                availableCardCheck,handCardDeck,discardDeck,leaderboard,winnerCircle,currentCard,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentTurn = playerPlayCard(availableCardCheck,handCardDeck,discardDeck,leaderboard,winnerCircle,currentCard,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentTurn)
                currentTurn = nextTurn(ascendingTurn,currentTurn)
            else:
                availableCardCheck,handCardDeck,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle = botPlayCard(availableCardCheck,handCardDeck,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle)
                currentTurn = nextTurn(ascendingTurn,currentTurn)

        else:
            if currentTurn == 0:
                leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,winnerCircle,numDraw = drawCardPlayer(leaderboard,currentCard,handCardDeck,discardDeck,draw2Check,draw4Check,cardDeck,currentTurn,ascendingTurn,turnTable,numDraw,winnerCircle)
                currentTurn = nextTurn(ascendingTurn,currentTurn)

            else:
                discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle = drawCardBot(discardDeck,cardDeck,draw4Check,draw2Check,handCardDeck,currentTurn,leaderboard,numDraw,ascendingTurn,turnTable,currentCard,winnerCircle)
                currentTurn = nextTurn(ascendingTurn,currentTurn)

    return currentCard,handCardDeck,currentTurn,ascendingTurn,leaderboard,draw2Check,draw4Check,numDraw,turnTable,discardDeck,winnerCircle,cardDeck

def displayRemainCards(handCardDeck,leaderboard): # Display amount of cards remaining of each player
    borderline()
    time.sleep(1.5)
    print("\nCards Left For Each Players\n")
    for i in range(0,4):
        numCard = checkNumCards(handCardDeck[i])
        print(f"{leaderboard[0][i]} : ",end="")
        print(Fore.RED + f"{numCard} ",end="")
        print(Style.RESET_ALL + "cards")
    print("")
    borderline()

def main(): # Main function where all the functions form a functional game
    leaderboard = [["Player","AI One","AI Two","AI Three"],[0,0,0,0]]

    exitStatus = False

    welcomeMessage()
    leaderboard[0][0] = userSetName()

    while (exitStatus == False):
        handCardDeck = [[],[],[],[]]
        discardDeck = []
        cardDeck = []

        currentCard = 0
        currentTurn = 0
        ascendingTurn = True
        turnTable = [0,1,2,3]
        numDraw = 0
        winnerCircle = False

        draw2Check = False
        draw4Check = False

        cardDeck = createDeck(cardDeck)
        random.shuffle(cardDeck)

        userChoice = menuChoice(leaderboard[0][0])

        match userChoice:

            case 1:
                cardDeck, handCardDeck = giveStartCards(cardDeck,handCardDeck)
                showPlayerDrawn(leaderboard[0][0],handCardDeck)
                currentCard = startDraw(cardDeck)
                if currentCard.valueC >= 11 and currentCard.valueC != 13:
                    currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable = specialCardFunc(currentCard.valueC,leaderboard,currentTurn,draw2Check,draw4Check,numDraw,ascendingTurn,turnTable)

                elif currentCard.valueC == 10:
                    print(f"The current player {leaderboard[0][currentTurn]} will be skipped!!!")
                    currentTurn = nextTurn(ascendingTurn,currentTurn)
            
                while (winnerCircle == False):
                    displayRemainCards(handCardDeck,leaderboard)
                    if currentTurn == 0:
                        playerCurrentCards(handCardDeck)
                    currentCard,handCardDeck,currentTurn,ascendingTurn,leaderboard,draw2Check,draw4Check,numDraw,turnTable,discardDeck,winnerCircle,cardDeck = controlFunc(currentCard,handCardDeck,currentTurn,ascendingTurn,leaderboard,draw2Check,draw4Check,numDraw,turnTable,discardDeck,winnerCircle,cardDeck)

            case 2:
                rulesOfUno()

            case 3:
                showLeaderboard(leaderboard)

            case 4:
                checkWinner(leaderboard)
                exitStatus = True