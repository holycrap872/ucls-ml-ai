#!/usr/bin/python3
import random
import typing

import matplotlib
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")
matplotlib.use("MacOSX")


class Point(typing.NamedTuple):
    x: float
    y: float


def get_distance(point_1: Point, point_2: Point) -> float:
    x_diff = point_1.x - point_2.x
    y_diff = point_1.y - point_2.y

    return (x_diff**2 + y_diff**2) ** 0.5


def in_circle(point: Point) -> bool:
    assert -1.0 <= point.x <= 1.0
    assert -1.0 <= point.y <= 1.0

    return get_distance(point, Point(0, 0)) < 1.0


def run_experiment(trials: int, graph_ites: int) -> None:
    in_x_points: typing.List[float] = []
    in_y_points: typing.List[float] = []
    out_x_points: typing.List[float] = []
    out_y_points: typing.List[float] = []

    running_best_guess = []
    total_in_circle = 0

    for trial_count in range(1, trials):
        random_point = Point((random.random() * 2.0) - 1.0, (random.random() * 2.0) - 1.0)
        if in_circle(random_point):
            total_in_circle += 1

            in_x_points += [random_point.x]
            in_y_points += [random_point.y]
        else:
            out_x_points += [random_point.x]
            out_y_points += [random_point.y]

        if trial_count % graph_ites == 0:
            running_best_guess += [(total_in_circle / trial_count) * 4]
            print(running_best_guess[-1])

    plots.figure(figsize=(6, 6))
    plots.title("Visualizing a Circle (erizzi)")
    plots.scatter(in_x_points, in_y_points, color="darkblue", label="Inside circle")
    plots.scatter(out_x_points, out_y_points, color="gold", label="Outside circle")
    plots.xlabel("X")
    plots.xlabel("Y")
    plots.yticks([-1, 0, 1])
    plots.xticks([-1, 0, 1])
    plots.show()

    plots.figure(figsize=(12, 6))
    plots.plot(running_best_guess)
    plots.xlabel("Iteration Count")
    plots.xlabel("Estimated Value of Pi")
    plots.show()


if __name__ == "__main__":
    run_experiment(5000, 10)
