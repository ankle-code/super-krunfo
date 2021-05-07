from csv import DictReader
from random import shuffle, randint

def list_all_super_heroes(filename: str) -> list:
    super_heroes = []
    with open(filename) as f:
        reader = DictReader(f)
        for super_hero in reader:
            super_hero_formated = {**super_hero, 'intelligence': int(super_hero['intelligence']), 'power': int(super_hero['power']), 'strenght': int(super_hero['strenght']), 'agility': int(super_hero['agility']), 'vitality': int(super_hero['vitality'])}
            super_heroes.append(super_hero_formated)
    return super_heroes

def get_players_decks(card_list: list) -> tuple:
    if len(card_list) % 2 != 0:
        return None

    shuffle(card_list)
    middle_of_deck = int(len(card_list) / 2)

    deck_player_one = card_list[: middle_of_deck]
    deck_player_two = card_list[middle_of_deck:]
    return (deck_player_one, deck_player_two)

def compare_cards(player_a_card, player_b_card, score):
    random_choice = randint(1 , len(player_a_card) -1)
    chosen_atribute = [atribute[1][0] for atribute in enumerate(player_a_card.items()) if atribute[0] == random_choice][0]

    print(f"WHO has more {chosen_atribute.upper()} ????? :0\n")
    
    if  player_a_card[chosen_atribute] > player_b_card[chosen_atribute]:
        score[0] += 1

    if  player_b_card[chosen_atribute] > player_a_card[chosen_atribute]:
        score[1] += 1

    return score
    
def play(card_list, score):
    players_deck = get_players_decks(card_list)

    if not players_deck:
        return None

    deck_size = len(players_deck[0])
    player_one_deck = players_deck[0]
    player_two_deck = players_deck[1]

    for comparation in range(deck_size):
        print(f"\n\n{comparation + 1}# BATTLE:\n")
        score = compare_cards(player_one_deck[comparation], player_two_deck[comparation], score)
        print(f"{player_one_deck[comparation]['name']}\n-----VS-----\n{player_two_deck[comparation]['name']}\n")
        print(f"Player ONE: {score[0]}\nPlayer TWO: {score[1]}")
        print("_____________")

    print(f"\nFINAL SCORE:\n\nPlayer ONE: {score[0]}\nPlayer TWO: {score[1]}")
    return score

play(list_all_super_heroes("super_heroes.csv"), [0,0])


    