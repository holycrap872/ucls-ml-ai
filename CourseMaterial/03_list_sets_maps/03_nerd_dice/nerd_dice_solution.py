#!/usr/bin/env python3
import random

import matplotlib
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")
matplotlib.use("MacOSX")


def roll_one_dice_() -> int:
    return random.randint(1, 20)


def roll_two_dice_() -> int:
    return random.randint(1, 10) + random.randint(1, 10)


def roll_twenty_dice_() -> int:
    s = 0
    for _ in range(20):
        s += random.randint(0, 1)
    return s


def one_dice_experiment() -> None:
    one_dice_count: dict[int, int] = {}
    for _ in range(0, 10_000):
        val = roll_one_dice_()
        if val not in one_dice_count:
            one_dice_count[val] = 1
        else:
            one_dice_count[val] += 1

    bar_names: list[str] = []
    bar_values: list[int] = []
    for k in sorted(one_dice_count):
        bar_names.append(str(k))
        bar_values.append(one_dice_count[k])

    plots.figure(figsize=(8, 6))
    plots.bar(x=bar_names, height=bar_values)
    plots.show()


if __name__ == "__main__":
    one_dice_experiment()
