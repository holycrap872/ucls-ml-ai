# Python Data Structure Wheaties (Structured)

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
    - For example: `{1: 5, 6: 3} -> {1, 6}`
    - **Do not** use the `.keys()` function
    - Hint: To iterate through a dictionary's keys, you do `for key in d:`
    - Hint: To create an empty accumulator set, you do `acc_set = set()`
1. Create a function that takes a dictionary of integers mapped to integers as
   an input and returns a set of all of the dictionary's **values**.
    - For example: `{1: 5, 6: 3} -> {5, 3}`
    - **Do not** use the `.values()` function
    - Hint: To use a key to get a dictionary's value, you do `d[key]`
2. Create a function that takes two lists of **equal size** as inputs and returns
   a dictionary where each element of the first list points to the corresponding
   element in the second list.
    - For example: `[1, 2, 3], ["a", "b", "c"] -> {1: "a", 2: "b", 3: "c"}`
    - Hint: To create an empty accumulator dict, you do `acc_dict = dict()`
    - Hint: To add a value in a dictionary, you do `d[key] = value`
3. Create a function that takes an **even-length** list of integers and returns
   a dictionary where each even-indexed element maps to the following,
   odd-indexed element.
    - For example: `[1, 10, 2, 7, 8, 3] -> {1: 10, 2: 7, 8: 3}`
    - Hint: Use a `for i in range(0, len(l), 2):` loop
4. Create a function that takes a sentence as an input and returns a set of all
   of the characters in the sentence.
   - For example: `"hey there" -> {"h", "e", "y", "t", "h", "r"}`
   - Hint: To create an empty accumulator set, you do `acc_set = set()`
5. Create a function that takes a sentence as an input and returns a dictionary
   storing the count of each character.
    - For example: `"wow!" -> {"w": 2, "o":  1, "!": 1}`
    - Hint: To create an empty accumulator dict, you do `acc_dict = dict()`
    - Hint: You need an `if letter not in d:` check somewhere in the loop
6. Create a function that takes a dictionary of integers mapped to integers as an
   input and returns the largest **key**.
    - For example: `{1: 9, 4: 2, 6: 6, 3: 7} -> 6`
    - Hint: Have an accumulator called `largest_key`
    - Hint: To iterate through a dictionary's keys, you do `for key in d:`
    - **Do not** use the `max()` function.
7. Create a function that takes dictionary of integers mapped to integers as an
   input and returns the smallest **value**.
    - For example: `{1: 9, 4: 2, 6: 6, 3: 7} -> 2`
    - **Do not** use the `min()` function.
    - Hint: To use a key to get it's corresponding value, you do `d[key]`
8. Create a function that takes a list of pairs as an input and returns those
   pairs as keys/values in a dictionary.
    - For example: `[(1, "a"), (2, "b"), (3, "c")] -> {1: "a", 2: "b", 3: "c"}`
    - Hint: To iterate through a list of pairs, you do `for first, second in l:`
9. Create a function that takes a sentence as an input and returns a set of all
   of the words in the sentence.
    - For example: `"my my well well" -> {"my", "well"}`
    - Hint: Use `.split(" ")`
    - Hint: To create an empty accumulator set, you do `acc_set = set()`
10. Create a function that takes two sets of integers as an input and returns a
    boolean of whether the first set is a "subset" of the second set.
    - Note: set `a` is subset of set `b` if every element in `a` is also in `b`
    - For example: `{1, 4}, {1, 4, 10} -> True`
    - Hint: To iterate through a set, you do `for elem in s:`
    - Hint: To check whether an element is in a set, you do `if elem in s:`
11. Create a function that takes list of integers and returns a dictionary
    containing the even/odd count.
    - For example: `[1, 11, 10, 5] -> {"even": 1, "odd": 3}`
    - Hint: Have an initial accumulator dict of `d = {"even": 0, "odd": 0}`
12. Create a function that takes a sentence as an input and returns the number
    of unique words in the sentence.
    - For example: `"hey you hey there hey" -> 3`
    - Hint: This is just like a previous problem, but then you use `len()`
13. Create a function that takes a dictionary of integers mapped to integers as
    an input and returns a list of all of the **values** in the dictionary in
    sorted order.
    - For example: `{1: 9, 4: 2, 6: 6, 3: 7} -> [2, 6, 7, 9]`
    - Hint: To get a sorted list of integers you do `sorted_l = sorted(l)`
14. Create a function that takes a dictionary of integers mapped to integers as
    an input and returns a list of all of the values **ordered by their keys**
    (different from the previous question).
    - For example: `{1: 100, 3: 55, 2: 8} -> [100, 8, 55]`
    - Hint: To get the keys of a dict in sorted order, you do `for k in sorted(d):`
15. Create a function that takes two lists of integers as inputs and returns the
    set of integers that are in both.
    - For example: `[6, 6, 8, 1], [1, 8, 3] -> {1, 8}`
    - Hint: To check if an element is in a list you do `if elem in l:`
16. Create a function that takes a sentence and counts the number of times each
    word in the sentence appears.
    - For example: `"hey you hey there hey" -> {"hey": 3, "you": 1, "there": 1}`
    - Hint: Use `split(" ")`
    - Hint: This is similar to a previous "counting dict" problem
17. Create a function that takes a string as an input and returns the first,
    non-repeated character in the string.
    - For example: `"good gosh" -> "d"`
    - Hint: First create and then use a counting dict of all of the letters
18. Create a function that takes a list of integers as an input and then returns
    a boolean of whether there are duplicates in the list.
    - For example: `[5, 6, 7, 4, 5] -> True`
    - Hint: Create a counting dict of all of the elements
19. Create a function that takes a list of strings as an input and returns a
    list containing the reverse of each string.
    - For example: `["apple", "banana", "cherry"] -> ["elppa", "ananab", "yrrehc"]`
    - Hint: Creating a helper function called `reverse_string()` will be useful
20. Create a function that takes two sets of integers as an input and returns a
    set of integers that is the intersection of the two sets.
    - **Do not** use the `intersection()` function.
    - Hint: To check if an element is in a set you do `if elem in s:`
21. Create a function that takes a list of integers as an input and returns a
    list that is a version of the original list, but without any duplicates. The
    order or the elements from the original list should be preserved.
    - For example: `[4, 5, 4, 4, 1, 2, 5] -> [4, 5, 1, 2]`
    - Hint: First create and then use a counting dict of all of the numbers
22. Create a function that takes two lists of integers as inputs and returns the
    set of integers that are in only one of the lists.
    - For example: `[4, 5, 4, 3], [3, 1, 5] -> {4, 1}`
    - Hint: To check if an element is in a set you do `if elem in l:`
23. Create a function that takes a nested dictionary of strings and a complex key
    as an input and then returns the value for the nested key. If the complex key
    doesn't lead to anything, have it return the empty string.
    - For example: `{"a": {"b": {"c": "d"}}}, "a/b/c" -> "d"`
    - For example: `{"a": {"b": {"c": "d"}}}, "a/h/i" -> ""`
    - Hint: Use `.split("/")`
