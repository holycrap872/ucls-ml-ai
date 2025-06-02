# Python Grab Bag Wheaties (Structured)

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`grab_bag_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/grab_bag_wheaties.py`). Name the other file
`test_grab_bag_wheaties.py` and put it in the `tests` folder
(`tests/test_grab_bag_wheaties.py`).

For each problem, create a new function in the `grab_bag_wheaties.py` file
and then write at **least two unit tests** in the `test_grab_bag_wheaties.py`
file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a string as an input and returns whether all
   characters in the string are unique.
    - For example: `"hello" -> False`
    - For example: `"helLo" -> True`
    - Hint: consider using a set
0. Create a function that takes a dictionary of integers mapped to integers and
   returns True if any key equals its value.
    - For example: `{1: 2, 3: 3, 4: 2} -> True`
0. Create a function that takes a string of comma-separated numbers and returns
   their sum.
    - For example: `"1,2,3,4" -> 10`
    - Hint: `split()`
0. Create a function for analyzing shipping packages. Package records are
   NamedTuples that include `id` (str), `weight` (float), and `dimension`
   (float). Create a function that takes a list of packages and returns a set of
   package IDs that would incur an oversized fee (weight over 50 lbs **OR**
   dimension over 24 inches).
    - For example: `[PR("A1", 45.0, 26.0), PR("B2", 55.0, 12.0)] -> {"A1", "B2"}`
    - For example: `[PR("A1", 45.0, 20.0), PR("B2", 51.0, 12.0)] -> {"B2"}`
0. Create a function that takes a sentence (string) as an input and returns the
   same string with words rotated one position left.
    - For example: `"hello there world" -> "there world hello"`
    - Hint: `pop(0)`
0. Create a function that takes a list of numbers as input and returns a new
   list containing only unique elements **while maintaining order**.
    - For example: `[1, 3, 3, 5, 1, 3, 2] -> [1, 3, 5, 2]`
    - Hint: seen set
    - Hint: accumulator pattern starting with an empty list
0. Create a function for finding suitable rental properties. Property records
   are NamedTuples that include `address` (str), `rent` (float), and
   `square_feet` (int). Create a function that takes a list of properties
   and a maximum price per square foot as inputs and returns a set of addresses
   that are within the budget.
    - For example: `[PR("123 Main", 2000.0, 1000), PR("456 Oak", 1500.0, 900)], 1.8 -> {"456 Oak"}`
0. Create a function that takes an integer as an input and returns a dictionary
   containing all of the numbers that "multiply to" the given number.
    - For example: `12 -> {1: 12, 2: 6, 3: 4, 4: 3, 6: 2, 12: 1}`
    - Hint: `12 % 3 -> 0`, `12 % 5 -> 2`
0. Create a function that takes a sentence (string) as an input and returns
   whether it's a pangram (contains every letter of the alphabet).
    - For example: `"The quick brown FOX jumps over the lazy DOG"` -> True
    - Hint: accumulator pattern starting with an empty set
    - Hint: `isalpha()` and `lower()`
0. Create a function that takes a dictionary of strings mapped to sets as an
   input and returns a dictionary with the keys mapped to the sets' sizes.
    - For example: `{"a": {1, 2, 3}, "b": {4, 5}} -> {"a": 3, "b": 2}`
    - Hint: accumulator pattern starting with an empty dictionary
0. Create a function that takes a list of strings and returns a set of all
   characters that appear exactly once across all strings.
    - For example: `["hello", "World!"] -> {"W", "r", "d", "!"}`
    - Hint: counting dictionary
0. Create a function that takes a string as an input and returns the number of
   times "a" is directly followed by a "b".
    - For example: `"an able labbies arbor" -> 2`
    - **Do not** use `.count()`
    - Hint: `for i in range(len(s) - 1):`
0. Create a function that processes a list of inventory records. Use a
   NamedTuple to represent the records, which includes `item` (str), `quantity`
   (int), and `location` (str). The function should take a list of records and
   return the set of locations that are out of stock (quantity = 0).
    - For example: `[IR("pen", 0, "A1"), IR("paper", 5, "B1"), IR("desk", 0, "A2")] -> {"A1", "A2"}`
