#!/usr/bin/env python3
import random


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result: list[int] = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # At this point, either left or right may have elements left; append them.
    result += left
    result += right
    return result


# Example usage
for _ in range(100):
    orig_arr = []
    for _ in range(random.randint(1, 100)):
        orig_arr.append(random.randint(1, 100))

    test_arr = orig_arr.copy()
    test_arr = merge_sort(test_arr)
    orig_arr.sort()
    assert test_arr == orig_arr, f"{test_arr}, {orig_arr}"
