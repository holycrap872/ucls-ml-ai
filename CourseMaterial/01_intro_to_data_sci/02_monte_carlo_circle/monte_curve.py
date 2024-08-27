#!/usr/bin/env python3
import random
import typing

import matplotlib
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")
matplotlib.use("MacOSX")


"""
Find the area under x^2 curve from -1 to 1
"""


def get_random_point() -> typing.Tuple[float, float]:
    rand_x = (random.random() * 2.0) - 1.0  # random number between -1 and 1
    rand_y = random.random()  # random number between 0 and 1
    return (rand_x, rand_y)


def is_under_curve(point: typing.Tuple[float, float]) -> bool:
    assert -1.0 <= point[0] <= 1.0
    assert -1.0 <= point[1] <= 1.0

    calc_y = point[0] ** 2
    return point[1] < calc_y


def run_experiment(trials: int, graph_ites: int) -> None:
    in_x_points: typing.List[float] = []
    in_y_points: typing.List[float] = []
    out_x_points: typing.List[float] = []
    out_y_points: typing.List[float] = []

    running_best_guess = []
    total_in_circle = 0

    for trial_count in range(1, trials):
        random_point = get_random_point()
        if is_under_curve(random_point):
            total_in_circle += 1

            in_x_points += [random_point[0]]
            in_y_points += [random_point[1]]
        else:
            out_x_points += [random_point[0]]
            out_y_points += [random_point[1]]

        if trial_count % graph_ites == 0:
            running_best_guess += [(total_in_circle / trial_count) * 2]
            print(running_best_guess[-1])

    plots.figure(figsize=(6, 6))
    plots.scatter(in_x_points, in_y_points, color="darkblue", label="Inside circle")
    plots.scatter(out_x_points, out_y_points, color="gold", label="Outside circle")
    plots.xlabel("X")
    plots.xlabel("Y")
    plots.show()

    plots.figure(figsize=(12, 6))
    plots.plot(running_best_guess)
    plots.xlabel("Iteration Count")
    plots.xlabel("Estimated Value Under Curve")
    plots.show()


if __name__ == "__main__":
    run_experiment(5000, 10)
