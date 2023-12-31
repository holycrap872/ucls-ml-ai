## Essential Questions

- How do we create "binary decision trees"?
- What properties does an effective "binary decision tree" have?

## Lesson Plan

This lesson provides an intuitive understanding of decisions trees (and trees
in general). Beginning with just playing, the students learn to create decision
trees and what features lead to the best tree (balanced). From there, we
compare their intuitions with the output of Weka.

### Setup

- Enough games of "guess who" for every student in the class
- Paper for them to draw their decision trees
- Up to date ata in `guess_who_data*.csv` that represents game

### Actual Lesson

- Play a game of Guess Who
    - Ask winner:
        - What was your strategy?
        - What questions did you ask?
    - Draw a decision tree as they go
- Have them play two more times and fill in their decision tree
    - Root node/existing nodes should not change
    - If change, shows asked a bad question to begin with
- What's going on here?
    - What is every one's first question?
        - Who's is best and why?
    - Features
    - Tree terminology
        - Node
        - Leaf
        - Child
        - Balanced
- Weka
    - Open `Weka` and select `Explorer`
    - Load up data in `guess_who_data.csv`
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

#### Homework

- Encode a decision tree of 4 Guess Who that I give you
    - Have it play based on the tree you encode
    - Can use ChatGPT to create code
