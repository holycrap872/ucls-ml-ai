## Essential Questions

- How we capture and process data about text documents?
- What are ways we can create knowledge about text documents?

## Lesson Plan

In this lesson, students will wrap up the `Intro to Data Science` unit. First,
we will review what we was learned. Then, we will discuss the overall flow of
the "Plotting the Classics" worksheet. Care will be taken to talk about how this
particular worksheet focuses more on a "data scientist" style of printing out
answers and then commenting out unused code. Finally, students start working
on the 

### Setup

- Solution associated with "Class Randomness" lesson printed out so students can analyze it
    - `class_randomness_solution.py`
    - TODO: Double check it's at the appropriate level of difficulty
- Two novels loaded up in Schoology
    - _The Great Gatsby_
    - _Little Women_
    - Both novels having keyword "START_CHAPTER", ... replacing existing chapter delimiters
        - Allows students to more easily parse
- `Plotting the Classics Worksheet` loaded up in Schoology
    - Structured: https://docs.google.com/document/d/1k0Y46h60qx6GHhTKwXQxuN1iBJZv7heu62betDO0f0o
    - Unstructured: https://docs.google.com/document/d/1WFiQGkNBqBaX5Cd6VJZwwE7HJb9LmMvjO0T-sgKW6Lk
- `data_sci_template.py` loaded up

### Actual Lesson

- Review
    - Monte Carlo
    - Randomness
    - Data quality
    - Parsing text
- Code discussion
    - Hand out _my_ solution for "Class Randomness" worksheet
        - `class_randomness_solution.py`
    - Discuss
- Setup
    - This worksheet will be analyzing books
    - Trying to "extract knowledge" from them
- Coding as a data-scientist
    - Answer question via print
    - Move onto next question
    - Show an example of:
        - creating a helper function to read in a the text of a book
        - creating a function to answer questions about the book
        - commenting out stuff as get answer
- Show/discuss basic program template
    - See `data_sci_template.py`
    - Go through some sample questions from worksheet and answer them
        - First character
        - Last character
    - How to use helper functions
        - Code normalization
- Today going to do an individual project
    - On Schoology
    - Emphasize mostly a review
    - Make sure to read though the worksheet and ask any questions
- Go!

### Homework

- Finish `Explore Twice` section
