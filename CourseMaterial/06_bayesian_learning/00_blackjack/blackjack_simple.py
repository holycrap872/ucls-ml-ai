#!/usr/bin/env python3
import random
import typing

from matplotlib import pyplot as plots

MAX_GAMES = 1000


def create_shuffled_deck() -> list[int]:
    cards = []
    for _ in range(4):
        cards += [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    random.shuffle(cards)

    assert len(cards) == 52
    return cards


def calculate_hand_value(hand: list[int]) -> int:
    assert len(hand) >= 2
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

    assert value >= 4
    return value


def is_yes_to_question(question: str) -> bool:
    assert question.endswith("?")

    while True:
        ans = input(question + " ")
        if ans.lower() == "n":
            return False
        elif ans.lower() == "y":
            return True
        else:
            print('sorry, i didn\'t get that, please answer with "y" or "n"')


def play_user(deck: list[int], hand: list[int]) -> int:
    while calculate_hand_value(hand) < 21:
        print(f"Your hand: {hand}")
        is_hit = is_yes_to_question("Would you like to hit?")
        if not is_hit:
            break
        else:
            hand.append(deck.pop())

    hand_val = calculate_hand_value(hand)
    print(f"Your final hand: {hand} with a value of {hand_val}")
    return hand_val


def play_bot(deck: list[int], hand: list[int], max_value: int) -> int:
    print(f"Dealer hand: {hand}")
    while calculate_hand_value(hand) < max_value:
        hand.append(deck.pop())

    hand_val = calculate_hand_value(hand)
    print(f"Dealer final hand: {hand} with a value of {hand_val}")
    return hand_val


def play_blackjack(*, max_value: typing.Optional[int] = None) -> str:
    deck = create_shuffled_deck()

    user_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Dealer shows a {dealer_hand[0]}")

    if max_value == None:
        user_val = play_user(deck, user_hand)
    else:
        user_val = play_bot(deck, user_hand, max_value)

    dealer_val = play_bot(deck, dealer_hand, 17)

    if user_val > 21:
        return "lose"
    elif dealer_val > 21:
        return "win"
    elif user_val == dealer_val:
        return "tie"
    elif user_val > dealer_val:
        return "win"
    else:
        return "lose"


if __name__ == "__main__":
    results = {"win": 0, "lose": 0, "tie": 0}
    while is_yes_to_question("Would you like to play a game of blackjack?"):
        result = play_blackjack()
        print(f"Result of game: {result}")
        results[result] += 1

    print(f"Final results: {results}")
    print("Thanks for playing!")


def plot_win_percentage(graph_x: list[int], graph_y: list[float]) -> None:
    plots.figure(figsize=(6, 6))
    plots.bar(x=graph_x, height=graph_y, color="red")
    plots.grid(True)
    plots.show()


if __name__ == "__main__":
    values_measured = []
    win_percentage = []

    for max_hit_val in range(12, 22):
        wins = 0
        for _ in range(MAX_GAMES):
            if play_blackjack(max_value=max_hit_val) == "win":
                wins += 1

        values_measured += [max_hit_val]
        win_percentage += [wins / MAX_GAMES]

    plot_win_percentage(values_measured, win_percentage)
