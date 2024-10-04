# Python Data Structure Wheaties

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
    - For example: `[(1, "a"), (2, "b"), (3, "c")] -> {1: "a", 2: "b", 3: "c"}`
9. Create a function that takes a sentence as an input and returns a set of all
   of the words in the sentence.
10. Create a function that takes two sets of ints as an input and returns a
    boolean of whether the first set is a "subset" of the second set. Do
    **not** use the `.issubset()` function.
11. Create a function that takes list of ints and returns a dictionary containing
    the even/odd count.
    - For example: `[1, 11, 10, 5] -> {"even": 1, "odd": 3}`
12. Create a function that takes a sentence as an input and returns the number
    of unique words in the sentence.
    - For example: `"hey you hey there hey" -> 3`
13. Create a function that takes a dictionary of ints mapped to ints as an input
    and returns a list of all of the values in the dictionary in sorted order.
14. Create a function that takes a dictionary of ints mapped to ints as an input
    and returns a list of all of the values ordered by their keys (different
    from the previous question).
    - For example: `{1: 100, 3: 55, 2: 8} -> [100, 8, 55]`
15. Create a function that takes two lists of ints as inputs and returns the
    set of ints that are in both.
16. Create a function that takes a sentence and counts the number of times each
    word in the sentence appears.
    - For example: `"hey you hey there hey" -> {"hey": 3, "you": 1, "there": 1}`
17. Create a function that takes a string as an input and returns the first,
    non-repeated character in the string.
    - For example: `"good gosh" -> "d"`
18. Create a function that takes a list as an input and then returns a boolean
    of whether there are duplicates in the list.
19. Create a function that takes a list of strings as an input and returns a
    list containing the reverse of each string.
    - For example: `["apple", "banana", "cherry"] -> ["elppa", "ananab", "yrrehc"]`
20. Create a function that takes two sets of ints as an input and returns a
    set of ints that is the intersection of the two sets. Do **not** use the
    `intersection()` function.
21. Create a function that takes a list of ints as an input and returns a set
    which is a version of the original list but without any duplicates.
22. Create a function that takes a list of ints as an input and returns a list
    which is a version of the original list but without any duplicates. The order
    or the elements from the original list should be preserved.
    - For example: `[4, 5, 4, 4, 1, 2, 5] -> [4, 5, 1, 2]`
23. Create a function that takes two lists of ints as inputs and returns the set
    of ints that are in only one of the lists.
    - For example: `[4, 5, 4, 3], [3, 1, 5] -> {4, 1}`
24. Create a function that takes a nested dictionary of strings and a complex key
    as an input and then returns the value for the nested key. If the complex key
    doesn't lead to anything, have it return the empty string.
    - For example: `{"a": {"b": {"c": "d"}}}, "a/b/c" -> "d"`
