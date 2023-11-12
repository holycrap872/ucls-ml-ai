#!/usr/bin/env python3
import random
import typing


class GameRecord(typing.NamedTuple):
    user_val: int
    dealer_val: int
    did_hit: bool
    result_won: bool


WIN_MEMORY: list[GameRecord] = []


def is_win(user_val: int, dealer_val: int) -> bool:
    assert user_val != dealer_val
    if user_val > 21:
        return False
    elif dealer_val > 21:
        return True
    elif user_val > dealer_val:
        return True
    else:
        return False


def add_to_memory(user_hand: list[str], orig_dealer_val: int, result_won: bool) -> None:
    """
    Memory:
    17, 13, hit, lost
    """
    if len(user_hand) > 2:
        hand = user_hand[:-1]
        WIN_MEMORY.append(GameRecord(get_hand_value(hand), orig_dealer_val, did_hit=True, result_won=result_won))

    WIN_MEMORY.append(GameRecord(get_hand_value(user_hand), orig_dealer_val, did_hit=False, result_won=result_won))


def new_shuffled_deck() -> list[str]:
    deck = []
    for suit in ["heart", "diamond", "spade", "club"]:
        deck += [f"{i}-{suit}" for i in range(2, 13)]
    random.shuffle(deck)
    return deck


def get_hand_value(hand: list[str]) -> int:
    cards = [int(c.split("-")[0]) for c in hand]
    cards.sort()

    val = 0
    for card in cards:
        if card == 14:
            if val > 10:
                val += 1
            else:
                val += 11
        elif 11 <= card <= 13:
            val += 10
        else:
            val += card
    return val


def should_hit(user_hand: list[str], dealer_val: int) -> bool:
    user_val = get_hand_value(user_hand)
    matches = [gr for gr in WIN_MEMORY if gr.user_val == user_val and gr.dealer_val == dealer_val]

    win_hits = 0
    total_hits = 0
    win_stays = 0
    total_stays = 0
    for gr in matches:
        if gr.did_hit:
            total_hits += 1
            if gr.result_won:
                win_hits += 1
        else:
            total_stays += 1
            if gr.result_won:
                win_stays += 1

    if total_hits < 10 or total_stays < 10:
        return bool(random.randint(0, 100) % 2 == 0)

    return (win_hits / total_hits) > (win_stays / total_stays)


if __name__ == "__main__":
    total_wins = 0
    plays = 0
    win_array = []

    for i in range(20_000):
        deck = new_shuffled_deck()

        user_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        orig_dealer_val = get_hand_value(dealer_hand)

        while True:
            user_val = get_hand_value(user_hand)
            if user_val > 21:
                break
            if user_val <= 10:
                # always hit
                pass
            if not should_hit(user_hand, orig_dealer_val):
                break

            user_hand.append(deck.pop())
        user_val = get_hand_value(user_hand)

        while user_val <= 21 and get_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        dealer_val = get_hand_value(dealer_hand)

        if user_val > 21 and dealer_val > 21 or user_val == dealer_val:
            print("Push")
            continue

        result_won = is_win(user_val, dealer_val)
        add_to_memory(user_hand, orig_dealer_val, result_won)

        plays += 1
        if result_won:
            total_wins += 1

        if plays % 1000 == 0:
            win_array.append(total_wins / plays)
            total_wins = 0
            plays = 0

    WIN_MEMORY.sort(key=lambda e: (e.user_val, e.dealer_val))
    for x in WIN_MEMORY:
        print(f"{x.user_val}, {x.dealer_val}, {x.did_hit}, {x.result_won}")

    print("Win percentage: ", win_array)
