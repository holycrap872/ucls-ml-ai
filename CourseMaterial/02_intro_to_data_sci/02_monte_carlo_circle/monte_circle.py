import datascience
import random
import typing
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def get_distance(point_1: Point, point_2: Point) -> float:
    x_diff = point_1.x - point_2.x
    y_diff = point_1.y - point_2.y

    return (x_diff ** 2 + y_diff ** 2) ** .5


def in_circle(point: Point) -> bool:
    assert -1.0 <= point.x <= 1.0
    assert -1.0 <= point.y <= 1.0

    return get_distance(point, Point(0, 0)) < 1.0


def run_experiment(trials: int, graph_ites: int) -> None:
    x_points: typing.List[float] = []
    y_points: typing.List[float] = []

    running_best_guess = []
    total_in_circle = 0

    for trial in range(1, trials):
        random_point = Point((random.random() * 2.0) - 1.0, (random.random() * 2.0) - 1.0)
        if in_circle(random_point):
            total_in_circle += 1

        x_points += [random_point.x]
        y_points += [random_point.y]

        if trial % graph_ites == 0:
            running_best_guess += [(total_in_circle / trial) * 4]
            print(running_best_guess[-1])

    points = datascience.Table().with_columns("X", datascience.make_array(*x_points), "Y", datascience.make_array(*y_points))
    over_time = datascience.Table().with_column("Best guess", datascience.make_array(*running_best_guess))

    points.scatter("X", "Y")
    over_time.plot()

run_experiment(500, 10)
