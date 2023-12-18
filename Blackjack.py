import copy
import random
import pygame
import time

def main():
    pygame.init()
    deck_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    one_deck = 4 * deck_cards
    decks = 1
    Width = 1000     #Screen Width
    Height = 900     #Screen Height
    bg_screen = pygame.display.set_mode([Width, Height])
    cobaltgreen= (20,185,91)
    pygame.display.set_caption('BlackJack')
    fps = 60
    game_time = pygame.time.Clock()
    word_font = pygame.font.Font('freesansbold.ttf', 44)    #Free font in pygame
    small_font = pygame.font.Font('freesansbold.ttf', 36) 
    active = False
    player_score = 0
    dealer_score = 0
    initial_deal = False
    player_hand = []
    dealer_hand = []
    game_outcome = 0
    reveal_dealer = False
    player_active = False
    add_score = False
    player_money = 10000
    bet_value='0'  
    rect_for_bet= pygame.Rect(790,200,140,32)
    results = ['','You Win :)', 'Dealer Win :(', 'Its a Draw']

    #Display the player's money
    def check_money():
        money_text = small_font.render(f'Player Money: {player_money}', True, 'white')
        bg_screen.blit(money_text, (600, 50))
        bet_text = small_font.render('Enter Bet:', True, 'white')
        bg_screen.blit(bet_text, (600, 200))
        pygame.draw.rect(bg_screen,'white',rect_for_bet,2)
        bet_text= small_font.render(bet_value,True,'white')
        bg_screen.blit(bet_text,(790,200))


    #Begin to shuffle the cards
    def shuffle_cards(current_hand, current_deck):
        card = random.randint(0, len(current_deck))
        current_hand.append(current_deck[card - 1])
        current_deck.pop(card - 1)
        return current_hand, current_deck

    #Display the player and dealer score
    def create_scores(player, dealer):
        bg_screen.blit(word_font.render('Dealer',True,'black'),(0,100))
        bg_screen.blit(word_font.render('Player(You)',True,'red'),(0,400))
        bg_screen.blit(word_font.render(f'Score[{player}]', True, 'white'), (350, 400))
        if reveal_dealer:
            bg_screen.blit(word_font.render(f'Score[{dealer}]', True, 'white'), (350, 100))

    #Draw the cards
    def create_cards(player, dealer, reveal):
        for i in range(len(player)):
            pygame.draw.rect(bg_screen, 'white', [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
            bg_screen.blit(word_font.render(player[i], True, 'black'), (75 + 70 * i, 465 + 5 * i))
            bg_screen.blit(word_font.render(player[i], True, 'black'), (143 + 70 * i, 635 + 5 * i))
            pygame.draw.rect(bg_screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

        for i in range(len(dealer)):
            pygame.draw.rect(bg_screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
            if i != 0 or reveal:
                bg_screen.blit(word_font.render(dealer[i], True, 'black'), (75 + 70 * i, 165 + 5 * i))
                bg_screen.blit(word_font.render(dealer[i], True, 'black'), (143 + 70 * i, 335 + 5 * i))
            else:
                bg_screen.blit(word_font.render('?', True, 'black'), (75 + 70 * i, 165 + 5 * i))
                bg_screen.blit(word_font.render('?', True, 'black'), (143 + 70 * i, 335 + 5 * i))
            pygame.draw.rect(bg_screen, 'black', [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)

    #Calculate the score
    def sum_up_score(hand):
        player_dealer_score = 0
        aces_count = hand.count('A')
        for i in range(len(hand)):
            for j in range(8):
                if hand[i] == deck_cards[j]:
                    player_dealer_score += int(hand[i])
            if hand[i] in ['10', 'J', 'Q', 'K']:
                player_dealer_score += 10
            elif hand[i] == 'A':
                player_dealer_score += 11
        if player_dealer_score > 21 and aces_count > 0:
            for i in range(aces_count):
                if player_dealer_score > 21:
                    player_dealer_score -= 10
        return player_dealer_score

    #Create buttons and score bar
    def create_buttons(act, result, player_hand):
        game_button_list = []
        if not act:
            deal = pygame.draw.rect(bg_screen, 'white', [150, 20, 320, 100], 0, 5)
            pygame.draw.rect(bg_screen, 'purple', [150, 20, 320, 100], 3, 5)                          #Shuffle cards button
            deal_text = word_font.render('Shuffle Cards', True, 'black')
            bg_screen.blit(deal_text, (165, 50))
            game_button_list.append(deal)
        else:
            if len(player_hand) == 2 and sum_up_score(player_hand) == 15:                    
                stay = pygame.draw.rect(bg_screen, 'white', [0, 700, 300, 100], 0, 5)                 #Stay button
                pygame.draw.rect(bg_screen, 'blue', [0, 700, 300, 100], 3, 5)                   
                stay_text = word_font.render('Stay', True, 'black')
                bg_screen.blit(stay_text, (55, 735))
                game_button_list.append(stay)
                run = pygame.draw.rect(bg_screen, 'white', [300, 700, 300, 100], 0, 5)                #Run button
                pygame.draw.rect(bg_screen, 'red', [300, 700, 300, 100], 3, 5)
                run_text = word_font.render('Run', True, 'black')
                bg_screen.blit(run_text, (355, 735))
                game_button_list.append(run)
            
            else:
                hit = pygame.draw.rect(bg_screen, 'white', [0, 700, 300, 100], 0, 5)                  #Hit button
                pygame.draw.rect(bg_screen, 'blue', [0, 700, 300, 100], 3, 5)
                hit_text = word_font.render('    Hit', True, 'black')
                bg_screen.blit(hit_text, (55, 735))
                game_button_list.append(hit)
                if player_score >15:
                    stand = pygame.draw.rect(bg_screen, 'white', [300, 700, 300, 100], 0, 5)           #Stand button
                    pygame.draw.rect(bg_screen, 'red', [300, 700, 300, 100], 3, 5)
                    stand_text = word_font.render('Stand', True, 'black')
                    bg_screen.blit(stand_text, (355, 735))
                    game_button_list.append(stand)

        if result != 0:
            bg_screen.blit(word_font.render(results[result], True, 'white'), (15, 25))
            deal = pygame.draw.rect(bg_screen, 'white', [150, 220, 300, 100], 0, 5)
            pygame.draw.rect(bg_screen, 'green', [150, 220, 300, 100], 3, 5)
            pygame.draw.rect(bg_screen, 'black', [153, 223, 294, 94], 3, 5)
            deal_text = word_font.render('New Game', True, 'black')
            bg_screen.blit(deal_text, (165, 250))
            game_button_list.append(deal)

        return game_button_list

    #The condition for the game to end
    def condition_endgame(hand_act, deal_score, play_score, result, add, player_money, player_hand, dealer_hand):
        if not hand_act and deal_score >= 17:
            player_blackjack = ('A' in player_hand) and any(card in ['10', 'J', 'Q', 'K'] for card in player_hand) and len(player_hand) == 2
            dealer_blackjack = ('A' in dealer_hand) and any(card in ['10', 'J', 'Q', 'K'] for card in dealer_hand) and len(dealer_hand) == 2
            if player_score == 15 and len(player_hand) == 2:     #Special conditions
                    result = 3
            elif dealer_blackjack and not player_blackjack:
                result = 2  
            elif player_blackjack and not dealer_blackjack:
                result = 1  
            elif player_blackjack and dealer_blackjack:
                result = 3  
            elif play_score > 21:
                if deal_score > 21:
                    result = 3  
                else:
                    result = 2 
            elif deal_score > 21:
                result = 1  
            elif play_score == deal_score:
                result = 3  
            elif play_score > deal_score:
                result = 1  
            else:
                result = 2  

        return result, add, player_money

    def exit():
        exit_button = pygame.draw.rect(bg_screen, 'white', [700, 300, 200, 100], 0, 5)
        pygame.draw.rect(bg_screen, 'red', [700, 300, 200, 100], 3, 5)
        exit_text = word_font.render('Exit', True, 'black')
        bg_screen.blit(exit_text, (750, 330))
        return exit_button
    #The main code
    run = True
    while run:
        if player_money<=0:             #Player money will reset to the usual amount if it is less than or equal 0
           player_money=10000                          
        game_time.tick(fps)
        bg_screen.fill(cobaltgreen)
        if initial_deal:
            for i in range(2):
                player_hand, game_deck = shuffle_cards(player_hand, game_deck)
                dealer_hand, game_deck = shuffle_cards(dealer_hand, game_deck)
            initial_deal = False

        if active:
            player_score = sum_up_score(player_hand)
            create_cards(player_hand, dealer_hand, reveal_dealer)
            if reveal_dealer:
                dealer_score = sum_up_score(dealer_hand)
                if dealer_score < 17:
                    dealer_hand, game_deck = shuffle_cards(dealer_hand, game_deck)
            create_scores(player_score, dealer_score)
            check_money()
        buttons = create_buttons(active, game_outcome, player_hand)

        if len(player_hand) == 5 and player_score <= 21:   #Special conditions
            game_outcome = 1  
            reveal_dealer = True          
            active = True
        if len(dealer_hand) == 5 and dealer_score <= 21:    #Special conditions
            game_outcome = 2  
            reveal_dealer = True
            active = True

        exit_button=exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                if bet_value == '0':  
                    bet_value = event.unicode  
                else:
                    if event.key ==pygame.K_BACKSPACE:
                        bet_value = bet_value[:-1]
                    else:
                        bet_value+= event.unicode
                if bet_value.isdigit():  
                    bet = int(bet_value)
                    if bet > player_money:  
                        bet_value = str(player_money)
        
            if event.type == pygame.MOUSEBUTTONUP:
                if exit_button.collidepoint(event.pos):
                    run = False
                if not active:
                    if buttons[0].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        player_hand = []
                        dealer_hand = []
                        game_outcome = 0
                        player_active = True
                        reveal_dealer = False
                        add_score = True  
                else:
                    if buttons[0].collidepoint(event.pos) and player_score < 21 and player_active:
                        player_hand, game_deck = shuffle_cards(player_hand, game_deck)
                    elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                        reveal_dealer = True
                        player_active = False
                    elif len(buttons) == 3:
                        if buttons[2].collidepoint(event.pos):
                            active = True
                            initial_deal = True
                            game_deck = copy.deepcopy(decks * one_deck)
                            player_hand = []
                            dealer_hand = []
                            game_outcome = 0
                            player_active = True
                            reveal_dealer = False
                            add_score = True
                            dealer_score = 0
                            player_score = 0
       
        if player_active and player_score >= 21:
            player_active = False
            reveal_dealer = True
        if game_outcome != 0 and add_score:               #Bet system conditions
            if game_outcome == 1:  
                player_money += int(bet_value)
            elif game_outcome == 2:  
                player_money -= int(bet_value)
            elif game_outcome ==3:
                pass
            add_score = False 

        game_outcome,add_score,player_money = condition_endgame(player_active, dealer_score, player_score, game_outcome, add_score,player_money,player_hand,dealer_hand)
        pygame.display.flip()
        time.sleep(0.7)
    pygame.quit()
main()
