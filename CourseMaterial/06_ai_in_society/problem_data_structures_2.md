# Python Data Structure Wheaties 2

Create two new files in your problem set skeleton. Name one file
`data_structure_wheaties_2.py` and put it in the `src` folder
(`src/data_structure_wheaties_2.py`). Name the other file
`test_data_structure_wheaties_2.py` and put it in the `test` folder
(`test/test_data_structure_wheaties_2.py`).

For each problem, create a new function in the `data_structure_wheaties_2.py` file
and then write at **least two unit tests** in the
`test_data_structure_wheaties_2.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes an integer as an input and returns a boolean of
   whether that number is a prime or not.
1. Create a function that takes a **list of lists of integers** as an input and
   returns the largest integer across all the sub-lists.
2. Create a function that takes a list of integers as an input and returns the
   maximum sum of two numbers in the list.
3. Create a function that takes a list of integers as an input and returns the
   number of times duplicates appear in the list.
4. Create a function that processes a list of student records. Each record is
   a NamedTuple containing `name`, `id`, `major`, and `gpa`. The function
   should take a list of student records and a major as an input and should
   return the average GPA of students in a specified major.
5. Create a function that takes a dictionary as an input and returns a
   dictionary where the keys and values have been reversed.
6. Create a function that takes a dictionary as an input and returns the
   **value** with the highest frequency in a dictionary.
7. Create a function that takes an integer as an input and returns a list
   containing all of the primes less than or equal to the given number.
8. Create a function that takes a string as an input and returns a list of all
   two-length substrings.
   - For example: `"compu" -> ["co", "om", "mp", "pu"]`
9. Create a function that analyzes flight data. Each flight record is a NamedTuple
    containing `flight_number`, `departure_time`, and `arrival_time`. The function
    should take a list of flight data and return the longest flight (time-wise).
10. Create a function that takes a **list of lists of integers** as an input
   and returns a "flattened" version of the input (aka. no sub-lists).
11. Create a function that takes a list of integers and returns how many pairs of
   numbers add up to 10.
   - For example: `[5, 7, 4] -> 0`
   - For example: `[5, 5, 6, 3, 4, 4] -> 3`
12. Create a function that finds the largest number in a list and returns a
    tuple: the number and the list without the number.
   - For example: `[5, 7, 4] -> (7, [5, 4])`
13. Create a function that takes a list of integers as an input and, use the
   function above, to returns a sorted version of the list.
14. Implement a system to track employee hours. Each record is a NamedTuple
   that includes `employee_id` and `hours_worked`. Create a function that takes
   a list of records and a employee id and returns the total hours worked by
   the employee in a given month.
15. Create a function that takes a list of integers as an input and returns the
   length of the longest consecutive elements sequence.
   - For example: `[1, 5, 5, 6, 6, 6, 5, 5, 2] -> 3`
16. Create a function that takes a string as an input and returns a boolean of
   whether the string has balanced parentheses.
   - For example: `"((1 + 2) * 4) + (4 * 5) -> True`
   - For example: `"((1 + 2) * 4 + (4 * 5) -> False`
17. Create a function that takes two dictionaries as inputs. It then returns
   a new dictionary containing all of the key/value pairs that are in **both**
   dictionaries.
18. Create a function that takes a list of integers as an input and then returns
   the maximum sum of non-adjacent numbers.
   - For example: `[17, 100, 101, 5, 8] -> 118`
19. Create a tool for analyzing traffic data. Use a NamedTuple for each data
    point, containing `date`, `location`, and `vehicle_count`. Create a
    function that takes a list of data points as an input and returns the
    busiest location in one day.
20. Create a function that takes a string as an input and returns the longest
   substring without repeating characters.
   - For example: `"hellothere" -> "lother"`
