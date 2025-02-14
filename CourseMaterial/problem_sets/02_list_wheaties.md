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
0. Create a function that takes a list of strings as an input and then returns
   a list of all of the strings that **do not** contain an `"a"` from the input list.
    - For example: `["What", "a", "wonderful", "world"] -> ["wonderful", "world"]`
0. Create a function that takes a list of integers as an input and then returns
   a list containing only the even integers from the input list.
    - For example: `[1, 4, 6, 7, 11] -> [4, 6]`
    - Hint: accumulator pattern
    - Hint: `% 2 == 0`
0. Create a function that takes a list of strings as an input and then returns
   a string that is all of the strings in the input list concatenated.
    - For example: `["for", "da", "win"] -> "fordawin"`
    - Hint: accumulator pattern
0. Create a function that takes a list of strings as an input and then returns
   the same list of strings with words rotated one position left.
    - For example: `["hello", "there", "world"] -> ["there", "world", "hello"]`
    - Hint: `pop()` and `append()`
0. Create a function that takes a list of strings as an input and then returns
   a list containing all elements that were at **even indices** from the input
   list.
    - For example: `["for", "da", "big", "win" "!"] -> ["for", "big", "!"]`
    - Hint: accumulator pattern combined with using `range()` with step
0. Create a function that takes a list of integers as an input and then, using
   a loop, returns the reverse of the input list.
    - For example: `[1, 5, 8, 10] -> [10, 8, 5, 1]`
    - **Do not** use something like `[::-1]`
0. Create a function that takes a list of strings as an input and then returns
   a list of all of the strings that **start with** a `"w"` or `"W"`.
    - For example: `["What", "awe", "wonderful", "world"] -> ["What", "wonderful", "world"]`
0. Create a function that takes a list of integers as input and returns the sum
   of all positive numbers.
    - For example: `[1, -4, 6, -2, 3] -> 10`
    - Hint: accumulator pattern
0. Create a function that takes **two inputs**: a list of integers and a single
   integer. The function will then return True/False as to whether the single
   integer is in the list.
    - For example: `[1, 3, 5], 4 -> False`
    - For example: `[1, 3, 5], 3 -> True`
0. Create a function that takes a list of **non-repeating** integers as an input
   and then returns the second largest integer in the input list.
    - For example: `[1, 3, 2, 5] -> 3`
    - Hint: `sorted()`
0. Create a function that takes **two inputs**: a list of integers and a single
   integer. The function will count the number of times that the given integer
   appears in the input list.
    - For example: `[1, 3, 5, 4, 11, 4], 4 -> 2`
0. Create a function that takes **two inputs**: a list of integers and a second
   list of integers as inputs and then returns a single list containing all
   elements that are in **both** of the two input lists.
    - For example: `[1, 2, 3, 5], [2, 3, 4, 5] -> [2, 3, 5]`
0. Create a function that takes **two inputs**: a list of strings and a second
   list of strings as inputs and then returns a single list which is the strings
   at each index concatenated.
    - For example: `["a", "hi"], ["b", "bye] -> ["ab", "hibye"]`
    - Note: assume that the two lists are of the same length
0. Create a function that takes a list of lists of integers and then returns
   a single list that is the input list "flattened".
    - For example: `[[1, 6], [3], [7, 9]] -> [1, 6, 3, 7, 9]`
0. Create a function that takes **two inputs**: a list of integers and a second
   list of integers as inputs and then returns a single list such that the
   elements are alternating from the two input lists.
    - For example: `[1, 4, 10], [100, 3, 55, 66, 7] -> [1, 100, 4, 3, 10, 55, 66, 7]`
    - **Do not** assume that the two lists are of the same length
0. Create a function that takes a string of words as an input and returns a
   list of integers representing the length of each those word.
    - For example: `"hey there friend" -> [3, 5, 6]`
0. Create a function that takes a string of numbers separated by spaces as an
   input and returns a list of integers such that each of the numbers in the
   string incremented by one.
    - For example: `"1 5 10 44" -> [2, 6, 11, 45]`
    - Hint: `split()`
0. Create a function that takes a list of integers as an input and returns the
   longest sequence of **identical numbers** in the list.
    - For example: `[1, 1, 6, 1, 5, 5, 6, 6, 6, 6, 8] -> [6, 6, 6, 6]`
0. Create a function that takes a list of integers as an input and returns the
   longest sequence of **consecutive numbers** in the list.
    - For example: `[1, 2, 3, 5, 6, 7, 8, 10] -> [5, 6, 7, 8]`
0. Create a function that takes a string containing tab-separated values
   (TSV) data and returns a list of lists, where each inner list represents a
   row of data.
    - For example: `"100\t88\n1\t2\n3\t62" -> [[100, 88], [1, 2], [3, 62]]`
    - Hint: use `split()` two times
0. Create a function that takes a string of numbers separated by commas as an
   input and returns a list of integers such that each of those numbers is
   squared.
    - For example: `"1,5,10,-9" -> [1, 25, 100, 81]`
    - Hint: `split()`
0. Create a function that takes a list of integers as input and returns a new
   list where each element is the sum of all previous elements.
    - For example: `[1, 2, 3, 11] -> [1, 3, 6, 17]`
0. Create a function that takes a string of the words "one" or "zero" and
   returns a matching list of those words as integers.
    - For example: `"one one zero one" -> [1, 1, 0, 1]`
0. Create a function that takes a list of integers and returns the difference
   between the smallest and the largest elements.
    - For example: `[3, -2, 10, 7, 0, -1] -> 12`
0. Create a function that takes a list of numbers as input and returns the
   average (float).
    - For example: `[1, 2, 3, 4] -> 2.5`
0. Create a function that takes **two inputs**: a list of integers and a second
   list of integers as inputs and then returns a single list containing all
   elements that are in **only one** of the two input lists.
    - For example: `[1, 2, 3], [2, 3, 4, 5] -> [1, 4, 5]`
    - Hint: use two separate loops
0. Create a function that takes a list of strings as an input and then returns
   whether the input list contains any duplicate elements.
    - Hint: use a loop in a loop
