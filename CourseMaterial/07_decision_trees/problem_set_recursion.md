# Python Recursion Wheaties

Create a new file in your problem set skeleton. Name the file
`recursion_wheaties.py` and put it in the `skeleton` folder
(`src/skeleton/recursion_wheaties.py`).

For each problem, create a new **recursive function** in the
`recursion_wheaties.py` file and then call the function from the `__main__`
hook at the bottom of the file to make sure it works.

> Note: You do not need to create any unit tests for this worksheet.

# Problems

0. Create a recursive function that prints a "counts down" to `0` and then
   prints `blast off`. The recursive function should take an integer as an
   input and return `None`.
    - For example, with the initial input of 3, the program should print `3`
      then `2`, then `1`, then `blast off`. 
1. Create a recursive function that calculates factorials. The recursive
   function should take an integer as an input and return an integer.
    - For example: `3 -> 6` (3 * 2 * 1)
    - For example: `5 -> 120` (5 * 4 * 3 * 2 * 1)
2. Create a recursive function that calculates the number of characters in a
   string. The recursive function should should take a string as an input and
   return an integer.
    - For example: `"hello -> 5`
3. Create a recursive function that calculates the sum of natural numbers. The
   recursive function should take an integer as an input and return an integer.
    - For example: `3 -> 6` (3 + 2 + 1)
    - For example: `5 -> 15` (5 + 4 + 3 + 2 + 1)
4. Create a recursive function that calculates the sum of integers in a list.
   The recursive function should take a list of integers as an input and return
   an integer.
    - For example: `[4] -> 4`
    - For example: `[3, 7, 1] -> 11`
5. Create a recursive function that checks if a given string is a palindrome.
   The recursive function should take a string as an input and return a boolean.
    - For example: `elle -> True`
    - For example: `racecar -> True`
    - For example: `none -> False`
6. Create a recursive function to calculate one number raised to the power of
   another. The recursive function should take two integer inputs: `x` and `y`
   and return an integer representing `x**y`.
    - For example: `x=2, y=3 -> 8`
    - For example: `x=10, y=2 -> 100`
7. Create a recursive function to find the minimum element in a list. The
   recursive function should take a list of integers as an input and return
   an integer.
    - For example: `[1] -> 1`
    - For example: `[9, 4, 2, 7] -> 2`
8. Create a recursive function to count the number of occurrences of a
   particular number in a list. The recursive function should take a list
   of integers and an integer as inputs and return an integer.
    - For example: `[1], 1 -> 1`
    - For example: `[2, 5, 5, 6, 7, 5], 5 -> 5`
    - For example: `[2, 5, 5, 6, 7, 5], 1 -> 0`
9. Create a recursive function to calculate the value of two numbers multiplied
   by each other. The recursive function should take two integer inputs and
   return an integer representing `x * y`.
    - For example: `3, 2 -> 6`
    - Hint: Multiplication is a bunch of additions
10. Create a recursive function to determine the whether a list is sorted.
    The recursive function should take a list of integers as an input and
    return a boolean.
    - For example: `[1, 4, 7, 8] -> True`
    - For example: `[1, 4, 8, 7] -> False`
11. Create a recursive function to determine whether a string contains any
    vowels. The recursive function should take a string as an input and return
    a boolean.
    - For example: `"yolo" -> True`
    - For example: `"l33t" -> False`
12. Create a recursive function to determine whether a string contains a
    particular letter. The recursive function should take a two strings as
    inputs and return a boolean.
    - For example: `"yolo", "y" -> True`
    - For example: `"l33t", "y" -> False`
13. Create a recursive function to determine whether two strings are equal.
    The recursive function should take two strings as inputs and return a
    boolean.
    - For example: `"yolo", "yolo" -> True`
    - For example: `"l33t", "leet" -> False`
14. Create a recursive function to find all of the subsets of a given set. The
    recursive function should take a set of integers as an input and return a
    set of sets of integers.
    - For example: `{1} -> {{1}}`
    - For example: `{1, 2} -> {{1}, {2}, {1, 2}}`
    - For example: `{1, 2, 3} -> {{1}, {2}, {3}, {1, 2}, {1, 3}, {2,3}, {1, 2, 3}}`
