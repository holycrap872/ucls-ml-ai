## Lesson Plan

The goal of this lesson is to have the students experience .csv files and to
work with the data a little bit.

> I was a bit floored by how much of a jump getting data out of a .csv file was
  for them. Be sure to go _very_ slow and explain exactly how the csv file maps
  to a string.

### Setup

Have a google sheet ready to go with columns for `Name` and `Number`. Bonus
points if you have a formula for checking that the numbers are between 0 and 9.

### Actual Lesson

#### Day 1

- Reflection
    - What was easy?
    - What was hard?
    - What did the lesson show?
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

- Reflection
    - What is randomness
    - Why is it hard
- Go over previous problem
    - Pick person and discuss
    - Edit code so don't use `num_even`/`num_odd` variables but instead use 2-element array
- Classwork:
    - Bar chart of total number of each number
    - Scatter plot of consecutive pairs of numbers
    - Bonus `s=` parameter to determine size of scatterplot

### Homework

None (or finish if didn't)

### Resources

- Maybe do an experiment on the "hot hand"
    - https://nautil.us/the-hot-hand-is-not-a-myth-643539
- Maybe do an experiment on monty hall problem
