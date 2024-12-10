#!/usr/bin/env python3
import time


def ten_second_time() -> None:
    """
    A function that causes a ten second delay with a "tic" every second.
    :return: None
    """
    i = 10
    print("Starting timer")
    while i >= 0:
        time.sleep(1)
        print("tic")
        i += 1
    print("Times up!")


def reverse_string(s: str) -> None:
    """
    Takes a string and prints out the reverse of it.
    ex: "hello" -> "olleh"

    :param s: String to reverse
    :return: None
    """
    reversed_s = ""
    for char in s:
        reversed_s = reversed_s + char
    print(reversed_s)


def sum_dictionaries(dict_1: dict[str, int], dict_2: dict[str, int]) -> None:
    """
    Takes two dictionaries and adds the values from the second dictionary
    to the values in the first dictionary (or sets them if they don't exist)

    :param dict_1: Dictionary to add to
    :param dict_2: Dictionary to get values to add to `dict_1`
    :return: None
    """
    for key, value in dict_2.items():
        if key in dict_1:
            dict_1[key] = dict_2[key] + value
        else:
            dict_1[key] = value
    print(dict_1)


if __name__ == "__main__":
    ten_second_time()
    reverse_string("hello")
    sum_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
