#!/usr/bin/env python3
import random


def sentence_markov(sentence: str) -> None:
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
    print(markov_dict)

    cur_char = "e"
    while cur_char != "$":
        print(cur_char)
        cur_char = random.sample(markov_dict[cur_char], 1)[0]


if __name__ == "__main__":
    sentence_markov("helloeveryonethere")
