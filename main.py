import random


def display_welcome():
    print("\nWelcome to Player Pairs!")
    print("In this game the player will receive 5 cards.")
    print("Once each hand has been dealt, we will compare them to see who has the most pairs! \n")


def create_deck():
    deck = []
    card_types = ["Ace", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "Jack", "Queen", "King"]

    for type in card_types:
        for number in range(4):
            deck.append(type)

    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    shuffled = deck
    return shuffled


def deal_cards(deck, number_of_players):
    player_hands = []
    range_counter = 0
    for number in range(number_of_players):
        player_hands.append(deck[range_counter:range_counter + 5])
        range_counter += 5

    return player_hands


def determine_pairs(player_hands):
    pairs_result = {
        "all_pairs": []
    }
    player_number = 1
    for hand in player_hands:
        duplicates = {x for x in hand if hand.count(x) > 1}
        pairs_result[f"Player {player_number}"] = {
            "hand": hand,
            "pairs": len(duplicates)
        }
        pairs_result["all_pairs"].append(len(duplicates))
        player_number += 1
    return pairs_result


def show_hand_results(pairs_result, result):
    for key in pairs_result:
        print(key)
        print(f"Hand: {', '.join(pairs_result[key]['hand'])}")
        print(f"Number of Pairs: {pairs_result[key]['pairs']}\n")

    print(f"{result}")


def determine_winner_or_ties(pairs_result):
    current_winner = ""
    all_zeroes = len(
        list(filter(lambda item: item != 0, pairs_result["all_pairs"]))) == 0
    pairs_result["all_pairs"].sort()
    highest_pair_count = pairs_result["all_pairs"].pop()
    highest_repeated = highest_pair_count in pairs_result["all_pairs"]
    del pairs_result["all_pairs"]

    if not highest_repeated:
        for key in pairs_result:
            if pairs_result[key]["pairs"] == highest_pair_count:
                current_winner = f"{key} wins!"
    elif all_zeroes:
        current_winner = "No pairs this round!"
    else:
        current_winner = "Tied between: "
        for key in pairs_result:
            if pairs_result[key]["pairs"] == highest_pair_count:
                current_winner += f"{key} "

    return current_winner


def run_player_pairs(number_of_players, number_of_rounds):
    display_welcome()
    for i in range(number_of_rounds):
        deck = create_deck()
        shuffled_deck = shuffle_deck(deck)
        player_hands = deal_cards(shuffled_deck, number_of_players)
        pairs_result = determine_pairs(player_hands)
        winner = determine_winner_or_ties(pairs_result)
        print(f"Round {i + 1} Results: \n")
        show_hand_results(pairs_result, winner)
        input("Press enter to continue!")
    else:
        print("Game complete!")


run_player_pairs(5, 2)
