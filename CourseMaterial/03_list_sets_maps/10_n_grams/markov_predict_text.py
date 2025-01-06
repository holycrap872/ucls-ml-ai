#!/usr/bin/env python3
import random

import matplotlib.pyplot as plt
import networkx as nx

SAID_WORDS = set()


def get_text_words(file_path: str) -> list[str]:
    with open(file_path, "r") as fd:
        text = fd.read()
        text = text.lower()
        text = text.replace("-", " ")
        text = text.replace("'", "")
        text = text.replace("_", "")
        text = text.replace(",", " ")
        text = text.replace('"', "")
        text = text.replace("“", "")
        text = text.replace("”", "")
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("&", "")
        text = text.replace(";", "")
        text = text.replace("\n", " ")
        return text.split(" ")


def create_markov_graph(text_words: list[str]) -> dict[str, dict[str, int]]:
    markov_graph: dict[str, dict[str, int]] = {}
    prev_word = None

    for word in text_words:
        cur_word = word.strip().lower()
        if cur_word not in markov_graph:
            markov_graph[cur_word] = {}

        if prev_word:
            if prev_word not in markov_graph[cur_word]:
                markov_graph[cur_word][prev_word] = 0

            markov_graph[cur_word][prev_word] += 1

        prev_word = cur_word

    return markov_graph


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


def produce(markov_graph: dict[str, dict[str, int]], input_word: str, length: int) -> None:
    start_word = input_word.lower()

    sentence = []
    for _ in range(0, length):
        sub_map = markov_graph[start_word]
        next_word = get_probabilistic_word(sub_map)

        sentence.append(next_word)
        start_word = next_word

    sentence = [input_word] + sentence
    print(" ".join(sentence))


def visualize(markov_graph: dict[str, dict[str, int]]) -> None:
    graph = nx.DiGraph()

    # Add nodes (you can also add nodes along with the edges)
    graph.add_nodes_from([w for w in markov_graph])

    # Add edges with weights (representing transition probabilities)
    for key, next_word_map in markov_graph.items():
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
    text_words = get_text_words("CourseMaterial/data/frankenstein.txt")
    text_words += get_text_words("CourseMaterial/data/dracula.txt")
    text_words += get_text_words("CourseMaterial/data/little_women.txt")
    markov_graph = create_markov_graph(text_words)
    produce(markov_graph, "Who", 15)

    sample_text_words = ["^", "fish", "swim", "fish", "jump", "i", "swim", "i", "fish", "$"]
    sample_markov_graph = create_markov_graph(sample_text_words)
    visualize(sample_markov_graph)
