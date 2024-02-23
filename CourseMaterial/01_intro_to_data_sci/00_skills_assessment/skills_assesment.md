# Python Skills Assessment

This skills assessment is intended to determine where you are as a programmer.
You **will not** be graded for how many of these problems your get right. All
that matters is that you approach this problem set with a problem solving
attitude and try to apply your past learnings to get as far as you can.

For each problem, create a new function and then call that function from the
`__main__` hook. Once you have completed the problem, comment it out out and
move onto the next one.

For example:

```python3
def say_hi():
    ...


def max_of_three():
    ...


if __name__ == "__main__":
    # say_hi()
    max_of_three()

```

# Problems

### Problems using `input()` and `print()` functions

0. Create a function that asks for the user's name and then prints out a greeting.
1. Create a function that take three numbers from the user and prints out the max.
   Do **not** use any outside helper functions (e.g., `max()`).
2. Create a function that takes a single number from the user and prints a
   "count down" from that number all the way to zero.

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a single number as input and returns a boolean
   of whether it is a prime or not.
1. Create a function that takes a single word (string) as input and returns a
   boolean of whether it is a palindrome or not. Create at least four unit tests.
2. Create a function that takes two lists of integers as input and returns a
   single list that is the "intersection" of the two lists. Create at least
   four unit tests.
3. Create a function that takes two **sorted** lists of integers as inputs and
   returns a single, combined **sorted** list. Create at least four unit tests.
   Do **not** use any outside helper functions (e.g., `sort()`).
4. Create a function that takes a single list of integers as input and returns
   a list of pairs of all the numbers that were "next to each other". For
   example: `[1, 5, 6] -> [(1, 5), (5, 6)]`. Create at least four unit tests.
5. Create a function that takes two strings as inputs and returns a boolean
   of whether they are anagrams. Write enough unit tests such that you have
   100% line coverage.
6. Crate a function that takes a single string as an input and returns the
   score of the given string in a Scrabble game. Write enough unit tests such
   that you have 100% line coverage.
7. Implement a basic linked list data structure with functions for `insert()`,
   `delete()`, and `contains()`. Write enough unit tests such that you have
   100% line coverage.
