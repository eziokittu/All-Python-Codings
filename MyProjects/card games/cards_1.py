import random

# Defining some variables
card_types = ["S", "C", "H", "D"]
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 'X', 'J', 'Q', 'K', 'A']
card_set = []
for i in card_types:
    for j in card_values:
        card_set.append(i+str(j))
centre_length = 70

def print_AllCards():
    '''prints all the 52 cards in the card game'''
    print("\nPrinting all the cards --")
    for i in range(len(card_types)):
        for j in range(len(card_values)):
            print(card_set[(i*len(card_values))+j], end = " ")

def print_player_cards(cards):
    '''prints all the 13 cards in the card game for the player(user)'''
    print("\nYour Cards -- ", end="")
    for card in cards:
        print(card, end=" ")

def cards_shuffle():
    '''returns a list of shuffled cards'''
    global card_set
    random.shuffle(card_set)
    return card_set

def cards_distribute_among_players():
    '''return a list consisting of 4 lists of 13 cards each for each of the 4 players'''
    global card_set
    p0 = [] # for the player
    p1 = [] # bot-1
    p2 = [] # bot-2
    p3 = [] # bot-3
    for i in range(len(card_set)):
        if i%(len(card_types))==0:
            p0.append(card_set[i])
        elif i%(len(card_types))==1:
            p1.append(card_set[i])
        elif i%(len(card_types))==2:
            p2.append(card_set[i])
        elif i%(len(card_types))==3:
            p3.append(card_set[i])
    return [p0, p1, p2, p3]

def game_instructions(state, *lis):
    '''Intrustions of the game'''
    global centre_length
    if state == 0:
        '''Welcome'''
        print("Welcome to 52-Cards 'Callbreak' Game!".center(centre_length))
    if state == 1:
        '''rules are defined here'''
        pass
    # for each round
    if state == 2:
        print(f" Round-{lis[0]} ".center(centre_length))
        pass

def game_ask_for_another_game():
    '''asks the player to input 'y' for YES or 'n' for NO - is the player wants to play another game. returns a BOOLEAN (True for YES)'''
    global centre_length
    print("\n"+"".center(centre_length, "-"))
    print("Do you want to play another Callbreak game?")
    print("Type 'y' for YES and 'n' for NO  --  ", end="")
    try:
        myInput = input()
        if (myInput.lower() == 'y'):
            print("\n"+"".center(centre_length, "-"))
            print(" Starting a new Callbreak game! ".center(centre_length, "-"))
            print("".center(centre_length, "-"))
            return True
        if (myInput.lower() == 'n'):
            print("\n"+"".center(centre_length, "-"))
            print(" Okay bye play again soon! ".center(centre_length, "-"))
            print("".center(centre_length, "-"))
            print("")
            return False
        else:
            print("[WRONG INPUT]")
            game_ask_for_another_game()
    except:
        print("[WRONG INPUT]")
        game_ask_for_another_game()

def cards_get_possible_cards(cards_in_hand, card_type):
    '''returns the list of possible_cards in the available card set of that card type'''
    global card_values
    cards = cards_in_hand
    cards_possible = []
    card_to_return = ["S",2] # since 2 is the minimum value
    # when the same card_type is available in card_in_hand
    for card in cards:
        if card[0] == card_type:
            cards_possible.append(card)
            cards.remove(card)
    # if len(cards_possible)>=1:
    #     for card in cards_possible:
    #         if cards_get_card_value(card)>=cards_get_card_value(card_to_return):
    #             card_to_return = card
    # when the same card_type (other than spade) is not available in card_in_hand but spade is there
    if len(cards_possible)==0 and card_type != "S":
        for card in cards:
            if card[0] == "S":
                cards_possible.append(card)
                cards.remove(card)
    # when noting is available random card is given

    return card_to_return

def cards_get_highest_card(cards_possible):
    '''returns the highest card in the possible_cards list'''
    highest_card = cards_possible[0]
    for card in cards_possible:
        if cards_get_card_value(card) > cards_get_card_value(highest_card):
            highest_card = card
    return highest_card

def cards_get_lowest_card(cards_possible):
    '''returns the lowest card in the possible_cards list'''
    lowest_card = cards_possible[0]
    for card in cards_possible:
        if cards_get_card_value(card) < cards_get_card_value(lowest_card):
            lowest_card = card
    return lowest_card

