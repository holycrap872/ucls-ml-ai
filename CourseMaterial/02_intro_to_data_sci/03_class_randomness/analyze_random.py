#!/usr/bin/python3
import csv
import typing

import matplotlib.pyplot as plots

plots.style.use("fivethirtyeight")


def read_file(file_path: str) -> typing.List[int]:
    """
    :param file_path: Takes in path to the .csv file
    :return: List of random integers in csv file
    """
    ret_list = []

    with open(file_path) as random_fp:
        c = csv.DictReader(random_fp)

        for elem in c:
            ret_list.append(int(elem["Random number"]))

    return ret_list


def bargraph_numbers(labels: typing.List[str], count_list: typing.List[int]) -> None:
    """
    :param labels: Labels to put for each bar in the bottom of the graph
    :param count_list: Number of seen values for each slot
    :return: None
    """
    plots.figure(figsize=(6, 6))
    plots.bar(x=labels, height=count_list, color="darkblue")
    plots.xlabel("X")
    plots.xlabel("Y")
    plots.show()


def scatter_numbers(numbers: typing.List[int]) -> None:
    """
    :param numbers: List of numbers
    :return: None
    """
    x_list = []
    y_list = []
    for i in range(0, len(numbers) - 1):
        x_list.append(numbers[i])
        y_list.append(numbers[i + 1])

    plots.figure(figsize=(6, 6))
    plots.scatter(x=x_list, y=y_list)
    plots.show()


if __name__ == "__main__":
    numbers = read_file("./CourseMaterial/01_intro_to_data_sci/07_class_randomness/random.csv")

    count_list = []
    labels = []
    for i in range(0, 10):
        labels.append(int(i))
        count_list.append(0)
    for n in numbers:
        count_list[n] += 1

    bargraph_numbers(labels, count_list)
    scatter_numbers(numbers)
