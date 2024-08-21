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

- Youtube video loaded up
    - Monte Carlo method: https://youtu.be/7ESK5SaP-bc?si=HMfKcjuDAKW5swWD
- Shared GoogleSheets document
    - Columns with `Name` and `Number`

### Actual Lesson

#### Day 1

- Review
    - What was easy?
    - What was hard?
    - What did the lesson show?
    - Show YouTube video
        - https://youtu.be/7ESK5SaP-bc?si=HMfKcjuDAKW5swWD
        - How does this relate to what we just did?
- Opening problem (as a class):
    - Get out the first column of the following two-row data string: "1,2,3\n4,5,6"
- Randomness talk
    - Random is hard
    - Humans are really bad at random
    - Random is important for things like Monte Carlo
- Today going to see how hard randomness is
    - Have everyone open a google sheet and put in 20 numbers between 0-10
    - Show everyone how to download that as a .csv file
    - Open the file and parse it
        1. Manually (parse on new lines and ",")
- Graph:
    - Bar chart of even/odds

#### Day 2

- Review
    - What is randomness?
    - Why is it hard?
- Go over previous problem
    - Pick person and discuss
    - Edit code so don't use `num_even`/`num_odd` variables but instead use 2-element array
- Classwork:
    - Bar chart of total number of each number
    - Scatter plot of consecutive pairs of numbers
    - Bonus `s=` parameter to determine size of scatterplot
- Reflection
    - What happens if used "random numbers" produced by humans instead of `random.random()`?

### Homework

- None (or finish if didn't)

### Resources

- Maybe do an experiment on the "hot hand"
    - https://nautil.us/the-hot-hand-is-not-a-myth-643539
- Maybe do an experiment on monty hall problem
