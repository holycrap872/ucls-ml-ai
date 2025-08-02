## Essential Questions

- How can we use randomness to solve hard problems?
- How does the quantity and quality of data affect ML outcomes?

## Lesson Plan

The goal of this lesson is to have students appreciate how having "good data"
is important for making ML calculations. Put another way: garbage in, garbage
out. To illustrate this, students will be asked to come up with a bunch of
random numbers and see how bad humans are at actually creating random numbers.
In addition, the goal is to give students experience working with/parsing .csv
files.

> I was a bit floored by how much of a jump getting data out of a .csv file was
  for them. Be sure to go _very_ slow and explain exactly how the csv file maps
  to a string.

### Setup

- YouTube video loaded up
    - Monte Carlo method: https://youtu.be/7ESK5SaP-bc?si=UuuSXWkl5mz-Vm8K&t=62
- Solution associated with "Monte Carlo Circle" lesson printed out so students can analyze it
    - `monte_circle_1.py`
    - TODO: Double check it's at the appropriate level of difficulty
- `random_numbers` GoogleSheets loaded up on Schoology
    - Example: https://docs.google.com/spreadsheets/d/1G52YSMPUyLe6uR_XOZGbHVeXh_G6HGZqlXgZ4w-oYsc
    - Make sure anyone at Lab can see it
    - Make sure it's in Editor mode for all
- `Class Randomness Worksheet` loaded up on Schoology
    - Structured: https://docs.google.com/document/d/1436AW0gXcQYpAqIjBmUheMjHBW3KaTdIMCMFE5IxwYI
    - Unstructured: https://docs.google.com/document/d/1BeyVPK8OWGAlv5E858vHgJkx7p1-JK8r69cCflRlsFA

### Actual Lesson

- Review
    - What was easy?
    - What was hard?
    - What did the lesson show?
        - Importance of lots of data
    - Show YouTube video
        - https://youtu.be/7ESK5SaP-bc?si=UuuSXWkl5mz-Vm8K&t=62
        - How does this relate to what we just did?
- Code discussion
    - Hand out _my_ solution for "Monte Carlo Circle" worksheet: `monte_circle_1.py`
    - Discuss
- Randomness talk
    - Random is hard
    - Humans are really bad at random
    - Random is important for things like Monte Carlo
- Today going to see how hard randomness is
    - Have everyone open a google sheet and put in 50 numbers between 0-9 (inclusive)
    - Show everyone how to download that as a .csv file
    - Open the file and parse it
        - What are the delimiters?
        - Manually (parse on "\n" and ",")
- "Pick the worksheet that works for you"
    - Pick structured/unstructured
    - Talk through worksheet
- Go!

### Homework

- TIL entry of "CSV" files
- `Python List Wheaties` 14 - 16