0. Create a function that takes a set of integers as an input and returns a
   dictionary where each key is a number and its value is how many numbers in
   the set are smaller than it.
    - For example: {1, 4, 2, 5, 3} -> {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    - Hint: create a helper function called `count_less_than()`
    - Hint: accumulator pattern starting with an empty dictionary
0. Create a function that takes a list of integers as an input and returns the
   "mountain distance" of that list. "Mountain distance" is the sum of all
   of the differences between elements that are adjacent in the list.
    - For example: `[1, 3, 5, 4, 2] -> 7` (`(3 - 1) + (5 - 3) + (5 - 4) + (4 - 2)`)
    - Hint: `abs()`
0. Create a function that takes a list of strings as an input and returns the most
   frequent character across all strings.
    - For example: `["hello", "world"] -> "l"`
    - Hint: counting dictionary
0. Create a function that processes a list of attendance records. Use a
   NamedTuple to represent records, which includes `student` (str), `date`
   (str), and `present` (bool). The function should return a dictionary mapping
   each student to their attendance percentage.
    - For example: `[AR("alice", "2024-01-01", True), AR("alice", "2024-01-02", False)] -> {"alice": 0.5}`
0. Create a function that takes a sentence (string) as an input and returns the
   same string with alternating case.
    - For example: `"hello there" -> "hElLo ThErE"`
    - Hint: use a counter with modulo
    - Hint: accumulator pattern starting with an empty string
0. Create a function that processes a list of score records. Use a NamedTuple
   to represent records, which includes `player` (str) and `score` (int). The
   function should return a NamedTuple containing the highest score and a set of
   players who achieved it.
    - For example: `[SR("alice", 10), SR("bob", 15), SR("carol", 15)] -> HSR(15, {"bob", "carol"})`
0. Create a function that takes a list of integers as an input and returns a
   list of lists containing all pairs that sum to zero.
    - For example: [1, 2, -1, -2, 3] -> [[1, -1], [2, -2]]
    - Hint: `* -1`
0. Create a function that processes transaction records. Use a NamedTuple to
   represent records, which includes `date` (str) and `amount` (float). The
   function should return a dictionary representing the total amount for each
   month.
    - For example: `[TR("2024-01-15", 100.0), TR("2024-01-20", 50.0)] -> {"2024-01": 150.0}`
    - Hint: Use string slicing on the date
0. Create a function that takes an integer N as an input and returns the Nth
   number that contains only 1s and 2s.
    - For example: `3 -> 11` (sequence: 1, 2, 11, 12, 21, 22, 111, ...)
    - For example: `4 -> 21` (sequence: 1, 2, 11, 12, 21, 22, 111, ...)
    - For example: `5 -> 22` (sequence: 1, 2, 11, 12, 21, 22, 111, ...)
0. Create a function that takes a list of integers as an input and returns the
   length of the longest increasing subsequence.
    - For example: `[1, 2, 3, 1, 4] -> 4` (the sequence `1, 2, 3, 4`)
    - Hint: nested loops
0. Create a function that takes a list of integers as an input and returns
   whether it can be split into two sublists of equal sum.
    - For example: `[1, 5, 5, 10, 1] -> True` (can be split into `[1, 5, 5]` and `[10, 1]`)
    - Hint: consider the total sum first
0. Create a function that takes a list of integers as an input and returns a new
   list where each element is replaced by its distance to the nearest zero.
    - For example: `[1, 0, 2, 0, 4] -> [1, 0, 1, 0, 1]`
    - Hint: create a helper function
0. Create a function that processes a set of message records. Use a NamedTuple
   to represent records which includes `sender` (str), `receiver` (str), and
   `text` (str). The function should return the set of all users who both sent
   and received messages.
    - For example: `[MR("alice", "bob", "hi"), MR("lou", "alice", "hello")] -> {"alice"}`
    - Hint: intersection
0. Create a function that takes a string as an input and returns the length of
   the longest substring with at most 2 different characters.
    - For example: `"ecceba" -> 4` (`"ecce"` has length 4)
    - Hint: sliding window with counter
0. Create a function that processes a list of student lab records. Use a
   NamedTuple to represent records which includes `student` (str), `lab_number`
   (int), and `time_spent` (int, in minutes). The function should identify
   "struggling students" who spend more than 1.5x the average time across all
   students.
    - For example: `[LR("amy", 1, 60), LR("dj", 2, 550), LR("bob", 1, 140)] -> {"dj"}`
