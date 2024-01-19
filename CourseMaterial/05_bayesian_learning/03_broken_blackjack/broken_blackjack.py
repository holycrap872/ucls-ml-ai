import random


def create_deck() -> list[int]:
    suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    for suite in suites:
        deck += [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

    return deck


def shuffle_deck(deck: list[int]) -> None:
    random.shuffle(deck)


def draw_card(deck: list):
    return deck.pop()


def calculate_hand_value(hand: list[int]) -> int:
    value = 0
    ace_count = 0

    for card_value in hand:
        if card_value == 11:
            ace_count += 1
            value += 1
        else:
            value += card_value

    for _ in range(ace_count):
        if value + 10 <= 21:
            value += 10

    return value


def show_hand(hand: list[int]) -> None:
    for card in hand:
        print(card)


def bot_turn(deck, bot_hand: list):
    hand_value = calculate_hand_value(bot_hand)

    while hand_value < 17:
        bot_hand.append(draw_card(deck))
        print("\nBot's Hand:")
        show_hand(bot_hand)
        hand_value = calculate_hand_value(bot_hand)  # Update hand_value
        print("Total value:", hand_value)

        if hand_value > 21:
            print("\nBot busts! Dealer wins!")
            return "dealer"

    return None


# if a user input is necessary, call this function
def play_player_turn(deck, player_hand: list):
    while True:
        choice = input("\nDo you want to Hit or Stand? Enter 'h' or 's': ")
        if choice.lower() == "h":
            player_hand.append(draw_card(deck))
            print("\nPlayer's Hand:")
            show_hand(player_hand)
            print("Total value:", calculate_hand_value(player_hand))

            if calculate_hand_value(player_hand) > 21:
                print("\nPlayer busts! Dealer wins!")
                return "dealer"

        elif choice.lower() == "s":
            break

        else:
            print("Please enter 'h' or 's' only.")
    return None


def track_wins(winner, wins: dict[str, int]) -> None:
    if winner == "player":
        wins["player"] += 1
    elif winner == "dealer":
        wins["dealer"] += 1
    else:
        wins["tie"] += 1


def print_wins(wins: dict[str, int]) -> None:
    print("Total Wins:")
    print("Player:", wins["player"])
    print("Dealer:", wins["dealer"])
    print("Tie:", wins["tie"])


def dealer_turn(deck: list[str], dealer_hand: list) -> None:
    print("\nDealer's Hand:")
    show_hand(dealer_hand)

    while calculate_hand_value(dealer_hand) < 17:
        card = deck.pop()
        dealer_hand.append(card)

    print("Dealer's Hand:")
    show_hand(dealer_hand)
    print("Total value:", calculate_hand_value(dealer_hand))


# this is where to change bot vs. user input
def play_round(deck, player_hand: list[int], dealer_hand: list[int]):
    shuffle_deck(deck)

    print("\nPlayer's Hand:")
    show_hand(player_hand)
    print("Total value:", calculate_hand_value(player_hand))

    print("\nDealer's Hand:")
    show_hand(dealer_hand)
    print("Total value:", calculate_hand_value(dealer_hand))

    if calculate_hand_value(player_hand) > 21:
        print("\nPlayer busts! Dealer wins!")
        return "dealer"
    elif calculate_hand_value(dealer_hand) > 21:
        print("\nDealer busts! Player wins!")
        return "player"
    elif calculate_hand_value(player_hand) == calculate_hand_value(dealer_hand):
        print("\nIt's a tie! Push.")
        return "tie"

    else:
        player_result = play_player_turn(deck, player_hand)  # Updated line

        if player_result == "dealer":
            return "dealer"

        if calculate_hand_value(player_hand) <= 21:
            while calculate_hand_value(dealer_hand) <= 17:
                dealer_hand.append(draw_card(deck))

            print("\nDealer's Hand:")
            show_hand(dealer_hand)
            print("Total value:", calculate_hand_value(dealer_hand))

            if calculate_hand_value(dealer_hand) > 21:
                print("\nDealer busts! Player wins!")
                return "player"
            elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
                print("\nDealer wins!")
                return "dealer"
            elif calculate_hand_value(dealer_hand) < calculate_hand_value(player_hand):
                print("\nPlayer wins!")
                return "player"
            else:
                print("\nIt's a tie! Push.")
                return "tie"


def play_blackjack():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Deal initial hands
    player_hand.append(draw_card(deck))
    dealer_hand.append(draw_card(deck))
    player_hand.append(draw_card(deck))
    dealer_hand.append(draw_card(deck))

    # Shuffle the deck after dealing initial hands

    return (deck, player_hand, dealer_hand)


if __name__ == "__main__":
    print("Welcome to Blackjack! Get as close to 21 as you can without going over.")

    wins = {"player": 0, "dealer": 0, "tie": 0}

    for _ in range(3000):
        winner = play_blackjack()
        track_wins(winner, wins)

    print("\nFinal Wins:")
    print_wins(wins)

    bot_win_percentage = (wins["player"] / 100) * 100
    print("\nBot Win Percentage:", bot_win_percentage, "%")
