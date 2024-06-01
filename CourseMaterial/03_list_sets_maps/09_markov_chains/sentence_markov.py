#!/usr/bin/env python3
import random


def create_markov_graph(sentence: str) -> dict[str, set[str]]:
    markov_dict: dict[str, set[str]] = {}

    cur_char = "^"
    for next_char in sentence:
        if cur_char not in markov_dict:
            markov_dict[cur_char] = set()

        markov_dict[cur_char].add(next_char)
        cur_char = next_char

    if cur_char not in markov_dict:
        markov_dict[cur_char] = set()
    markov_dict[cur_char].add("$")

    return markov_dict


def produce_string(markov_dict: dict[str, set[str]], str_len: int) -> None:
    cur_char = "e"
    new_string = "e"
    while cur_char != "$" and len(new_string) < str_len:
        cur_char = random.sample(list(markov_dict[cur_char]), 1)[0]
        new_string += cur_char

    print(new_string)


if __name__ == "__main__":
    mg = create_markov_graph("helloeveryonethere")
    print(mg)
    produce_string(mg, 5)
