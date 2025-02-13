# Python Advanced Data Structure Wheaties (Unstructured)

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`adv_data_structure_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/adv_data_structure_wheaties.py`). Name the other file
`test_adv_data_structure_wheaties.py` and put it in the `test` folder
(`test/test_adv_data_structure_wheaties.py`).

For each problem, create a new function in the `adv_data_structure_wheaties.py` file
and then write at **least two unit tests** in the
`test_adv_data_structure_wheaties.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a list of integers as an input and returns a new
   list of all of the integers that are **odd** in the original list.
    - For example: `[3, 1, 7, 6, 6, 10] -> [3, 1, 7]`
0. Create a function that takes a dictionary of integers mapped to integers as
   an input and returns a new dictionary that contains all of the key/value
   pairs from the input dictionary where: the keys are even and the values are odd.
    - For example: `{2: 5, 3: 6, 7: 7, 4: 11} -> {2: 5, 4: 11}`
0. Create a function that takes a list of integers as an input and returns a new
   list of all of the integers in the original list that have exactly two zeroes.
    - For example: `[101, 500, 2031, 2030, 9000] -> [500, 2030]`
    - Hint: Convert the integers to strings
0. Create a function that takes an integer and a list of integers as inputs and
   returns a boolean of whether the integer is divisible by ALL of the integers
   in the list.
    - For example: `12, [1, 2, 3, 4, 6] -> True`
    - For example: `9, [1, 3, 4] -> False`
0. Create a function that takes an integer as an input and returns a boolean of
   whether that number is a prime or not.
    - For example: `12 -> False`
    - For example: `13 -> True`
0. Create a function that takes a **list of lists of integers** as an input and
   returns the largest integer across all of the sub-lists.
    - For example: `[[9, 1], [14, 11], [10]] -> 14`
0. Create a function that processes a list of student records. Each student
   record is a NamedTuple containing `name` (str), `id` (int), `major` (str),
   and `gpa` (float). The function should take a list of student records and
   a major as inputs and return a float that is the average GPA of students in
   the specified major.
    - For example: `[SR("eric", "cs", 3.3), SR("jen", "bio", 3.7)], "cs" -> 3.3`
0. Create a function that takes a list of integers as an input and returns the
   maximum sum of two **different** numbers in the list.
    - For example: `[4, 8, 2, 3] -> 12`
    - Hint: Return `None` if you don't have all the necessary information
0. Create a function that takes a list of integers as an input and returns the
   number of times duplicates appear in the list.
    - For example: `[1, 1, 5, 1, 5, 6] -> 3`
    - For example: `[1, 5, 6, 1] -> 1`
0. Create a function that aggregates weather data. Use a NamedTuple to represent
   each weather record, which includes `date` (a "YYYY-MM-DD" str), `temperature`
   (int), and `precipitation` (float). The function should take three inputs: a
   list of weather records, a start date (a "YYYY-MM-DD" string), and an end
   date (a "YYYY-MM-DD" string). It should then return both the average
   temperature (float) and the total precipitation over a given period (float).
    - Hint: The fact you're using a "YYYY-MM-DD" string means you can use `<=`
      to easily compare dates.
0. Create a function that takes a dictionary as an input and returns a
   dictionary where the keys and values have been reversed.
    - For example: `{"a": 1, "b": 2} -> {1: "a", 2: "b"}`
    - Note: It's ok if duplicate values result in some things being "dropped"
0. Create a function that takes a dictionary as an input and returns the
   **value** with the highest frequency in a dictionary.
    - For example: `{"a": 1, "b": 2, "c": 1} -> 1`
0. Create a function that takes an integer as an input and returns a list
   containing all of the primes less than or equal to the given number.
    - For example: `11 -> [2, 3, 5, 7, 11]`
0. Create a function that takes a string as an input and returns a list of all
   two-length substrings.
    - For example: `"compu" -> ["co", "om", "mp", "pu"]`
0. Create a function that analyzes flight data. Each flight record is a
   NamedTuple containing `flight_number` (int), and `departure_date` (a
   `"YYYY-MM-DD"` string). The function should take a set of flight records,
   a start date, and an end date as inputs and return a list of all the
   flight numbers that departed within the given time period.
    - Hint: The fact you're using a "YYYY-MM-DD" string means you can use `<=`
      to easily compare dates.
0. Create a function that takes a **list of lists of integers** as an input
   and returns a "flattened" version of the input (aka. no sub-lists).
    - For example `[[1, 3], [4, 3, 100]] -> [1, 3, 4, 3, 100]`
0. Create a function that takes a list of integers as an input and returns a
   NamedTuple. The NamedTuple should have the properties `largest_int` (int)
   and `rest` (the original list without the `largest_int`).
    - For example: `[5, 7, 4] -> (7, [5, 4])`
    - Note: You **cannot** use `sorted()` or `sort()`
0. Create a function that takes a list of integers as an input and returns
   a sorted version of the list.
    - For example: `[5, 7, 4, 3] -> [3, 4, 5, 7]`
    - Note: You **must use** the function your created for the previous problem
0. Implement a system to track employee hours. Employee hours should be tracked
   via a NamedTuple that includes `employee_id` (int) and `hours_worked` (int).
   Create a function that takes a list of the employee records and a list of
   employee ids and returns the total hours (int) worked by those employees.
0. Create a function that takes a list of integers and returns how many pairs of
   numbers add up to 10.
    - For example: `[5, 7, 4] -> 0`
    - For example: `[5, 5, 6, 3, 4, 4] -> 3`
0. Create a function that takes a list of integers as an input and returns
   a NamedTuple that contains information on which number has the longest
   consecutive elements sequence and what the length of the sequence was.
    - For example: `[1, 5, 5, 6, 6, 6, 5, 5, 2] -> NamedTuple(val=6, length=3)`
0. Create a function that takes two dictionaries as inputs. It then returns
   a new dictionary containing all of the key/value pairs that are in **both**
   dictionaries.
    - For example: `{1: 5, 3: 7}, {3: 4, 1: 5, 9: 10} -> {1: 5}`
0. Create a tool for analyzing traffic data. Use a NamedTuple for each data
   point that includes `date` ("YYYY-MM-DD" string), `location` (string), and
   `vehicle_count` (int). Create a function that takes a list of data points
   as an input and returns the busiest location (str) in one day.
    - Note: There can be two or more NamedTuples about the same location
0. Create a function that takes a list of integers as an input and then returns
   the maximum sum of **non-adjacent** numbers.
    - For example: `[17, 100, 101, 5, 8] -> 118`
0. Create a function that takes a string as an input and returns a boolean of
   whether the string has balanced parentheses.
    - For example: `"((1 + 2) * 4) + (4 * 5) -> True`
    - For example: `"))(( -> False`
    - For example: `"(()) -> True`
    - For example: `"((1 + 2) * 4 + (4 * 5) -> False`
    - For example: `"((1 + 2))) * 4 + ((4 * 5) -> False`
0. Create a function that takes a string as an input and returns the longest
   substring without repeating characters.
    - For example: `"hellothere" -> "lother"`
