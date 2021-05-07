from krunfo import list_all_super_heroes, get_players_decks, compare_cards, play

def test_list_all_super_heroes():
    given_a_file_name = "super_heroes.csv"
    result = list_all_super_heroes(given_a_file_name)
    expected = [
    {'name': 'batman', 'intelligence': 10, 'power': 1, 'strenght': 6, 'agility': 6, 'vitality': 7},
    {'name': 'super man', 'intelligence': 7, 'power': 10, 'strenght': 10, 'agility': 10, 'vitality': 10},
    {'name': 'bat girl', 'intelligence': 8, 'power': 1, 'strenght': 4, 'agility': 8, 'vitality': 3},
    {'name': 'iron man', 'intelligence': 10, 'power': 1, 'strenght': 2, 'agility': 5, 'vitality': 5},
    {'name': 'huck', 'intelligence': 9, 'power': 7, 'strenght': 10, 'agility': 7, 'vitality': 10},
    {'name': 'thor', 'intelligence': 4, 'power': 9, 'strenght': 8, 'agility': 7, 'vitality': 8},
    {'name': 'spider man', 'intelligence': 7, 'power': 6, 'strenght': 5, 'agility': 9, 'vitality': 7},
    {'name': 'dr. strange', 'intelligence': 10, 'power': 9, 'strenght': 6, 'agility': 5, 'vitality': 8},
    {'name': 'captain marvel', 'intelligence': 6, 'power': 10, 'strenght': 8, 'agility': 10, 'vitality': 10},
    {'name': 'the thing', 'intelligence': 3, 'power': 6, 'strenght': 10, 'agility': 2, 'vitality': 10},
    {'name': 'storm', 'intelligence': 5, 'power': 10, 'strenght': 5, 'agility': 5, 'vitality': 6},
    {'name': 'wolverine', 'intelligence': 5, 'power': 8, 'strenght': 8, 'agility': 9, 'vitality': 10},
    {'name': 'beast', 'intelligence': 9, 'power': 6, 'strenght': 9, 'agility': 8, 'vitality': 10},
    {'name': 'black panther', 'intelligence': 6, 'power': 5, 'strenght': 6, 'agility': 10, 'vitality': 9},
    {'name': 'human torch', 'intelligence': 2, 'power': 10, 'strenght': 6, 'agility': 8, 'vitality': 8},
    {'name': 'thanos', 'intelligence': 9, 'power': 10, 'strenght': 10, 'agility': 7, 'vitality': 10}
    ]
    assert result == expected

def test_get_players_decks():
    given_a_card_list = [
    {'name': 'batman', 'intelligence': 10, 'power': 1, 'strenght': 6, 'agility': 6, 'vitality': 7},
    {'name': 'super man', 'intelligence': 7, 'power': 10, 'strenght': 10, 'agility': 10, 'vitality': 10},
    {'name': 'bat girl', 'intelligence': 8, 'power': 1, 'strenght': 4, 'agility': 8, 'vitality': 3},
    {'name': 'iron man', 'intelligence': 10, 'power': 1, 'strenght': 2, 'agility': 5, 'vitality': 5},
    {'name': 'huck', 'intelligence': 9, 'power': 7, 'strenght': 10, 'agility': 7, 'vitality': 10}
    ]
    result = get_players_decks(given_a_card_list)
    expected = None
    assert result == expected, "Amount of cards sould be even"

    given_a_card_list = [
    {'name': 'batman', 'intelligence': 10, 'power': 1, 'strenght': 6, 'agility': 6, 'vitality': 7},
    {'name': 'super man', 'intelligence': 7, 'power': 10, 'strenght': 10, 'agility': 10, 'vitality': 10},
    {'name': 'bat girl', 'intelligence': 8, 'power': 1, 'strenght': 4, 'agility': 8, 'vitality': 3},
    {'name': 'iron man', 'intelligence': 10, 'power': 1, 'strenght': 2, 'agility': 5, 'vitality': 5}
    ]
    result = get_players_decks(given_a_card_list)
    expected_type = tuple
    expected_length = 2
    assert type(result) == expected_type, "Should return a tuple"
    assert len(result) == expected_length, "Tuple should have 2 positions"

def test_compare_cards():
    given_player_a_card_atribute = {'name': 'Super Teste','intelligence': 8, 'power': 10}
    given_player_b_card_atribute = {'name': 'Capitão Teste', 'intelligence': 7,'power': 7}
    given_a_score = [0,0]
    result = compare_cards(given_player_a_card_atribute,given_player_b_card_atribute, given_a_score)
    expected = [1,0]
    assert result == expected, "Player One should win"

    given_player_a_card_atribute = {'name': 'Capitão Teste', 'intelligence': 7,'power': 7}
    given_player_b_card_atribute = {'name': 'Super Teste','intelligence': 8, 'power': 10}
    given_a_score = [0,0]
    result = compare_cards(given_player_a_card_atribute,given_player_b_card_atribute, given_a_score)
    expected = [0,1]
    assert result == expected, "Player Two should win"

    given_player_a_card_atribute = {'name': 'Capitão Teste', 'intelligence': 8,'power': 10}
    given_player_b_card_atribute = {'name': 'Super Teste','intelligence': 8, 'power': 10}
    given_a_score = [0,0]
    result = compare_cards(given_player_a_card_atribute,given_player_b_card_atribute, given_a_score)
    expected = [0,0]
    assert result == expected, "Should draw"

def test_play():
    given_a_card_list = [
    {'name': 'Super Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    {'name': 'Capitão Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    {'name': 'Mulher Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    {'name': 'Capitã Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    ]
    given_a_score = [0,0]
    result = play(given_a_card_list, given_a_score)
    expected = [0,0]
    assert result == expected, "Should draw"

    given_a_card_list = [
    {'name': 'Super Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    {'name': 'Capitão Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    {'name': 'Mulher Teste', 'intelligence': 7, 'power': 7, 'strenght': 7, 'agility': 7, 'vitality': 7},
    ]
    given_a_score = [0,0]
    result = play(given_a_card_list, given_a_score)
    expected = None
    assert result == expected, "Card list is odd, should return None"



    
