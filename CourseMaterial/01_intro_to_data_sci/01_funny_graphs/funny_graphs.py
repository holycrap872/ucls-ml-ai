#!/usr/bin/python3
import typing

import matplotlib
import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")
matplotlib.use("MacOSX")


def funny_bar_chart() -> None:
    bar_names = ["Confirmed", "Refuted"]
    bar_values = [0, 100]

    plots.figure(figsize=(6, 6))

    plots.bar(x=bar_names, height=bar_values)

    # Make unique title for when students copy it
    plots.title("Claims of Supernatural Powers (erizzi)")
    plots.grid(False)
    plots.yticks([0, 25, 50, 75, 100])

    plots.show()


def funny_scatter_plot() -> None:
    plots.figure(figsize=(6, 6))

    plots.scatter([2.5, 3, 2, 1], [10, 9.5, 9, 10], color="red", label="Infant")
    plots.scatter([14, 12.5, 14.5, 13.5, 14], [1, 0, 0, 0.5, 0.5], color="orange", label="Teen")
    plots.scatter([25, 24, 23, 22], [0, 0.5, 0, 1], color="yellow", label="Hipster")
    plots.scatter([40, 37, 36, 39], [7, 2, 9, 2.5], color="green", label="Parent")
    plots.scatter([60, 62, 65, 66], [3, 2.5, 8.1, 8.7], color="blue", label="Retirement")
    plots.scatter([80, 81, 82, 83], [10, 9.5, 10, 9], color="purple", label="Elderly")

    plots.ylabel("Ability to Sit and Smile")
    plots.xlabel("Life Stage")
    plots.legend()
    plots.grid(True)

    plots.show()


def is_day(hours_since_start: int) -> bool:
    hour = hours_since_start % 24
    if 6 < hour < 22:
        return True
    return False


def funny_line_graph() -> None:
    plots.figure(figsize=(15, 8))

    hours = []
    fondness = []
    for hour in range(0, 100):
        hours.append(hour)
        if is_day(hour):
            fondness.append(hour)
        else:
            fondness.append(0)

    plots.plot(hours, fondness)

    plots.title("Absence Makes the Heart Grow Fond (except when I'm sleeping)")
    plots.ylabel("Amount of Fondness")
    plots.xlabel("Amount of Absence")
    plots.legend()
    plots.grid(True)

    plots.show()


if __name__ == "__main__":
    funny_bar_chart()
    funny_scatter_plot()
    funny_line_graph()
