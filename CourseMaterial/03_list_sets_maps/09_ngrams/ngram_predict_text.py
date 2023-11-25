#!/usr/bin/env python3
import random


def get_text_words(file_path: str) -> list[str]:
    """
    :param file_path: Path to text to read
    :returns: The text split into tokens (words)
    """
    with open(file_path, "r") as fd:
        text = fd.read()
        text = text.lower()
        text = text.replace("-", " ")
        text = text.replace("'", "")
        text = text.replace("_", "")
        text = text.replace(",", "")
        text = text.replace('"', "")
        text = text.replace("“", "")
        text = text.replace("”", "")
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("&", "")
        text = text.replace("”", "")
        text = text.replace(";", "")
        text = text.replace("\n", " ")
        split_text = text.split(" ")

    ret: list[str] = []
    for word in split_text:
        w = ""
        for c in word:
            if c.isalpha():
                w += c
        w = w.strip().lower()
        if len(w) > 0:
            ret.append(w)
    return ret


def create_markov_graph(text_words: list[str]) -> dict[str, dict[str, int]]:
    """
    :param text_words: Ordered list of tokens (words) to create graph from
    :returns: Markov graph
    """
    markov_graph: dict[str, dict[str, int]] = {}

    for i in range(len(text_words) - 3):
        # Create "tri-gram" for context
        word_0 = text_words[i]
        word_1 = text_words[i + 1]
        word_2 = text_words[i + 2]

        trigram_key = "-".join([word_0, word_1, word_2])
        if trigram_key not in markov_graph:
            markov_graph[trigram_key] = {}

        next_word = text_words[i + 3]
        if next_word not in markov_graph[trigram_key]:
            markov_graph[trigram_key][next_word] = 0

        markov_graph[trigram_key][next_word] += 1

    return markov_graph


def get_probabilistic_word(hit_map: dict[str, int]) -> str:
    choices = []
    for w, c in hit_map.items():
        for _ in range(c):
            choices.append(w)

    return random.choice(choices)


def produce(markov_graph: dict[str, dict[str, int]], input_words: list[str], length: int) -> None:
    assert len(markov_graph) > 0
    assert len(input_words) == 3
    assert length > 3

    cur_trigram = input_words.copy()

    produced_sentence = []
    for _ in range(0, length):
        trigram_key = "-".join(cur_trigram)
        sub_map = markov_graph[trigram_key]
        next_word = get_probabilistic_word(sub_map)

        produced_sentence.append(next_word)
        cur_trigram.append(next_word)
        cur_trigram.pop(0)

    sentence = input_words + produced_sentence
    print(" ".join(sentence))


if __name__ == "__main__":
    text_words = get_text_words("CourseMaterial/data/dracula.txt")
    text_words += get_text_words("CourseMaterial/data/frankenstein.txt")
    text_words += get_text_words("CourseMaterial/data/great_gatsby.txt")
    text_words += get_text_words("CourseMaterial/data/little_women.txt")
    text_words += get_text_words("CourseMaterial/data/oliver_twist.txt")
    text_words += get_text_words("CourseMaterial/data/pride_and_prejudice.txt")
    text_words += get_text_words("CourseMaterial/data/robert_frost.txt")
    text_words += get_text_words("CourseMaterial/data/the_time_machine.txt")
    markov_graph = create_markov_graph(text_words)

    produce(markov_graph, ["i", "am", "feeling"], 15)
    produce(markov_graph, ["who", "are", "you"], 15)
