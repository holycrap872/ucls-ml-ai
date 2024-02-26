#!/usr/bin/env python3


def calc_fib(num: int) -> int:
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return calc_fib(num - 1) + calc_fib(num - 2)


breakpoint()
# print(calc_fib(0))
# print(calc_fib(1))
print(calc_fib(2))
# print(calc_fib(3))
# print(calc_fib(4))
