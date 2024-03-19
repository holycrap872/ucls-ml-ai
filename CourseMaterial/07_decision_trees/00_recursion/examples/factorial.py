def factorial(x: int) -> int:
    if x <= 1:
        breakpoint()
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == "__main__":
    print(factorial(5))
