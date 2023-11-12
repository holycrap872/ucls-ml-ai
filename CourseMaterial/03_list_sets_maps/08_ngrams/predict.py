#!/usr/bin/env python3
import random


def get_words(file_path: str) -> list[str]:
    with open(file_path, "r") as fd:
        text = fd.read()
        text = text.lower()
        text = text.replace("-", "")
        text = text.replace("'", "")
        text = text.replace("_", "")
        text = text.replace(",", "")
        text = text.replace('"', "")
        text = text.replace("“", "")
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("&", "")
        text = text.replace("”", "")
        text = text.replace("\n", " ")
        split_text = text.split(" ")

    ret = []
    for word in split_text:
        w = ""
        for c in word:
            if c.isalpha():
                w += c
        ret.append(w.strip().lower())
    return ret


def ingest(text_words: list[str]) -> dict[str, dict[str, int]]:
    ngram_map: dict[str, dict[str, int]] = {}

    for i in range(len(text_words) - 3):
        word_0 = text_words[i]
        word_1 = text_words[i + 1]
        word_2 = text_words[i + 2]

        n_gram = "-".join([word_0, word_1, word_2])
        if n_gram not in ngram_map:
            ngram_map[n_gram] = {}

        next_word = text_words[i + 3]
        if next_word not in ngram_map[n_gram]:
            ngram_map[n_gram][next_word] = 0

        ngram_map[n_gram][next_word] += 1

    return ngram_map


def get_probabilistic_word(hit_map: dict[str, int]) -> str:
    choices = []
    for w, c in hit_map.items():
        for _ in range(c):
            choices.append(w)

    return random.choice(choices)


def produce(ngram_map: dict[str, dict[str, int]], input_gram: list[str], length: int) -> None:
    start_gram = input_gram.copy()

    sentence = []
    for _ in range(0, length):
        sub_map = ngram_map["-".join(start_gram)]
        print(sub_map)
        next_word = get_probabilistic_word(sub_map)

        sentence.append(next_word)
        start_gram.append(next_word)
        start_gram.pop(0)

    sentence = input_gram + sentence
    print(" ".join(sentence))


if __name__ == "__main__":
    text_words = get_words("CourseMaterial/data/frankenstein.txt")
    text_words += get_words("CourseMaterial/data/dracula.txt")
    text_words += get_words("CourseMaterial/data/little_women.txt")
    ngram_map = ingest(text_words)
    produce(ngram_map, ["i", "am", "feeling"], 15)
