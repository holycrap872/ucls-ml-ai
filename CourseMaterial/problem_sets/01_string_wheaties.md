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
   - Hint `[]`
1. Create a function that takes a sentence (string) as an input and then returns
   a string of the fourth, five, sixth, and seventh characters of the input string.
   - For example: `"hi there" -> "ther"`
   - Hint: `[x:y]`
2. Create a function that takes a sentence (string) as an input and then returns
   a version of the input string with the first two and last two characters removed.
   - For example: `"hello there" -> "llo the"`
   - Hint: slicing
3. Create a function that takes a sentence (string) as an input and then returns
   a boolean of whether the string ends with "ing".
   - Hint: `in`
4. Create a function that takes a sentence (string) as an input and then returns
   the middle character of the input string. If the string is of even length, it
   returns the middle two characters.
   - For example: `"hello!" -> "ll"`
   - Hint: `/ 2` and `% 2`
5. Create a function that takes a sentence (string) as an input and then, using
   a loop, returns the reverse of the input string. Do **not** use something like
   `[::-1]`.
   - Hint: accumulator pattern
6. Create a function that takes a sentence (string) as an input and then returns
   the input string repeated 4 times.
   - For example: `"hi!" -> "hi!hi!hi!hi!"`
   - Hint: `*`
7. Create a function that takes a sentence (string) as an input and then returns
   the number of words in the input string.
   - For example: `"hello there" -> 2`
   - Hint: `count()` OR `split()`
8. Create a function that takes a sentence (string) as an input and then returns
   the longest word in the input string.
   - Hint: `split()`
9. Create a function that takes a sentence (string) as an input and then returns
   the number of vowels in the input string.
   - For example: `"hello there" -> 4`
   - Hint: use a string's `count()` function multiple times
10. Create a function that takes a sentence (string) as an input and then returns
    all email addresses (words with `@`) within the input string as a list of
    strings.
    - For example: `"hi e@test.com and r@what.com" -> ["e@test.com", "r@what.com"]`
    - Hint: accumulator pattern
11. Create a function that takes a sentence (string) as an input and then returns
    a version of the input string where the first letter of every word is
    capitalized.
    - For example: `"hello there" -> "Hello There"`
    - Hint: `split()` and `upper()`
12. Create a function that takes **two** words (strings) as inputs and then
    returns their longest common prefix.
    - For example: `"apple", "application" -> "appl"`
    - Hint: accumulator pattern
13. Create a function that takes a sentence (string) as an input and then returns
    a version of the input string where all uppercase letters are switched into
    lowercase and all lowercase letters are switch into uppercase.
    - For example: `"Hello There" -> "hELLO tHERE"`
    - Hint: `isupper()`, `upper()`, `lower()`
