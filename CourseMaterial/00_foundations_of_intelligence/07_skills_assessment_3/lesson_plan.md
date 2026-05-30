## Essential Questions

- Why are tests important?
- What is the best kind of test?

## Lesson Plan

The goal of this lesson is to give students another chance to reflect and
try and load up their prior Python knowledge. First, we will do a quick review
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
- Unit tests
    - Show a function I wrote — does it work?
        ```python
        def can_ride_coaster(height: int, age: int) -> bool:
            """Rider must be at least 48 inches AND at least 8 years old."""
            if height >= 48 or age >= 8:
                return True
            return False
        ```
    - Read the spec out loud, then the code
        - What does the spec say?
        - What does the code actually do?
        - Find an input where the two disagree
    - Now: how do we *prove* the function is broken in a way the computer can check?
        - Write an `assert` that captures the disagreement
        - `assert can_ride_coaster(20, 50) == False`  # short kid, way too old
        - Run it. Watch it fail.
    - That's a unit test. Two more things to notice:
        - The test names a specific input — not a vibe, an input
        - Once you fix the function, the test stays around forever as a
          guarantee the bug can't come back unnoticed
    - This function comes from a project we'll come back to in a couple weeks
- Class program
    - Create function takes a list of ints and returns a list of all the even numbers in the input
    - Create three unit tests — at least one should catch a wrong implementation
- Today going to just program as much as we can
- Continue working on `Skills Assessment Worksheet`

### Homework

- Finish up to and including Problem 2.4 of `Skills Assessment Worksheet`
