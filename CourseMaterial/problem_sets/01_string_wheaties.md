# Python String Wheaties

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`string_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/string_wheaties.py`). Name the other file `test_string_wheaties.py`
and put it in the `test` folder (`test/test_string_wheaties.py`).

For each problem, create a new function in the `string_wheaties.py` file and
then write at **least two unit test** in the `test_string_wheaties.py` file.

# Problems

### Problems using **parameters** for input and `return` for output

0. Create a function that takes a sentence (string) as an input and then returns
   the first and last characters of the input string as a string.
    - For example: `"hi there" -> "he"`
    - Hint: You can access the last character of a string with `[-1]`
0. Create a function that takes a sentence (string) as an input and then returns
   a string of the fourth, fifth, sixth, and seventh characters of the input string.
    - For example: `"hi there" -> "ther"`
    - Hint: You can "slice" out a substring of a string using `[x:y]`
0. Create a function that takes a sentence (string) as an input and then returns
   a version of the input string with the first two and last two characters removed.
    - For example: `"hello there" -> "llo the"`
    - Hint: slicing
0. Create a function that takes a sentence (string) as an input and then returns
   a boolean of whether the string ends with "ing".
    - Hint: slicing
0. Create a function that takes a sentence (string) as an input and returns the
   same string with all spaces and exclamation points removed.
    - For example: `"hello! there!" -> "hellothere"`
    - Hint: `replace()`
0. Create a function that takes a sentence (string) as an input and then returns
   the number of words in the input string.
    - For example: `"hello there" -> 2`
    - Hint: `count()` OR `split()`
0. Create a function that takes a sentence (string) as an input and then, using
   a loop, returns the reverse of the input string.
    - **Do not** use something like `[::-1]`.
    - Hint: accumulator pattern
0. Create a function that takes a sentence (string) as an input and then returns
   the input string repeated 4 times.
    - For example: `"hi!" -> "hi!hi!hi!hi!"`
    - Hint: string multiplication
0. Create a function that takes a sentence (string) as an input and returns the
   number of digits in the string.
    - For example: `"hello 123" -> 3`
    - Hint: accumulator pattern combined with `isdigit()`
0. Create a function that takes a sentence (string) as an input and then returns
   the middle character of the input string. If the string is of even length, it
   returns the middle two characters.
    - For example: `"hello!" -> "ll"`
    - Hint: `/ 2` and `% 2`
0. Create a function that takes a sentence (string) and a number N as an input and
   returns a string containing every Nth character.
    - For example: `"hello there", 2 -> "hlotee"`
    - Hint: accumulator pattern combined with using `range()` with step
0. Create a function that takes a sentence (string) as an input and then returns
   the longest word in the input string.
    - Hint: `split()`
    - Hint: accumulator pattern
0. Create a function that takes a sentence (string) as an input and then returns
   the number of vowels in the input string.
    - For example: `"hello there" -> 4`
    - Hint: use string's `count()` function multiple times
0. Create a function that takes a sentence (string) as an input and then returns
   a version of the input string where the first letter of every word is
   capitalized.
    - For example: `"hello there" -> "Hello There"`
    - Hint: use the accumulator pattern combined with `split()` and `upper()`
0. Create a function that takes **two** words (strings) as inputs and then
   returns their longest common prefix.
    - For example: `"apple", "application" -> "appl"`
    - Hint: accumulator pattern
0. Create a function that takes a sentence (string) as an input and then returns
   a version of the input string where all uppercase letters are switched into
   lowercase and all lowercase letters are switched into uppercase.
    - For example: `"Hello There" -> "hELLO tHERE"`
    - Hint: `isupper()`, `upper()`, `lower()`
0. Create a function that takes a sentence (string) as an input and returns the
   ratio of uppercase letters (float).
    - For example: `"Hello There" -> .2` (2 out of 10 characters are uppercase)
    - Hint: accumulator pattern
0. Create a function that takes a sentence (string) as an input and then returns
   all email addresses (words with `@`) within the input string as a list of
   strings.
    - For example: `"hi e@test.com and r@what.com" -> ["e@test.com", "r@what.com"]`
    - Hint: accumulator pattern
