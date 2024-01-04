## Essential Questions

- How do we create "binary decision trees"?
- What properties does an effective "binary decision tree" have?

## Lesson Plan

This lesson provides an intuitive understanding of decisions trees (and trees
in general). Beginning with just playing, the students learn to create decision
trees and what features lead to the best tree (balanced). From there, we
compare their intuitions with the output of Weka.

### Setup

- Enough games of "Guess Who" for every student in the class
- Paper for them to draw their decision trees
- Up to date ata in `guess_who_data*.csv` that represents game

### Actual Lesson

- Review
    - Supervised
    - Reinforcement
    - Unsupervised
    - Classifier
    - Over-fitting
    - Human vs. Machine learning
- Guess Who is very hot right now
    - Who's played Guess Who?
    - https://www.youtube.com/watch?v=vl4dQrGaOcU
        - 0:00 - 1:30
- Play a game of Guess Who
    - Draw a decision tree as they go
    - Ask winner:
        - What was your strategy?
        - What questions did you ask?
- Have them play two more times and continue to fill in their decision tree
    - Root node/existing nodes should not change
    - If change, shows asked a bad question to begin with
- What's going on here?
    - What is everyone's first question?
        - Who's is best and why?
    - Features
- Weka
    - Show `guess_who_data.csv` in excel
        - Brief aside about how gender is a construct
        - Brief aside about how I did my best, but open to revisions
    - Open `Weka` and select `Explorer`
    - Load up data in `guess_who_data.csv`
        - Click through data
        - Show that `gender` is the _likely_ the best first split
            - Initially starts out balanced
    - Select `Classify`
    - Select `trees` -> `J48`
    - Modify parameters of `J48` by clicking on the `2` after the `-M` option
        - `binarySplits` -> True
        - `minNumObj` -> `1`
        - `unpruned` -> `True`
        - Resulting parameters should be `J48 -U -B -M 1`
    - Load up "Supplied test set" `guess_who_data_training.csv`
        - Just a copy of `guess_who_data.csv` under a different name
    - `Start`
- Discuss
    - How is this a classifier?
    - Why is the test set "weird" in this case?
- Tree terminology
    - Node
    - Leaf
    - Child
    - Balanced
    - Acyclical
    - Similar to 20 questions
        - Exponential growth!
        - Optimum strategy is finding properties that split sets in half
    - Show example code in `guess_who_code.py` of "classes"

#### Homework

- Read `science_of_learning.docx` and prepare for discussion