def cards_get_card_value(card):
    '''returns INTEGER values ranging from 1,2,....13 based of card, where ACE = 13, King = 12, ...'''
    print("[DEBUG] 1")
    global card_values
    v = card[1]
    print("[DEBUG] 2")
    if v in card_values:
        print("HEHEHHEHEHHEEH")
        if v == 'A':
            return 13
        elif v == 'K':
            return 12
        elif v == 'Q':
            return 11
        elif v == 'J':
            return 10
        elif v == 'X':
            return 9
        else:
            return (int(v)-1)
    else:
        print("'cards_get_card_value' ERROR, card =", card)
        return 0

def game_bots_drop_a_card(cards_in_hand, *cards_dropped_till_now):
    '''on each round, the 3 bots drop the suitable card'''
    # when no cards are dropped till now
    if len(cards_dropped_till_now) == 0:
        card_index = random.randint(0,12)
        return cards_in_hand(card_index)
    # when there are cards dropped previously in that round
    else:
        cards_possible = cards_get_possible_cards(cards_in_hand, cards_dropped_till_now[0][0])
        # no cards available of same type, we check for spade
        if len(cards_possible) == 0:
            cards_possible = cards_get_possible_cards(cards_in_hand, 'S')
            # still no cards possible 
            if cards_possible == 0:
                card_index = random.randint(0,len(cards_in_hand)-1)
                return cards_in_hand(card_index)
            # spade cards are possible we check value
            else:
                return cards_get_highest_card(cards_possible)
        # cards are available of the same type
        elif len(cards_possible) > 0:
            return cards_get_highest_card(cards_possible)

def game_ask_player_to_drop_a_card(cards):
    '''user input to type the card to be dropped for the round'''
    print("Drop a card : ", end = "")
    my_card = input()
    # checking if the cord is valid or not
    if my_card in cards:
        print("[DEBUG] 4 ", my_card)
        return str(my_card)
    else:
        print("[Wrong Card Format / Card not available] Try Again")
        game_ask_player_to_drop_a_card(cards)

def game_find_highest_card_value(cards_dropped):
    '''returns the INTEGER index of highest value card - index so that a player or bot can win'''
    highest_card = cards_dropped[0]
    for card in cards_dropped:
        if highest_card[0] == card[0] and cards_get_card_value(card)>cards_get_card_value(highest_card):
            highest_card = card
        elif highest_card[0] != card[0] and card[0]=='S':
            highest_card = card
    for i in range(len(cards_dropped)):
        if highest_card == cards_dropped[i]:
            return i

def game_give_score_to_players(player_index):
    '''gives player scores based on player index who won last round'''
    global player_scores
    player_scores[player_index]+=1

def game_round(round):
    '''for each round returns some instructions and asks each player to drop a card based on last round winner.
    The starting round is always started by the player.'''
    print(f" ROUND - {round} ".center(centre_length,"-"))
    global player_cards
    global player_won_last_round
    cards_dropped = []
    if round == 1:
        # for player 0
        card_dropped = game_ask_player_to_drop_a_card(player_cards[0])
        print("[DEBUG] 3 ", card_dropped)
        player_cards[0].remove(card_dropped)
        cards_dropped.append(card_dropped)
        # For player 1
        card_dropped = game_bots_drop_a_card(player_cards[1], cards_dropped)
        player_cards[1].remove(card_dropped)
        cards_dropped.append(card_dropped)
        # For player 2
        card_dropped = game_bots_drop_a_card(player_cards[2], cards_dropped)
        player_cards[2].remove(card_dropped)
        cards_dropped.append(card_dropped)
        # For player 3
        card_dropped = game_bots_drop_a_card(player_cards[3], cards_dropped)
        player_cards[3].remove(card_dropped)
        cards_dropped.append(card_dropped)
        
        player_won_last_round = game_find_highest_card_value(cards_dropped)
        game_give_score_to_players(player_won_last_round)

    else:
        pass


if __name__ == "__main__":
    game_instructions(0)
    game_is_running = True
    while game_is_running:
        
        print("Playing game")
        cards_shuffle()
        # all the list of cards for wach player, p0, p1, p2, p3, where p0 is the player(user) and others are for bots
        player_cards = cards_distribute_among_players()
        # printing the player cards
        print_player_cards(player_cards[0])
        # which player has won last round. By default p0 has won
        player_won_last_round = 0
        # player scores
        player_scores = [0,0,0,0]

        # 13 rounds will go on and the game will end with a scoreboard
        round = 1
        while round<=13:
            game_round(round)

        game_is_running = game_ask_for_another_game()