#!/usr/bin/env python3
import random
import typing

import matplotlib
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")
matplotlib.use("MacOSX")


def roll_two_dice_experiment() -> int:
    return random.randint(1, 10) + random.randint(1, 10)


def roll_one_dice_experiment() -> int:
    return random.randint(1, 20)


def one_dice_experiment() -> None:
    one_dice_count = {}
    for _ in range(0, 10_000):
        val = roll_one_dice_experiment()
        if val not in one_dice_count:
            one_dice_count[val] = 0
        one_dice_count[val] += 1

    bar_names = []
    bar_values = []
    for k in sorted(one_dice_count):
        bar_names.append(str(k))
        bar_values.append(one_dice_count[k])

    plots.figure(figsize=(6, 6))

    plots.bar(x=bar_names, height=bar_values)

    plots.title("One Dice graph")
    plots.grid(False)
    plots.yticks([1])

    plots.show()


def two_dice_experiment() -> None:
    two_dice_count = {}
    for _ in range(0, 10_000):
        val = roll_two_dice_experiment()
        if val not in two_dice_count:
            two_dice_count[val] = 0
        two_dice_count[val] += 1

    bar_names = []
    bar_values = []
    for k in sorted(two_dice_count):
        bar_names.append(str(k))
        bar_values.append(two_dice_count[k])

    plots.figure(figsize=(6, 6))

    plots.bar(x=bar_names, height=bar_values)

    plots.title("Two Dice Graph")
    plots.grid(False)
    plots.yticks([1])

    plots.show()


if __name__ == "__main__":
    one_dice_experiment()
    two_dice_experiment()
