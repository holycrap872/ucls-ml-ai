#!/usr/bin/env python3


def get_words(file_path: str) -> list[str]:
    with open(file_path, "r") as fd:
        text = fd.read()
        text = text.lower()
        text = text.replace("-", "")
        text = text.replace("'", "")
        text = text.replace("_", "")
        text = text.replace('"', "")
        text = text.replace("“", "")
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("&", "")
        text = text.replace("\n", " ")
        return text.split(" ")


def ingest(text_words: list[str]) -> dict[str, dict[str, int]]:
    ngram_map: dict[str, dict[str, int]] = {}
    prev_word = None

    for word in text_words:
        cur_word = word.strip().lower()
        if cur_word not in ngram_map:
            ngram_map[cur_word] = {}

        if prev_word:
            if prev_word not in ngram_map[cur_word]:
                ngram_map[cur_word][prev_word] = 0

            ngram_map[cur_word][prev_word] += 1

        prev_word = cur_word

    return ngram_map


def get_most_frequest_word_word(hit_map: dict[str, int]) -> str:
    max_hit = None
    max_word = None
    for word, ite in hit_map.items():
        if not max_hit or ite > max_hit:
            max_hit = ite
            max_word = word
    return max_word


def produce(ngram_map: dict[str, dict[str, int]], start_word: str, length: int) -> None:
    start_word = start_word.lower()
    for _ in range(0, length):
        sub_map = ngram_map[start_word]
        next_word = get_most_frequest_word_word(sub_map)

        print(start_word)
        start_word = next_word


if __name__ == "__main__":
    text_words = get_words("CourseMaterial/data/frankenstein.txt")
    ngram_map = ingest(text_words)
    produce(ngram_map, "Alive", 5)
