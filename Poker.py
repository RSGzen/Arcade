import random #poker hand
import time


flower=[" (♠) spades"," (♥) hearts"," (♦) diamonds "," (♣) clubs "]
number=["Ace","2","3","4","5","6","7","8","9","Jack","Queen","King"]

def check_flowerAndnumber(tempCard):
    value = int(tempCard % 13)
    cardValue = number[value-1] #-1 else will over range
    cardFlower = flower[tempCard // 13]

    finalCardValue = (str(cardValue) + str(cardFlower))
    return finalCardValue

def getcard(allcard):
    playerCompCard= allcard[:2] #get card from the main deck
    allcard[:] = allcard [2:]   #Remove the card from the main deck
    return playerCompCard,allcard

def getcardCommunity(x,allcard):
    communityCompCard= allcard[:x] #get card from the main deck
    allcard[:] = allcard [x:]      #Remove the card from the main deck
    return communityCompCard,allcard

def count_duplicates(list):
    seen = {} #dictionary 
    for num in list:
        #dictionary.get(keyname, value)
        seen[num] = seen.get(num, 0) + 1 #set the key=num and value =value+1
    
    duplicates = {} #dictionary
    for num, count in seen.items(): #in seen key-value
        if count > 1: #- value >1 then append it 
            duplicates[num] = count
    duplicates = {num: count for num, count in seen.items() if count > 1} #new dictionary which will only assig number if the count in seen the >1
    return duplicates

def checkCard(communityCard,playerCompCard):

    deck= communityCard + playerCompCard
    playerFlower=[] #flower=suit
    playerValue=[]  #value=rank

    for i in range (len(deck)):
        flowerValue=deck[i]//13
        cardValue=deck[i]%13
        playerValue.append(cardValue)
        playerFlower.append(flowerValue)


    duplicateFlower=count_duplicates(playerFlower)
    duplicateValue=count_duplicates(playerValue) 
    doubleLst=[]
    tripleLst=[]
    rank="Hello"#just set a random value
    if bool(duplicateValue)==False: #duplicateValue == empthy list
        rank="High Card"
        
    

    else:    
        for value in duplicateValue.values():

            if value==3:
                rank="Three of a kind"

            if value==2:
                
                for key in duplicateValue:
                    if duplicateValue[key]==2: #if the value being duplicated for 2 time then key will be put in other list
                        doubleLst.append(key)
                    if duplicateValue[key]==3:#if the value being duplicated for 3 time then key will be put in other list
                        tripleLst.append(key)
                

                if (len(doubleLst))==1:
                    if (rank !="Flush") and (rank != "Three of a kind"):
                        rank="One pair"

                if (len(doubleLst))>=2:
                    if (rank !="Flush") and (rank != "Three of a kind"):
                        rank="Two pair"

            if tripleLst and all(tripleLst): #chcek if tripleLst is an empty list  
                if (len(tripleLst))==1 and (len(doubleLst))==1:
                    rank="Full house" 

            elif value==4:
                rank="Four of a kind"
                

    if bool(duplicateFlower)==True:
        for value in duplicateFlower.values():
            if (value==5 and (rank!="Full house")) or (value==5 and (rank!="Four of a kind")):
                rank="Flush"

    return rank
     
def playerAction(player2win):
    while True:
        playerAction1=int(input("\nWhat Action do you want to do?\n1.Fold\n2.Check\nYour Action(1,2) :"))
        if playerAction1 == 1 :
            print("\nYou Foled")
            print("Player 2 won ")
            player2win = player2win + 1
            break
        
        elif playerAction1 == 2 :
            player2win=0
            print("\nYou check.")
            break

        else:
            player2win=0
            print("Wrong input")
        
    return  player2win

def botAction(player1win):
    actionlist=[1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]    
    botAction1=random.choice(actionlist)
    if botAction1 == 1 :
        time.sleep(1.5)
        print("Bot Foled")
        print("\nPlayer 1 won")
        player1win = player1win + 1
    
    elif botAction1 == 2 :
        player1win=player1win
        time.sleep(1.0)
        print("Bot check.")

    return  player1win


def main():
    print("\nWelcome to this simple poker game machine")
    startInp=6
    computerWin=0
    drawGame=0
    playerWin=0
    while startInp!= 4:
        time.sleep(0.5)
        startInp=int(input("\n ___________Menu___________\n| 1. Rules and Regulations |\n| 2. Start Game            |\n| 3. Match History         |\n| 4. Quit                  |\n ==========================\nYour Move (1,2,3,4) :"))
        allcard=[x for x in range(52)]
        random.shuffle(allcard)
        player1win=0
        player2win=0


        if startInp == 4:
            print("Thank you for playing this game\n")
            break

        elif startInp == 1:
            print("\nRule for this simple poker machine, it is different from others poker game:")#just use a def to priunt all that
            time.sleep(1.5)
            print(" ________________________________________________________________________________ ")
            print("|  Basic  | 1. There are 52 cards needed for this game to start.                 |")
            print("|         | 2. Suit =Clubs (♣), Diamonds (♦), Hearts (♥), and Spades (♠)         |")
            print("|         | 3. Rank =Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King          |")
            print("|         | 4. This poker game is played by a player and a computer              |")
            print("|         | 5. There is no bet system.                                           |")
            print("|         | 6. The Action:                                                       |")
            print("|         |      I. Check (continue game)       II. Fold (surrender)             |")
            print("|         |                                                                      |")
            print("|         | 7. If both the Player and Bot have the same rank, draw will happend. |")
            print("|         |                                                                      |")
            print("|---------|----------------------------------------------------------------------|")
            print("|         |                                                                      |")
            print("|  Flow   | 1. Game start, each player will be given for 2 cards.                |")
            print("|         | 2. All player can take a look at his own card and decide if he/she   |")
            print("|         |    want to continue the game(Check) or surrender(Fold).              |")
            print("|         | 3. If both the player decide to continue game, 3 card will be draw,  |")
            print("|         |    three of the card will known as community card.                   |")
            print("|         | 4. All player can now decide to continue the game(Check) or          |")
            print("|         |    surrender(Fold).                                                  |")
            print("|         | 5. If both the player decide to continue game, 1 card will be draw,  |")
            print("|         |    the card will be added to community card.                         |")
            print("|         | 6. All player can now decide to continue the game(Check) or          |")
            print("|         |    to continue the game(Check) or surrender(Fold).                   |")
            print("|         | 7. If both the player decide to continue game, last card will be     |")
            print("|         |    draw, the last card will be added to community card.              |")
            print("|         | 8. All player can now decide to continue the game(Check) or          |")
            print("|         |    to continue the game(Check) or surrender(Fold).                   |")
            print("|         | 9. If both the player decide to continue game, both player will      |")
            print("|         |    try to make the highest rank between community card and           |") 
            print("|         |    his/her cards.                                                    |")
            print("|         |10. The player with the highest rank will win the game                |")
            print("|         |                                                                      |")
            print("|---------|----------------------------------------------------------------------|")
            print("|         |                                                                      |")
            print("| Ranking | The ranking system for this poker game (from High to Low)            |")
            print("|         | 1. Four of a Kind                                                    |")
            print("|         | 2. Full House                                                        |")
            print("|         | 3. Flush                                                             |")
            print("|         | 4. Three of a Kind                                                   |")
            print("|         | 5. Two Pair                                                          |")
            print("|         | 6. One Pair                                                          |")
            print("|         | 7. High Card                                                         |")
            print("|---------|----------------------------------------------------------------------|")
            print("| Four of | Four card of the same rank, plus one card of another rank            |")
            print("|  a Kind | -Example: A(♣),A(♦),A(♥),A(♠),7(♠)                                   |")
            print("|---------|----------------------------------------------------------------------|")
            print("| Full    | Three card of the same rank, plus two card of another same rank      |")
            print("|  house  | -Example: A(♣),A(♦),A(♥),K(♠),K(♠)                                   |")
            print("|---------|----------------------------------------------------------------------|")
            print("| Flush   | All five card have the same suit                                     |")
            print("|         | -Example: A(♣),8(♣),6(♣),5(♣),3(♣)                                   |")
            print("|---------|----------------------------------------------------------------------|")
            print("| Three of| Three card of the same rank, plus two other card which are not pair  |")
            print("|  a Kind | -Example: A(♣),A(♦),A(♥),4(♠),3(♠)                                   |")
            print("|---------|----------------------------------------------------------------------|")
            print("| Two pair| Two different set of card with the same rank, plus one more card     |")
            print("|         | -Example: A(♣),A(♦),Q(♥),Q(♠),3(♠)                                   |")
            print("|---------|----------------------------------------------------------------------|")
            print("| One pair| Two card of the same rank, plus three more unmatch card              |")
            print("|         | -Example: A(♣),A(♦),7(♥),4(♠),2(♠)                                   |")
            print("|---------|----------------------------------------------------------------------|")
            print("| High    | Any other configuration of cards, ranked from highest card to lowest |")
            print("|   card  | -Example: A(♣),K(♦),7(♥),4(♠),2(♠)                                   |")
            print("|_________|______________________________________________________________________|")

        elif startInp == 2:
            endGame=0
            while endGame==0:
                player1CompCard,allcard=getcard(allcard) #transform the computer value(52) into King(♣)
                player1Card = [check_flowerAndnumber(card) for card in player1CompCard] #player1Card will be result of check_flowerAndnumber
                time.sleep(0.5)
                print("\nPlayer 1's Cards :")
                for card in player1Card:
                    time.sleep(0.5)
                    print(card)

                print("\nCard for player 2(computer)") 
                player2CompCard,allcard=getcard(allcard) #transform the computer value(52) into King(♣)
                player2Card = [check_flowerAndnumber(card) for card in player2CompCard] #player2Card will be result of check_flowerAndnumber
                time.sleep(0.5)
                print("Player 2 Cards :")
                time.sleep(0.5)
                print("Hident\n")



                player2win=playerAction(player2win) #if fold is taken then it willbreak
                if player2win!=0:
                    computerWin = computerWin +1
                    break
                else:
                    pass


                player1win=botAction(player1win) #if fold is taken then it willbreak
                if player1win!=0:
                    playerWin= playerWin +1
                    break
                else:
                    pass

                print("\nTime to draw 3 card for the community card.")
                time.sleep(1.0)
                communityCompCard,allcard=getcardCommunity(5,allcard) #transform the computer value(52) into King(♣)
                communityCard=[check_flowerAndnumber(card) for card in communityCompCard] #communityCard will be result of check_flowerAndnumber  
                for card in range (0,3):
                    time.sleep(0.5)
                    print(communityCard[card])

                print("\nPlayer 1's Cards :")
                for card in player1Card:
                    time.sleep(0.5)
                    print(card)

                player2win=playerAction(player2win)
                if player2win!=0:
                    computerWin = computerWin +1
                    break
                else:
                    pass


                player1win=botAction(player1win)
                if player1win!=0:
                    playerWin= playerWin +1
                    break
                else:
                    pass

                #printing community and player's cards
                print("\nTime to draw 1 more card for the community card.")
                time.sleep(1.0)
                for card in range(0,4):
                    time.sleep(0.5)
                    print(communityCard[card])
                print("\nPlayer 1's Cards :")
                for card in player1Card:
                    time.sleep(0.5)
                    print(card)

                player2win=playerAction(player2win)
                if player2win!=0:
                    computerWin = computerWin +1
                    break
                else:
                    pass


                player1win=botAction(player1win)
                if player1win!=0:
                    playerWin= playerWin +1
                    break
                else:
                    pass

                #printing community and player's cards
                print("\nTime to draw last card for the community card.")
                time.sleep(1.0)
                for card in range (0,5):
                    time.sleep(0.5)
                    print(communityCard[card])
                print("\nPlayer 1's Cards :")
                for card in player1Card:
                    time.sleep(0.5)
                    print(card)

                player2win=playerAction(player2win)
                if player2win==1:
                    break
                else:
                    pass
                player1win=botAction(player1win)
                if player1win==1:
                    break
                else:
                    pass
                
                #check for  the rank of both the player and computer
                playerRank=checkCard(communityCompCard,player1CompCard)
                computerRank=checkCard(communityCompCard,player2CompCard)

                #printing all community, player and computer's cards
                print("\n")
                time.sleep(0.3)
                print("Community card:")
                for card in communityCard:
                    time.sleep(0.5)
                    print(card)
                print("\n")

                time.sleep(0.3)
                print("Player 1 card:")
                for card in player1Card:
                    time.sleep(0.5)
                    print(card)
                time.sleep(0.3)
                print("Rank :",playerRank)
                print("\n")

                time.sleep(0.3)
                print("Player 2 card:")
                for card in player2Card:
                    time.sleep(0.5)
                    print(card)
                time.sleep(0.3)
                print("Rank :",computerRank)
                print("\n")

                
                #chcecking all the condition that computer will win
                if playerRank==computerRank:
                    time.sleep(1.5)
                    print("Draw")
                    drawGame = drawGame + 1

                    break
                elif playerRank=="High Card" and computerRank!="High Card":
                    time.sleep(1.5)
                    print("Computer Win")
                    computerWin = computerWin +1
                    break
                elif (playerRank=="One pair" and computerRank == "Two pair") or (playerRank=="One pair" and computerRank == "Three of a kind") or (playerRank=="One pair" and computerRank == "Flush") or (playerRank=="One pair" and computerRank == "Full house") or (playerRank=="One pair" and computerRank == "Four of a kind"):
                    print("Computer win")
                    time.sleep(1.5)
                    computerWin = computerWin +1
                    break
                elif (playerRank=="Two pair" and computerRank == "Three of a kind") or (playerRank=="Two pair" and computerRank == "Flush") or (playerRank=="Two pair" and computerRank == "Full house") or (playerRank=="Two pair" and computerRank == "Four of a kind"):
                    time.sleep(1.5)
                    print("Computer win")
                    computerWin = computerWin +1
                    break
                elif (playerRank=="Three of a kind" and computerRank == "Flush") or (playerRank=="Three of a kind" and computerRank == "Full house") or (playerRank=="Three of a kind" and computerRank == "Four of a kind"):
                    time.sleep(1.5)
                    print("Computer win")
                    computerWin = computerWin +1
                    break
                elif (playerRank=="Flush" and computerRank == "Full house") or (playerRank=="Flush" and computerRank == "Four of a kind"):
                    time.sleep(1.5)
                    print("Computer Win")
                    computerWin = computerWin +1
                    break
                elif (playerRank=="Full house" and computerRank == "Four of a kind"):
                    time.sleep(1.5)
                    print("Computer Win")
                    computerWin = computerWin +1
                    break
                else:
                    time.sleep(1.5)
                    print("Player Win")
                    playerWin= playerWin +1
                    break

            time.sleep(0.5)
            print("Good game")


        elif startInp==3:
            totalGame=playerWin+computerWin+drawGame
            print("\nThe Match History :")
            time.sleep(1.5)
            print(" _____________________")
            print("| Player win   | ",playerWin,"  |") #idk why dont remember player had win
            print("|--------------|------|")
            print("| Computer win | ",computerWin,"  |")
            print("|--------------|------|")
            print("|   Total Game | ",totalGame,"  |")
            print("|______________|______|")


        else:
            print("Wrong Input")

