## EQ's

- Why are tests important?
- What is the best kind of test?

## Lesson Plan

The goal of this lesson is to give students another chance to reflect and
try and load up their "Python knowledge". First, we will do a quick review
about what they ran into. After that, I will introduce unit tests and explain
why they're so important. Finally, as a class we will solve a problem - complete
with unit tests - before the students finally strike out on their own. While
they're working, I will go around and suggest various things (e.g., types and
tests) that will help each of them as they encounter a problem.

### Setup

- None

### Actual Lesson

- Review
    - What did we do last class?
    - How do you know that you are/are not in a workspace?
    - Techniques for thinking about problems
        - Accumulator pattern
- Unit Testing
    - Show simple piece of code
        ```python
        def print_name(name: str) -> str:
            lower_name = name.lower()
            if lower_name.startswith("eric"):
                return "Uhhhhh... you wrote this"
            else:
                return "Hello " + name
        ```
    - What tests should be created?
    - Why?
- Class program
    - Create function takes a list of ints and returns a list of all the even numbers in the input
    - Create three unit tests
- Today going to just program as much as we can
- Continue working on `Skills Assessment`

## Homework

- Finish up to and including Problem 2.4
