# Python Data Structure Wheaties

Create two new files in your problem set skeleton. Name one file
`data_structure_wheaties.py` and put it in the `src` folder
(`src/data_structure_wheaties.py`). Name the other file
`test_data_structure_wheaties.py` and put it in the `test` folder
(`test/test_data_structure_wheaties.py`).

For each problem, create a new function in the `data_structure_wheaties.py` file
and then write at **least two unit tests** in the
`test_data_structure_wheaties.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a dictionary of ints mapped to ints as an
   input and returns a list of all of the dictionary's keys. Do **not** use
   the `.keys()` function.
1. Create a function that takes a dictionary of ints mapped to ints as an
   input and returns a list of all of the dictionary's values. Do **not** use
   the `.values()` function.
2. Create a function that takes a list of ints (even in length) and returns a
   dictionary where each even indexed element maps to the following, odd
   indexed element.
   - For example: `[1, 10, 2, 7, 8, 3] -> {1: 10, 2: 7, 8: 3}`
3. Create a function that takes two lists of equal size as inputs and returns a
   dictionary where each element of the first list points to the corresponding
   element in the second list.
   - For example: `[1, 2, 3], ["a", "b", "c"] -> {1: "a", 2: "b", 3: "c"}`
4. Create a function that takes a sentence as an input and returns a set of all
   of the characters in the sentence.
5. Create a function that takes a sentence as an input and returns a dictionary
    storing the count of each character.
    - For example: `"wow!" -> {"w": 2, "o":  1, "!": 1}`
6. Create a function that takes dictionary of ints mapped to ints as an input and
   returns the largest key.
7. Create a function that takes dictionary of ints mapped to ints as an input and
   returns the smallest value.
8. Create a function that takes a list of pairs as an input and returns those
   pairs as keys/values in a dictionary.
    - For example: `[(1, "a") (2, "b") (3, "c")] -> {1: "a", 2: "b", 3: "c"}`
9. Create a function that takes a sentence as an input and returns a set of all
   of the words in the sentence.
10. Create a function that takes list of ints and returns a dictionary containing
    the even/odd count.
    - For example: `[1, 11, 10, 5] -> {"even": 1, "odd": 3}`
11. Create a function that takes a sentence as an input and returns the number
    of unique words in the sentence.
    - For example: `"hey you hey there hey" -> 3`
12. Create a function that takes a dictionary of ints mapped to ints as an input
    and returns a list of all of the values in the dictionary in sorted order.
13. Create a function that takes a dictionary of ints mapped to ints as an input
    and returns a list of all of the values ordered by their keys (different
    from the previous question).
    - For example: `{1: 100, 3: 55, 2: 8} -> [100, 8, 55]`
14. Create a function that takes two lists of ints as inputs and returns the
    set of ints that are in both.
15. Create a function that takes a sentence and counts the number of times each
    word in the sentence appears.
    - For example: `"hey you hey there hey" -> {"hey": 3, "you": 1, "there": 1}`
16. Create a function that takes a string as an input and returns the first,
    non-repeated character in the string.
    - For example: `"good gosh" -> "d"`
17. Create a function that takes a list as an input and then returns a boolean
    of whether there are duplicates in the list.
18. Create a function that takes a list of strings as an input and returns a
    list containing the reverse of each string.
    - For example: `["apple", "banana", "cherry"] -> ["elppa", "ananab", "yrrehc"]`
19. Create a function that takes a list of ints as an input and returns a version
    of the input list without any duplicates but with order preserved.
    - For example: `[4, 5, 4, 4, 1, 2, 5] -> [4, 5, 1, 2]`
20. Create a function that takes a list of ints as an input and returns a version
    of the input list without any duplicates (order need not be preserved).
21. Create a function that takes two lists of ints as inputs and returns the set
    of ints that are in only one of the lists.
    - For example: `[4, 5, 4, 3], [3, 1, 5] -> {4, 1}`
