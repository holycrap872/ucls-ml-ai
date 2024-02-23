# Python List Wheaties

Create two new files in your problem set skeleton. Name one file
`list_wheaties.py` and put it in the `skeleton` folder
(`src/skeleton/list_wheaties.py`). Name the other file `test_list_wheaties.py`
and put it in the `test` folder (`test/test_list_wheaties.py`).

For each problem, create a new function in the `list_wheaties.py` file and
then write at **least two unit tests** in the `test_list_wheaties.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a list of integers as an input and then returns
   a list containing only the even integers from the input list.
1. Create a function that takes a list of strings as an input and then returns
   a list containing all elements that were at **even indices** from the input
   list.
   - For example: `["for", "da", "big", "win" "!"] -> ["for", "big", "!"]`
2. Create a function that takes a list of strings as an input and then returns
   a string that is all of the strings in the input list concatenated.
   - For example: `["for", "da", "w"] -> "fordaw"`
3. Create a function that takes a list of integers as an input and then, using
   a loop, returns the reverse of the input list. Do **not** use something like
   `[::-1]`.
4. Create a function that takes a list of strings as an input and then returns
   a list of all of the strings that do not contain an "a" from the input list.
   - For example: `["What", "a", "wonderful", "world"] -> ["wonderful", "world"]`
5. Create a function that takes two inputs: a list of integers and a single
   integer. The function will the return True/False as to whether the single
   integer is in the list.
   - For example: `[1, 3, 5], 4 -> False`
6. Create a function that takes a list of integers as an input and then returns
   the second largest integer in the input list.
7. Create a function that takes a list of strings as an input and then returns
   whether the input list contains any duplicate elements.
8. Create a function that takes two lists of integers as inputs and then returns
   a single list containing all elements that are only in **one** of the two
   input lists.
   - For example: `[1, 2, 3], [2, 3, 4, 5] -> [1, 4, 5]`
9. Create a function that takes two lists of strings as inputs and then returns
   a single list which is the strings at each index concatenated. Assume that
   the two lists are of the same length.
   - For example: `["a", "hi"], ["b", "bye] -> ["ab", "hibye"]`
10. Create a function that takes a list of lists of integers and then returns
   a single list that is the input list "flattened".
   - For example: `[[1, 6], [3], [7, 9]] -> [1, 6, 3, 7, 9]`
11. Create a function that takes two lists of integers as inputs and then returns
   a single list such that they elements are alternating from the two input lists.
   **Do not** assume that the two lists are of the same length.
   - For example: `[1, 4, 10], [100, 3, 55] -> [1, 100, 4, 3, 10, 55]`