# Python Wheaties

For each problem, create a new function and then call that function from the
`__main__` hook. Once you have completed the problem, comment it out out and
move onto the next one.

For example:

```python3
def min_of_three():
    ...


def max_of_three():
    ...


if __name__ == "__main__":
    # say_hi()
    min_of_three(4, 5, 6)

```

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes three numbers as input and returns the smallest
   number. Do **not** use any outside helper functions (e.g., `min()`). Create
   at least three unit tests.
1. Create a function that takes a list of numbers as input and returns the sum
   of all the numbers in the list. Do **not** use any outside helper functions
   (e.g., `sum()`). Create at least three unit tests.
2. Create a function that takes two lists of numbers of the same size as input
   and returns a single list with each of the numbers in the same indices added
   together. For example `[1, 4], [3, 2] -> [4, 6]` Create at least three unit
   test.
3. Create a function that takes a list of pairs and returns a single list with
   each of the pairs added together. For example `[(1, 4), (3, 10)] -> [5, 13]`.
   Create at least three unit tests.
