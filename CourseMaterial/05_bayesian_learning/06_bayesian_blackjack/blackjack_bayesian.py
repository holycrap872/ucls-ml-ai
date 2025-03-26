#!/usr/bin/env python3
import random
import typing

MAX_GAMES = 10_000


class Card(typing.NamedTuple):
    value: int
    suite: str


class RoundResult(typing.NamedTuple):
    user_hand: int
    dealer_hand: int
    result: str


class GameData(typing.NamedTuple):
    user_hand: int
    dealer_shown: int
    user_hit: bool
    user_win: bool


def get_data() -> list[str]:
    with open("CourseMaterial/05_bayesian_learning/06_bayesian_blackjack/blackjack_data.csv") as bl_fp:
        return bl_fp.read().split("\n")[1:]


def parse_data(rows: list[str]) -> list[GameData]:
    acc: list[GameData] = []
    for row in rows:
        split = row.strip().split(",")
        if len(split) != 4:
            continue

        user_hand = int(split[0])
        dealer_shown = int(split[1])
        user_hit = "true" in split[2].lower()
        user_win = "true" in split[3].lower()

        gd = GameData(user_hand, dealer_shown, user_hit, user_win)
        acc.append(gd)

    return acc


def create_shuffled_deck() -> list[Card]:
    cards: list[Card] = []
    for suite in ["hearts", "diamonds", "clubs", "spades"]:
        for val in range(1, 14):
            cards.append(Card(val, suite))
    random.shuffle(cards)

    assert len(cards) == 52
    return cards


def calculate_hand_value(hand: list[Card]) -> int:
    assert len(hand) >= 1
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

    assert value >= 2
    return value


def get_win_percentage(data: list[GameData], user_val: int, dealer_val: int, *, is_hit: bool) -> float:
    win = 0
    lose = 0
    for game in data:
        if user_val == game.user_hand and dealer_val == game.dealer_shown and is_hit == game.user_hit:
            if game.user_win:
                win += 1
            else:
                lose += 1

    return win / (win + lose)


def should_hit(data: list[GameData], user_hand: list[Card], dealer_shows: Card) -> bool:
    user_val = calculate_hand_value(user_hand)
    dealer_val = calculate_hand_value([dealer_shows])

    if user_val < 12:
        return True

    if user_val > 17:
        return False

    hit_win_percent = get_win_percentage(data, user_val, dealer_val, is_hit=True)
    stand_win_percent = get_win_percentage(data, user_val, dealer_val, is_hit=False)

    should_hit = hit_win_percent > stand_win_percent
    return should_hit


def play_bayesian(data: list[GameData], deck: list[Card], user_hand: list[Card], dealer_shows: Card) -> int:
    while should_hit(data, user_hand, dealer_shows):
        user_hand.append(deck.pop())

    hand_val = calculate_hand_value(user_hand)
    return hand_val


def play_bot(deck: list[Card], hand: list[Card], max_value: int) -> int:
    while calculate_hand_value(hand) < max_value:
        hand.append(deck.pop())

    hand_val = calculate_hand_value(hand)
    return hand_val


def play_blackjack(data: list[GameData]) -> RoundResult:
    deck = create_shuffled_deck()

    user_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    user_val = play_bayesian(data, deck, user_hand, dealer_hand[0])

    if user_val <= 21:
        dealer_val = play_bot(deck, dealer_hand, 17)
    else:
        dealer_val = calculate_hand_value(dealer_hand)

    if user_val > 21:
        ret = "lose"
    elif dealer_val > 21:
        ret = "win"
    elif user_val == dealer_val:
        ret = "tie"
    elif user_val > dealer_val:
        ret = "win"
    else:
        ret = "lose"

    return RoundResult(user_val, dealer_val, ret)


if __name__ == "__main__":
    data = parse_data(get_data())

    wins = 0
    losses = 0
    for _ in range(MAX_GAMES):
        result = play_blackjack(data)
        if result.result == "win":
            wins += 1
        elif result.result == "lose":
            losses += 1
        print(result.result)

    win_percentage = wins / (wins + losses)
    print(win_percentage)
