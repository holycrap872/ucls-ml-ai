#!/usr/bin/env python3
import random
import typing

from matplotlib import pyplot as plots

MAX_GAMES = 10_000


class Card(typing.NamedTuple):
    value: int
    suite: str


class RoundResult(typing.NamedTuple):
    user_hand: int
    dealer_hand: int
    result: str


def create_shuffled_deck() -> list[Card]:
    cards: list[Card] = []
    for suite in ["hearts", "diamonds", "clubs", "spades"]:
        for val in range(1, 14):
            cards.append(Card(val, suite))
    random.shuffle(cards)

    assert len(cards) == 52
    return cards


def calculate_hand_value(hand: list[Card]) -> int:
    assert len(hand) >= 2
    value = 0
    ace_count = 0

    for card in hand:
        if card.value == 1:
            ace_count += 1
            value += 1
        elif card.value <= 9:
            value += card.value
        else:
            value += 10

    for _ in range(ace_count):
        if value + 10 <= 21:
            value += 10

    assert value >= 4
    return value


def play_bot(deck: list[Card], hand: list[Card], max_value: int) -> int:
    while calculate_hand_value(hand) < max_value:
        hand.append(deck.pop())

    hand_val = calculate_hand_value(hand)
    return hand_val


def play_blackjack(*, max_value: int) -> RoundResult:
    deck = create_shuffled_deck()

    user_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    bot_val = play_bot(deck, user_hand, max_value)

    if bot_val <= 21:
        dealer_val = play_bot(deck, dealer_hand, 17)
    else:
        dealer_val = calculate_hand_value(dealer_hand)

    if bot_val > 21:
        ret = "lose"
    elif dealer_val > 21:
        ret = "win"
    elif bot_val == dealer_val:
        ret = "tie"
    elif bot_val > dealer_val:
        ret = "win"
    else:
        ret = "lose"

    return RoundResult(bot_val, dealer_val, ret)


def plot_win_percentage(graph_x: list[int], graph_y: list[float]) -> None:
    plots.figure(figsize=(6, 6))
    plots.bar(x=graph_x, height=graph_y, color="red")
    plots.grid(True)
    plots.show()


if __name__ == "__main__":
    values_measured: list[int] = []
    win_percentage: list[float] = []

    for max_hit_val in range(3, 22):
        wins = 0
        for _ in range(MAX_GAMES):
            if play_blackjack(max_value=max_hit_val).result == "win":
                wins += 1

        values_measured += [max_hit_val]
        win_percentage += [wins / MAX_GAMES]

    print(win_percentage)
    plot_win_percentage(values_measured, win_percentage)
