#!/usr/bin/env python3
import random
import typing

import matplotlib
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")
matplotlib.use("MacOSX")


def get_distance_from_origin(x: float, y: float) -> float:
    return (x**2 + y**2) ** 0.5


def in_circle(x: float, y: float) -> bool:
    assert -1.0 <= x <= 1.0
    assert -1.0 <= y <= 1.0

    return get_distance_from_origin(x, y) < 1.0


def run_experiment(trials: int) -> None:
    in_x_points: typing.List[float] = []
    in_y_points: typing.List[float] = []
    out_x_points: typing.List[float] = []
    out_y_points: typing.List[float] = []

    total_in_circle = 0

    for trial in range(1, trials):
        random_x = (random.random() * 2.0) - 1.0
        random_y = (random.random() * 2.0) - 1.0
        if in_circle(random_x, random_y):
            total_in_circle += 1

            in_x_points += [random_x]
            in_y_points += [random_y]
        else:
            out_x_points += [random_x]
            out_y_points += [random_y]

    plots.figure(figsize=(6, 6))
    plots.title("Visualizing a Circle (erizzi)")

    plots.scatter([], [], color="darkblue", label="Inside circle")
    plots.scatter([], [], color="gold", label="Outside circle")
    plots.show()

    plots.xlabel("X")
    plots.xlabel("Y")
    plots.yticks([-1, 0, 1])
    plots.xticks([-1, 0, 1])
    plots.show()


if __name__ == "__main__":
    run_experiment(5000)
