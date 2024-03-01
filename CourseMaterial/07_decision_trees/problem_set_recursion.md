# Python Recursion Wheaties

Create a new file in your problem set skeleton. Name the file
`recursion_wheaties.py` and put it in the `skeleton` folder
(`src/skeleton/recursion_wheaties.py`).

For each problem, create a new **recursive function** in the
`recursion_wheaties.py` file and then call the function from the `__main__`
hook at the bottom of the file to make sure it works.

> Note: You do not need to create any unit tests for this worksheet.

# Problems

0. The goal of this problem is to create a recursive function that "counts down"
   to `0` and then says `blast off`. The recursive function should take an
   integer as an input and return `None`.
    - For example, with the initial input of 3, the program should print `3`
      then `2`, then `1`, then `blast off`. 
1. The goal of this problem is to create a recursive function that calculates
   the number of characters in a string. The recursive function should should
   take a string as an input and return an integer.
    - For example: `"hello -> 5`
2. The goal of this problem is to create a recursive function that calculates
   factorials. The recursive function should take an integer as an input and
   return an integer.
    - For example: `3 -> 6` (3 * 2 * 1)
    - For example: `5 -> 120` (5 * 4 * 3 * 2 * 1)
3. The goal of this problem is to create a recursive function that checks if
   a given string is a palindrome. The recursive function should take a string
   as an input and return a boolean.
    - For example: `elle -> True`
    - For example: `racecar -> True`
    - For example: `none -> False`
4. The goal of this problem is to create a recursive function that calculates
   the sum of integers in an array. The recursive function should take a list
   of integers as an input and return an integer.
    - For example: `[4] -> 4`
    - For example: `[3, 7, 1] -> 11`
5. The goal of this problem is to create a recursive function that calculates
   the sum of natural numbers. The recursive function should take an integer as
   an input and return an integer.
    - For example: `3 -> 6` (3 + 2 + 1)
    - For example: `5 -> 15` (5 + 4 + 3 + 2 + 1)
6. The goal of this problem is to create a recursive function to calculate one
   number raised to the power of another. The recursive function should take
   two integer inputs: `x` and `y` and return an integer representing `x**y`.
    - For example: `x=2, y=3 -> 8`
    - For example: `x=10, y=2 -> 100`
