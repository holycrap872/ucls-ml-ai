#!/usr/bin/env python3
import random

import matplotlib.pyplot as plt
import networkx as nx

SAID_WORDS = set()


def get_words(file_path: str) -> list[str]:
    with open(file_path, "r") as fd:
        text = fd.read()
        text = text.lower()
        text = text.replace("-", " ")
        text = text.replace("'", "")
        text = text.replace("_", "")
        text = text.replace(",", " ")
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


def get_most_frequest_word(hit_map: dict[str, int]) -> str:
    max_hit = None
    max_word = None
    for word, ite in hit_map.items():
        if not max_hit or ite > max_hit:
            max_hit = ite
            max_word = word

    assert max_word
    return max_word


def get_most_frequest_unsaid_word(hit_map: dict[str, int]) -> str:
    max_hit = None
    max_word = None
    for word, ite in hit_map.items():
        if not max_hit or ite > max_hit and word not in SAID_WORDS:
            max_hit = ite
            max_word = word

    assert max_word
    SAID_WORDS.add(max_word)
    return max_word


def get_probabilistic_word(hit_map: dict[str, int]) -> str:
    choices = []
    for w, c in hit_map.items():
        for _ in range(c):
            choices.append(w)

    return random.choice(choices)


def produce(ngram_map: dict[str, dict[str, int]], input_word: str, length: int) -> None:
    start_word = input_word.lower()

    sentence = []
    for _ in range(0, length):
        sub_map = ngram_map[start_word]
        print(sub_map)
        next_word = get_probabilistic_word(sub_map)

        sentence.append(next_word)
        start_word = next_word

    sentence = [input_word] + sentence
    print(" ".join(sentence))


def visualize() -> None:
    words = ["^", "fish", "swim", "fish", "jump", "i", "swim", "i", "fish", "$"]
    n_graph_map = ingest(words)

    graph = nx.DiGraph()

    # Add nodes (you can also add nodes along with the edges)
    graph.add_nodes_from(words)

    # Add edges with weights (representing transition probabilities)
    for key, next_word_map in n_graph_map.items():
        total = sum([n for n in next_word_map.values()])
        for next_word, occurences in next_word_map.items():
            graph.add_edge(next_word, key, prob=f"{(occurences / total):0.2f}")

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), arrowsize=30)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "prob"))

    plt.show()


if __name__ == "__main__":
    text_words = get_words("CourseMaterial/data/frankenstein.txt")
    text_words += get_words("CourseMaterial/data/dracula.txt")
    text_words += get_words("CourseMaterial/data/little_women.txt")
    ngram_map = ingest(text_words)
    produce(ngram_map, "Who", 15)
    visualize()
