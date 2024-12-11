# Python Data Structure Wheaties (Unstructured)

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`data_structure_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/data_structure_wheaties.py`). Name the other file
`test_data_structure_wheaties.py` and put it in the `test` folder
(`test/test_data_structure_wheaties.py`).

For each problem, create a new function in the `data_structure_wheaties.py` file
and then write at **least two unit tests** in the
`test_data_structure_wheaties.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a dictionary of integers mapped to integers as
   an input and returns a set of all of the dictionary's **keys**.
    - **Do not** use the `.keys()` function.
    - For example: `{1: 5, 6: 3} -> {1, 6}`
1. Create a function that takes a dictionary of integers mapped to integers as
   an input and returns a set of all of the dictionary's **values**.
    - **Do not** use the `.values()` function.
    - For example: `{1: 5, 6: 3} -> {5, 3}`
2. Create a function that takes two lists of **equal size** as inputs and returns
   a dictionary where each element of the first list points to the corresponding
   element in the second list.
    - For example: `[1, 2, 3], ["a", "b", "c"] -> {1: "a", 2: "b", 3: "c"}`
3. Create a function that takes an **even-length** list of integers and returns
   a dictionary where each even-indexed element maps to the following,
   odd-indexed element.
    - For example: `[1, 10, 2, 7, 8, 3] -> {1: 10, 2: 7, 8: 3}`
4. Create a function that takes a sentence as an input and returns a set of all
   of the characters in the sentence.
   - For example: `"hey there" -> {"h", "e", "y", "t", "h", "r"}`
5. Create a function that takes a sentence as an input and returns a dictionary
   storing the count of each character.
    - For example: `"wow!" -> {"w": 2, "o":  1, "!": 1}`
6. Create a function that takes dictionary of integers mapped to integers as an
   input and returns the largest **key**.
    - **Do not** use the `max()` function.
    - For example: `{1: 9, 4: 2, 6: 6, 3: 7} -> 6`
7. Create a function that takes dictionary of integers mapped to integers as an
   input and returns the smallest **value**.
    - **Do not** use the `min()` function.
    - For example: `{1: 9, 4: 2, 6: 6, 3: 7} -> 2`
8. Create a function that takes a list of pairs as an input and returns those
   pairs as keys/values in a dictionary.
    - For example: `[(1, "a"), (2, "b"), (3, "c")] -> {1: "a", 2: "b", 3: "c"}`
9. Create a function that takes a sentence as an input and returns a set of all
   of the words in the sentence.
    - For example: `"my my well well" -> {"my", "well"}`
10. Create a function that takes two sets of integers as an input and returns a
    boolean of whether the first set is a "subset" of the second set.
    - Note: set `a` is subset of set `b` if every element in `a` is also in `b`.
    - For example: `{1, 4}, {1, 4, 10} -> True`
    - **Do not** use the `.issubset()` function.
11. Create a function that takes list of integers and returns a dictionary
    containing the even/odd count.
    - For example: `[1, 11, 10, 5] -> {"even": 1, "odd": 3}`
12. Create a function that takes a sentence as an input and returns the number
    of unique words in the sentence.
    - For example: `"hey you hey there hey" -> 3`
13. Create a function that takes a dictionary of integers mapped to integers as
    an input and returns a list of all of the **values** in the dictionary in
    sorted order.
    - Hint: use the `sorted()` function
    - For example: `{1: 9, 4: 2, 6: 6, 3: 7} -> [2, 6, 7, 9]`
14. Create a function that takes a dictionary of integers mapped to integers as
    an input and returns a list of all of the values **ordered by their keys**
    (different from the previous question).
    - For example: `{1: 100, 3: 55, 2: 8} -> [100, 8, 55]`
15. Create a function that takes two lists of integers as inputs and returns the
    set of integers that are in both.
    - For example: `[6, 6, 8, 1], [1, 8, 3] -> {1, 8}`
16. Create a function that takes a sentence and counts the number of times each
    word in the sentence appears.
    - For example: `"hey you hey there hey" -> {"hey": 3, "you": 1, "there": 1}`
17. Create a function that takes a string as an input and returns the first,
    non-repeated character in the string.
    - Hint: use a function you created for an earlier problem in this sheet
    - For example: `"good gosh" -> "d"`
18. Create a function that takes a list of integers as an input and then returns
    a boolean of whether there are duplicates in the list.
    - For example: `[5, 6, 7, 4, 5] -> True`
19. Create a function that takes a list of strings as an input and returns a
    list containing the reverse of each string.
    - For example: `["apple", "banana", "cherry"] -> ["elppa", "ananab", "yrrehc"]`
20. Create a function that takes two sets of integers as an input and returns a
    set of integers that is the intersection of the two sets.
    - For example: `{6, 9, 12}, {1, 5, 6, 8, 12, 13} -> {6, 12}`
    - **Do not** use the `intersection()` function.
21. Create a function that takes a list of integers as an input and returns a
    list that is a version of the original list, but without any duplicates. The
    order or the elements from the original list should be preserved.
    - For example: `[4, 5, 4, 4, 1, 2, 5] -> [4, 5, 1, 2]`
22. Create a function that takes two lists of integers as inputs and returns the
    set of integers that are in only one of the lists.
    - For example: `[4, 5, 4, 3], [3, 1, 5] -> {4, 1}`
23. Create a function that takes a set of integers and a number as an input and
    then returns a new set of integers containing numbers from the input set
    that are **less than** the given number.
    - For example: `{1, 4, 6, 3, 7, 2}, 5 -> {1, 4, 3, 2}`
24. Create a function that takes a list of integers and returns a dictionary
    where the keys are the integers and the values are lists of their indices.
    - For example: `[1, 2, 1, 3, 2] -> {1: [0, 2], 2: [1, 4], 3: [3]}`
25. Create a function that takes a list of integers and returns their average.
    - For example: `[4, 9, 11, 5] -> 5.8`
26. Create a function that takes a list of strings and a minimum length, then
    returns a set of all strings that are at least that length.
    - For example: `["cat", "dog", "mouse", "rat"], 4 -> {"mouse"}`
27. Create a function that takes a string and returns a dictionary where the
    keys are vowels and the values are how many times each vowel appears.
    - For example: `"hello there" -> {"e": 2, "o": 1, "a": 0, "i": 0, "u": 0}`
28. Create a function that takes a list of strings and returns a set of all
    characters that appear in every string.
    - For example: `["hello", "help", "whole"] -> {"h", "e", "l"}`
    - Hint: `.intersection()`
29. Create a function that takes a list of lists of integers and returns the
    average of each sub-list.
    - For example: `[[4, 9, 11, 5], [3, 5], [1, 1, 1]] -> [7.25, 4.0, 1.0]`
    - Hint: A recent previous problem will be very helpful
30. Create a function that takes a dictionary of student grades (lists of
    integers) and returns a dictionary with the same keys but values replaced
    with the letter grade (A >= 90, B >= 80, C >= 70, D >= 60, F < 60).
    - For example: `{"Alice": [92, 87], "Bob": [75, 77]} -> {"Alice": "B", "Bob": "C"}`
31. Create a function that takes a string and returns a dictionary where keys
    are characters and values are lists of indices where they appear.
    - For example: `"hello" -> {"h": [0], "e": [1], "l": [2, 3], "o": [4]}`
32. Create a function that takes a list of integers and returns a set of all
    numbers that are multiples of both 2 and 3.
    - For example: `[9, 12, 2, 3, 5, 10, 6, 7, 8] -> {6, 12}`
33. Create a function that takes a nested dictionary of strings and a complex key
    as an input and then returns the value for the nested key. If the complex key
    doesn't lead to anything, have it return the empty string.
    - For example: `{"a": {"b": {"c": "d"}}}, "a/b/c" -> "d"`
    - For example: `{"a": {"b": {"c": "d"}}}, "a/h/i" -> ""`
34. Create a function that takes a list of strings and returns a dictionary
    where the keys are the first characters and the values are sets of words
    that start with that character.
    - For example: `["hat", "cat", "hi"] -> {"h": {"hat", "hi"}, "c": {"cat"}}`
