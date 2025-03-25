#!/usr/bin/env python3
import random
import typing


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


def get_card_str(card: Card) -> str:
    if card.value == 1:
        return f"Ace of {card.suite}"
    elif card.value == 13:
        return f"King of {card.suite}"
    elif card.value == 12:
        return f"Queen of {card.suite}"
    elif card.value == 11:
        return f"Jack of {card.suite}"
    else:
        return f"{card.value} of {card.suite}"


def get_hand_str(hand: list[Card]) -> str:
    ret = ""
    for card in hand:
        ret += get_card_str(card) + ", "
    return ret.strip().strip(",")


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


def is_yes_to_question(question: str) -> bool:
    assert question.endswith("?")

    while True:
        ans = input(question + " ")
        if ans.lower() == "n":
            return False
        elif ans.lower() == "y":
            return True
        else:
            print('''Sorry, I didn't get that, please answer with "y" or "n"''')


def play_user(deck: list[Card], hand: list[Card]) -> int:
    while calculate_hand_value(hand) < 21:
        print(f"Your hand: {get_hand_str(hand)}")
        is_hit = is_yes_to_question("Would you like to hit?")
        if not is_hit:
            break
        else:
            hand.append(deck.pop())

    hand_val = calculate_hand_value(hand)
    print(f"Your final hand: {get_hand_str(hand)} with a value of {hand_val}")
    return hand_val


def play_bot(deck: list[Card], hand: list[Card], max_value: int) -> int:
    print(f"Dealer hand: {get_hand_str(hand)}")
    while calculate_hand_value(hand) < max_value:
        hand.append(deck.pop())
        print(f"Dealer hits and gets a {get_card_str(hand[-1])}")

    hand_val = calculate_hand_value(hand)
    print(f"Dealer final hand: {get_hand_str(hand)} with a value of {hand_val}")
    return hand_val


def play_blackjack(*, max_value: typing.Optional[int] = None) -> RoundResult:
    deck = create_shuffled_deck()

    user_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Dealer shows: {get_card_str(dealer_hand[0])}")

    if max_value == None:
        user_val = play_user(deck, user_hand)
    else:
        user_val = play_bot(deck, user_hand, max_value)

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
    results = {"win": 0, "lose": 0, "tie": 0}
    rounds: list[RoundResult] = []
    while is_yes_to_question("Would you like to play a game of blackjack?"):
        print()
        round_result = play_blackjack()
        rounds.append(round_result)
        print(f"Result of game: {round_result.result}\n\n")
        results[round_result.result] += 1

    print(f"Final results: {results}")
    print("Thanks for playing!\n\n")

    while is_yes_to_question("Would you like to see the results of a particular round?"):
        round_index = int(input("Which round would you like to see? "))
        print(
            f"User final: {rounds[round_index].user_hand}, Dealer final: {rounds[round_index].dealer_hand}, Result: {rounds[round_index].result}"
        )
