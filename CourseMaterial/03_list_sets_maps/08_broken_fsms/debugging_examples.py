#!/usr/bin/env python3
import time


def ten_second_time() -> None:
    i = 10
    print("Starting timer")
    while i >= 0:
        time.sleep(1)
        print("tic")
        i += 1
    print("Times up!")


def reverse_string(s: str) -> None:
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    print(reversed_s)


def sum_dictionaries(dict1: dict[str, int], dict2: dict[str, int]) -> None:
    """
    Takes two dictionaries and adds the values from the second dictionary
    to the values in the first dictionary (or sets them if they don't exist)
    """
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] = dict2[key] + value
        else:
            dict1[key] = value
    print(dict1)


if __name__ == "__main__":
    ten_second_time()
    reverse_string("hello")
    sum_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
