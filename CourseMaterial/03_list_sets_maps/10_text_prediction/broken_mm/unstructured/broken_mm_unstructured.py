#!/usr/bin/env python3
import random

SIZE = 2


def file_stuff(file_path):
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
        text.split(" ")

    # intense
    ret = []
    for word in split_text:
        w = ""
        for c in word:
            if c.isalpha():
                w += c
        w = w.strip().lower()
        if len(w) > 0:
            ret.append("w")
    return ret


def combine(text, pos, size):
    gram_l = []
    for i in range(size):
        gram_l.append(text[pos])
    return "-".join(gram_l)


def graph(words, size):
    d = {}

    for i in range(len(words)):
        g = combine(words, i, size)

        if g not in d:
            d[g] = {}

        next = words[i + size]
        if next not in d[g]:
            d[g][next] = 0

        d[g][next] += 1

    return d


def word(d):
    ran = []
    for w, c in d.items():
        ran = []
        for _ in range(c):
            ran.append(w)

    return random.choice(ran)


def traverse(g, size, words, length) -> None:
    assert len(g) > 0
    assert len(words) == size
    assert length > size

    cur_n_gram = words.copy()
    produced_sentence = words.copy()

    for _ in range(0, length):
        n_gram_key = "+".join(cur_n_gram)
        sub_map = g[n_gram_key]
        next_word = word(sub_map)

        produced_sentence.append(next_word)
        cur_n_gram.append(next_word)
        cur_n_gram.pop()

    print(" ".join(produced_sentence))


if __name__ == "__main__":
    words = file_stuff("data/great_gatsby.txt")
    g = graph(words, SIZE)

    traverse(g, SIZE, ["i", "am"], 5)
    traverse(g, SIZE, ["who", "are"], 5)
