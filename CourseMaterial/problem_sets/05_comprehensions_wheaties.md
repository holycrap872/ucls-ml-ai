# Python Comprehension Wheaties

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`comprehension_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/comprehension_wheaties.py`). Name the other file `test_comprehension_wheaties.py`
and put it in the `test` folder (`test/test_comprehension_wheaties.py`).

For each problem, create a new, **single line** function in the
`comprehension_wheaties.py` file and then write at **least two unit test** in
the `test_comprehension_wheaties.py` file.

# Preparation

- Watch [this video](https://youtu.be/AhSvKGTh28Q) up to 00:04:52.00
- Check out [this webpage](https://www.w3schools.com/Python/python_lists_comprehension.asp)

# Problems

### List Comprehension Problems using **parameters** for input and `return` for output

0. Create a function that takes a number as an input and then returns a new list
   with all the numbers from 0 up to the given number.
    - For example: `3 -> [0, 1, 2, 3]`
1. Create a function that takes a list of strings as an input and then returns
   a new list containing the length of each string.
    - For example: `["hey", "there", "class"] -> [3, 5, 5]`
2. Create a function that takes a list of numbers as an input and then returns
   a new list containing only the positive numbers from the input list.
    - For example: `[-1, 2, -3, 4, -5] -> [2, 4]`
3. Create a function that takes a list of numbers as an input and then returns
   a new list containing a string representation of whether the element was
   positive or negative.
    - For example: `[-1, 2, -3] -> ["negative", "positive", "negative"]`
4. Create a function that takes a list of numbers as an input and then returns
   a new list containing the numbers from the input list that are divisible by 3.
    - For example: `[1, 2, 3, 4, 5, 6, 7] -> [3, 6]`
5. Create a function that takes a list of strings as an input and then returns
   a new list containing the strings from the input list that are palindromes
   (the same forwards and backwards).
    - For example: `["racecar", "level", "python"] -> ["racecar", "level"]`
6. Create a function that takes a list of strings as an input and then returns
   a new list containing the strings from the input list that are palindromes
   and have an even number of characters.
    - For example: `["hey", "civic", "hannah"] -> ["hannah"]`
7. Create a function that takes a list of numbers as an input and then returns
   a new list containing the numbers from the input list that are perfect
   squares.
    - For example: `[1, 2, 3, 4, 5] -> [1, 4]`

### Dict Comprehension Problems using **parameters** for input and `return` for output

8. Create a function that takes a number as an input and then returns a new dictionary
   with all the numbers from 0 up to the given number mapped to their square.
    - For example: `3 -> {0: 0, 1: 1, 2: 4, 3: 9}`
9. Create a function that takes a list of strings as an input and returns a
   dictionary where the keys are the strings and the values are the lengths of
   the strings.
    - For example: `["hey", "there"] -> {"hey": 4, "there": 5}`
10. Create a function that takes a list of strings as an input and returns a
    dictionary where the keys are the strings and the values are boolean values
    indicating whether the string contains the letter 'e'.
    - For example: `["hello", "class"] -> {"hello": True, "class": False}`
11. Create a function that takes a list of tuples (name, age) as an input and
    returns a dictionary where the keys are the names and the values are the ages.
    - For example: `[("Alice", 25), ("Bob", 30)] -> {"Alice": 25, "Bob": 30}`
12. Create a function that takes a dictionary and returns a new dictionary where
    the keys and values are reversed. If there are duplicate values, it's ok if
    one of them gets dropped.
    - For example `{"a": 1, "b": 2, "c": 1} -> {1: "c", 2: "b"}`
13. Create a function that takes two lists of equal size and returns a dictionary
    where the items in the first list are mapped to the items in the second list.
    - For example `[1, 4], [5, 8] -> {1: 5, 4: 8}`
