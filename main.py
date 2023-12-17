import random
import os


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ten_scores = ["Jack", "Queen", "King", 10]
removed_cards = []


def add_card(deck):
    random_card = random.choice(cards)
    if random_card == 10:
        display_card = random.choice(ten_scores)
    elif random_card == 11:
        display_card = "Ace"
    else:
        display_card = random_card
    deck.append(random_card)
    cards.remove(random_card)
    removed_cards.append(random_card)
    return display_card


def calculate_score(deck):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack():
    print(logo)
    players_cards = []
    computers_cards = []
    player_display = []
    computer_display = []
    for _ in range(2):
        player_display.append(add_card(players_cards))
        computer_display.append(add_card(computers_cards))
    computers_score = calculate_score(computers_cards)
    players_score = calculate_score(players_cards)
    is_game_over = False
    while not is_game_over:
        players_score = calculate_score(players_cards)
        computers_score = calculate_score(computers_cards)
        players_score_display = players_score
        if players_score == 0:
            players_score_display = 21
        print(f"   Your cards: {player_display}, current score: {players_score_display}")
        print(f"   Computer's first card: {computer_display[0]}")
        if players_score == 0 or computers_score == 0 or players_score > 21:
            is_game_over = True
        else:
            more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
            if more_cards == "y":
                player_display.append(add_card(players_cards))
                continue
            else:
                is_game_over = True
    while computers_score != 0 and computers_score < 17:
        computer_display.append(add_card(computers_cards))
        computers_score = calculate_score(computers_cards)
    computers_score_display = computers_score
    if computers_score == 0:
        computers_score_display = 21
    players_score_display = players_score
    if players_score == 0:
        players_score_display = 21
    print(f"\nYour cards: {player_display}, Your final score: {players_score_display}")
    print(f"Computer's cards: {computer_display}, computer's final score: {computers_score_display}")
    print(compare(players_score, computers_score))


clear = lambda: os.system('cls')
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    for card in removed_cards:
        cards.append(card)
    blackjack()
