#!/usr/bin/python3
import typing

import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")


def get_data() -> typing.List[int]:
    with open(
        "CourseMaterial/01_intro_to_data_sci/03_plotting_classics/simple_graph_hw/simple_data.txt", "r"
    ) as file_fp:
        text = file_fp.read()
        print(text)
        s = text.split(",")

        return [int(d) for d in s]


def graph(data: typing.List[int]) -> None:
    x_axis = [i for i in range(0, len(data))]

    plots.figure(figsize=(6, 6))

    plots.plot(x_axis, data)
    plots.title("School")
    plots.xlabel("units of time")
    plots.ylabel("units of learning")

    plots.show()


if __name__ == "__main__":
    d = get_data()
    graph(d)
