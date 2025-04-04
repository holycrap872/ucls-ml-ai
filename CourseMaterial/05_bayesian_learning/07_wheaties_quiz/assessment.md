# Python Wheaties Quiz

Create two new files in your `ProblemSetSkeleton` workspace. Name one file
`quiz_2_wheaties.py` and put it in the `src/skeleton` folder
(`src/skeleton/quiz_2_wheaties.py`). Name the other file `test_quiz_2_wheaties.py`
and put it in the `test` folder (`test/test_quiz_2_wheaties.py`).

For each problem, create a new function in the `quiz_2_wheaties.py` file and
then write at **least two unit tests** in the `test_quiz_2_wheaties.py` file.

## Grading:

- 10% for using proper types
- 50% for correct functionality
- 25% for tests that "stress" different paths through the functions
- 15% for reflection

# Problems

0. Create a function that takes a list of integers as an input and returns the
   product of all even numbers PLUS the product of all odd numbers in the list.
    - For example: `[1, 2, 3, 4, 5] -> 23` since `8 (2 * 4) + 15 (1 * 3 * 5) -> 23`
    - Hint: multiple accumulator variables
    - Hint: use the modulo (`%`) operator
0. Create a function that takes a list of people and categorizes them into age
   ranges. Use a NamedTuple to represent a person, which includes `name` (str)
   and `age` (int). The function should return a dictionary where the keys are
   age groups (`"child"` (0-12), `"teen"` (13-19), `"adult"` (20+)) and the
   values are sets of names in that group.
    - For example: `[Pr("Al", 10), Pr("Jen", 25)] -> {"child": {"Al"}, "adult": {"Jen"}}`
    - Hint: Create a version of a counting dictionary

# Reflection

0. In 1-2 sentences, explain how your predicted grade matched up with how you
   felt while taking the quiz **and** what this says about your preparation.
   ```









   ```
0. In 1-2 sentences, identify a particular _good_ habit you have while interacting
   with ChatBots that you would like to continue to use **and** why it's helpful.
   ```









   ```
0. In 1-2 sentences, identify a particular _bad_ habit you use while interacting
   with ChatBots that you would like to eliminate **and** why it's bad.
   ```









   ```
