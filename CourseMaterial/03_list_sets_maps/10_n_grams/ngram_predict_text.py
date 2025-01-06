#!/usr/bin/env python3
import random

N_GRAM_SIZE = 2


def get_text_words(file_path: str) -> list[str]:
    """
    :param file_path: Path to text to read
    :returns: The next normalized and split into tokens (words)
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

    # intense normalization
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


def create_n_gram(text: list[str], pos: int, n_gram_size: int) -> str:
    """
    Given a list of text, create an n-gram of a given size starting at a given
    position.

    :param text: Text to pull n-gram from
    :param pos: Position in the text to _start_ the n-gram
    :param n_gram_size: Size of the n-gram to create
    """
    n_gram_list = []
    for i in range(n_gram_size):
        n_gram_list.append(text[pos + i])
    return "-".join(n_gram_list)


def create_markov_graph(text_words: list[str], n_gram_size: int) -> dict[str, dict[str, int]]:
    """
    :param text_words: Ordered list of tokens (words) to create graph from
    :n_gram_size: Size of n-gram to use as a "node" in the graph
    :returns: Markov graph
    """
    markov_graph: dict[str, dict[str, int]] = {}

    for i in range(len(text_words) - n_gram_size):
        # Create "n-gram" for context
        gram_key = create_n_gram(text_words, i, n_gram_size)

        if gram_key not in markov_graph:
            markov_graph[gram_key] = {}

        next_word = text_words[i + n_gram_size]
        if next_word not in markov_graph[gram_key]:
            markov_graph[gram_key][next_word] = 0

        markov_graph[gram_key][next_word] += 1

    return markov_graph


def get_probabilistic_word(next_word_count_dict: dict[str, int]) -> str:
    """
    Given that an n-gram leads to a particular set of words with a different
    frequencies, randomly select the next word based proportionate to those
    frequencies.

    :param next_word_count_dict: A counting dictionary of the words that follow
        a particular n-gram and how often the occur.
    """
    choices = []
    for w, c in next_word_count_dict.items():
        for _ in range(c):
            choices.append(w)

    return random.choice(choices)


def traverse(markov_graph: dict[str, dict[str, int]], n_gram_size: int, input_words: list[str], length: int) -> None:
    """
    Given a markov graph, traverse the model to produce a "plausible sentence"
    up to a given length.

    :param markov_graph: The markov graph to traverse
    :param n_gram_size: The size of the n-grams the graph was created from
    :param input_words: The seed words to start the new, "plausible sentence"
    :param length: The length of the sentence to create
    """
    assert len(markov_graph) > 0
    assert len(input_words) == n_gram_size
    assert length > n_gram_size

    cur_n_gram = input_words.copy()
    produced_sentence = input_words.copy()

    for _ in range(0, length):
        n_gram_key = "-".join(cur_n_gram)
        sub_map = markov_graph[n_gram_key]
        next_word = get_probabilistic_word(sub_map)

        produced_sentence.append(next_word)
        cur_n_gram.append(next_word)
        cur_n_gram.pop(0)

    sentence = produced_sentence
    print(" ".join(sentence))


if __name__ == "__main__":
    text_words = get_text_words("CourseMaterial/data/frankenstein.txt")
    markov_graph = create_markov_graph(text_words, N_GRAM_SIZE)

    traverse(markov_graph, N_GRAM_SIZE, ["i", "am"], 15)
    traverse(markov_graph, N_GRAM_SIZE, ["who", "are"], 15)
