# Python List Wheaties

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`list_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/list_wheaties.py`). Name the other file `test_list_wheaties.py`
and put it in the `test` folder (`test/test_list_wheaties.py`).

For each problem, create a new function in the `list_wheaties.py` file and
then write at **least two unit tests** in the `test_list_wheaties.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a list of strings as an input and then returns
   the number of strings that contain `"a"` from the input list.
    - For example: `["What", "a", "wonderful", "world"] -> 2`
    - Hint: accumulator pattern
    - Hint: `in`
1. Create a function that takes a list of strings as an input and then returns
   a list of all of the strings that **do not** contain an `"a"` from the input list.
    - For example: `["What", "a", "wonderful", "world"] -> ["wonderful", "world"]`
2. Create a function that takes a list of integers as an input and then returns
   a list containing only the even integers from the input list.
    - For example: `[1, 4, 6, 7, 11] -> [4, 6]`
    - Hint: accumulator pattern
    - Hint: `% 2 == 0`
3. Create a function that takes a list of strings as an input and then returns
   a string that is all of the strings in the input list concatenated.
    - For example: `["for", "da", "win"] -> "fordawin"`
4. Create a function that takes a list of strings as an input and then returns
   a list containing all elements that were at **even indices** from the input
   list.
    - For example: `["for", "da", "big", "win" "!"] -> ["for", "big", "!"]`
5. Create a function that takes a list of integers as an input and then, using
   a loop, returns the reverse of the input list.
    - **Do not** use something like `[::-1]`.
6. Create a function that takes a list of strings as an input and then returns
   a list of all of the strings that **start with** a `"w"` or `"W"`.
    - For example: `["What", "awe", "wonderful", "world"] -> ["What", "wonderful", "world"]`
7. Create a function that takes **two inputs**: a list of integers and a single
   integer. The function will the return True/False as to whether the single
   integer is in the list.
    - For example: `[1, 3, 5], 4 -> False`
8. Create a function that takes a list of **non-repeating** integers as an input
   and then returns the second largest integer in the input list.
    - For example: `[1, 3, 2, 5] -> 3`
    - Hint: Sorting really helps
9. Create a function that takes **two inputs**: a list of integers and a single
   integer. The function will count the number of times that the given integer
   appears in the input list.
    - For example: `[1, 3, 5], 4 -> 0`
10. Create a function that takes **two inputs**: a list of integers and a second
   list of integers as inputs and then returns a single list containing all
   elements that are in **only one** of the two input lists.
    - For example: `[1, 2, 3], [2, 3, 4, 5] -> [1, 4, 5]`
11. Create a function that takes **two inputs**: a list of strings and a second
   list of strings as inputs and then returns a single list which is the strings
   at each index concatenated.
    - Assume that the two lists are of the same length.
    - For example: `["a", "hi"], ["b", "bye] -> ["ab", "hibye"]`
12. Create a function that takes a list of lists of integers and then returns
   a single list that is the input list "flattened".
    - For example: `[[1, 6], [3], [7, 9]] -> [1, 6, 3, 7, 9]`
13. Create a function that takes **two inputs**: a list of integers and a second
   list of integers as inputs and then returns a single list such that the
   elements are alternating from the two input lists.
    - **Do not** assume that the two lists are of the same length.
    - For example: `[1, 4, 10], [100, 3, 55, 66, 7] -> [1, 100, 4, 3, 10, 55, 66, 7]`
14. Create a function that takes a string of words as an input and returns a
   list of integers representing the length of each those word.
    - For example: `"hey there friend" -> [3, 5, 6]`
15. Create a function that takes a string of numbers separated by spaces as an
   input and returns a list of integers such that each of the numbers in the
   string incremented by one.
    - For example: `"1 5 10 44" -> [2, 6, 11, 45]`
    - Hint: `split()`
16. Create a function that takes a list of integers as an input and returns the
   longest sequence of **identical numbers** in the list.
    - For example: `[1, 1, 6, 1, 5, 5, 6, 6, 6, 6, 8] -> [6, 6, 6, 6]`
17. Create a function that takes a list of integers as an input and returns the
   longest sequence of **consecutive numbers** in the list.
    - For example: `[1, 2, 3, 5, 6, 7, 8, 10] -> [5, 6, 7, 8]`
18. Create a function that takes a string containing tab-separated values
   (TSV) data and returns a list of lists, where each inner list represents a
   row of data.
    - For example: `"100\t88\n1,2\n3\t62" -> [[100, 88], [1, 2], [3, 62]]`
    - Hint: use `split()` two times
19. Create a function that takes a string of numbers separated by commas as an
   input and returns a list of integers such that each of those numbers is
   squared.
    - For example: `"1,5,10,-9" -> [1, 25, 100, 81]`
    - Hint: `split()`
20. Create a function that takes a string of the words "one" or "zero" and
   returns a matching list of those words as integers.
    - For example: `"one one zero one" -> [1, 1, 0, 1]`
21. Create a function that takes a list of strings as an input and then returns
   whether the input list contains any duplicate elements.
    - Hint: A loop in a loop
