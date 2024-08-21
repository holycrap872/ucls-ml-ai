# Python Skills Assessment

## Explanation

This skills assessment is intended to determine where you are as a programmer.
You **will not** be graded for how many of these problems you get right. All
that matters is that you approach each problem with a problem solving attitude
and try to apply your past learnings to get as far as you can.

## Setup

Create a new file in your `ProblemSetSkeleton` workspace called `skills_assessment.py`
and put it in the `skeleton` folder (`src/skeleton/skills_assessment.py`).

For each problem, create a new function and then call that function from the
`__main__` hook. Once you have completed the problem, comment it out and move
onto the next one.

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

### Section 0: Functions using `input()` and `print()`

0. Create a function that asks for the user's name and then prints out a greeting.
1. Create a function that asks the user for three numbers and prints out the max.
   Do **not** use any outside helper functions (e.g., `max()`).
2. Create a function that asks the user for a single number and prints a "count
   down" from that number all the way to zero.

### Section 1: Functions using **parameters** for input and `return` for output

0. Create a function that takes a single number as an input and returns a boolean
   of whether it is a prime or not.
1. Create a function that takes a single word (string) as an input and returns a
   boolean of whether it is a palindrome or not. Create at least three unit tests.
2. Create a function that takes two lists of integers as inputs and returns a
   single list that is the "intersection" of the two lists. Create at least
   three unit tests.
3. Create a function that takes two **sorted** lists of integers as inputs and
   returns a single, combined **sorted** list. Create at least three unit tests.
   Do **not** use any outside helper functions (e.g., `sort()`).
4. Create a function that takes a single list of integers as an input and returns
   a list of pairs of all the numbers that were "next to each other". For
   example: `[1, 5, 6] -> [(1, 5), (5, 6)]`. Create at least three unit tests.
5. Create a function that takes two strings as inputs and returns a boolean
   of whether they are anagrams. Create at least three unit tests.
6. Create a function that takes a single string as an input and returns the
   score of the given string in a Scrabble game. Create at least three unit
   tests.
7. Implement a basic linked list data structure with functions for `insert()`,
   `delete()`, and `contains()`. Write enough unit tests such that you have
   100% line coverage.
