# Python Advanced Data Structure Wheaties

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

0. Create a function that takes an integer as an input and returns a boolean of
   whether that number is a prime or not.
1. Create a function that processes a list of student records. Each student
   record is a NamedTuple containing `name` (str), `id` (int), `major` (str),
   and `gpa` (float). The function should take a list of student records and
   a major as inputs and return a float that is the average GPA of students in
   the specified major.
2. Create a function that takes a **list of lists of integers** as an input and
   returns the largest integer across all of the sub-lists.
3. Create a function that takes a list of integers as an input and returns the
   maximum sum of two numbers in the list.
4. Create a function that takes a list of integers as an input and returns the
   number of times duplicates appear in the list.
5. Create a function that aggregates weather data. Use a NamedTuple to represent
   each weather record, which includes `date` (a "YYYY-MM-DD" str), `temperature`
   (int), and `precipitation` (float). The function should take three inputs: a
   list of weather records, a start date (a "YYYY-MM-DD" string), and an end
   date (a "YYYY-MM-DD" string). It should then return both the average
   temperature (float) and the total precipitation over a given period (float).
    - Hint: The fact you're using a "YYYY-MM-DD" string means you can use `<=`
      to easily compare dates.
6. Create a function that takes a dictionary as an input and returns a
   dictionary where the keys and values have been reversed.
   - For example: `{"a": 1, "b": 2} -> {1: "a", 2: "b"}`
   - Note: It's ok if duplicate values result in some things being "dropped"
7. Create a function that takes a dictionary as an input and returns the
   **value** with the highest frequency in a dictionary.
   - For example: `{"a": 1, "b": 2, "c": 1} -> 1`
8. Create a function that takes an integer as an input and returns a list
   containing all of the primes less than or equal to the given number.
   - For example: `11 -> [2, 3, 5, 7, 11]`
   - Hint: Use the function your created for problem 0 in your solution
9. Create a function that takes a string as an input and returns a list of all
   two-length substrings.
   - For example: `"compu" -> ["co", "om", "mp", "pu"]`
10. Create a function that analyzes flight data. Each flight record is a
    NamedTuple containing `flight_number` (int), and `departure_date` (a
    "YYYY-MM-DD" string). The function should take a set of flight records,
    a start date, and an end date as inputs and return a list of all the
    flight numbers that departed within the given time period.
    - Hint: The fact you're using a "YYYY-MM-DD" string means you can use `<=`
      to easily compare dates.
11. Create a function that takes a **list of lists of integers** as an input
    and returns a "flattened" version of the input (aka. no sub-lists).
    - For example `[[1, 3], [4, 100]] -> [1, 3, 4, 100]`
12. Create a function that finds the largest number in a list and returns a
    tuple: the number and the list without the number.
    - For example: `[5, 7, 4] -> (7, [5, 4])`
13. Create a function that takes a list of integers as an input and returns
    a sorted version of the list.
    - For example: `[5, 7, 4, 3] -> [3, 4, 5, 7]`
    - Hint: Use the function your created for problem 13 in your solution
14. Implement a system to track employee hours. Employee hours should be tracked
    via a NamedTuple that includes `employee_id` (int) and `hours_worked` (int).
    Create a function that takes a list of the employee records and a list of
    employee ids and returns the total hours (int) worked by those employees.
15. Create a function that takes a list of integers and returns how many pairs of
    numbers add up to 10.
    - For example: `[5, 7, 4] -> 0`
    - For example: `[5, 5, 6, 3, 4, 4] -> 3`
16. Create a function that takes a list of integers as an input and returns
    a NamedTuple that contains information on which number has the longest
    consecutive elements sequence and what the length of the sequence was.
    - For example: `[1, 5, 5, 6, 6, 6, 5, 5, 2] -> NamedTuple(val=6, length=3)`
17. Create a function that takes two dictionaries as inputs. It then returns
    a new dictionary containing all of the key/value pairs that are in **both**
    dictionaries.
18. Create a tool for analyzing traffic data. Use a NamedTuple for each data
    point that includes `date` ("YYYY-MM-DD" string), `location` (string), and
    `vehicle_count` (int). Create a function that takes a list of data points
    as an input and returns the busiest location (str) in one day.
19. Create a function that takes a list of integers as an input and then returns
    the maximum sum of **non-adjacent** numbers.
    - For example: `[17, 100, 101, 5, 8] -> 118`
20. Create a function that takes a string as an input and returns a boolean of
    whether the string has balanced parentheses.
    - For example: `"((1 + 2) * 4) + (4 * 5) -> True`
    - For example: `"((1 + 2) * 4 + (4 * 5) -> False`
21. Create a function that takes a string as an input and returns the longest
    substring without repeating characters.
    - For example: `"hellothere" -> "lother"`
